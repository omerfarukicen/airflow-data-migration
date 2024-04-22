import datetime as dt
from airflow import DAG
from airflow.decorators import task
from airflow.providers.oracle.hooks.oracle import OracleHook
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.utils.dates import days_ago

def toDateString(dataDfRow, fieldName):
    strDate = dataDfRow[fieldName].strftime('%Y-%m-%d %H:%M:%S')
    return strDate

@task
def get_last_update_date_postgres():
    pg_hook= PostgresHook(postgres_conn_id='musteri_postgres_conn')
    data = pg_hook.get_pandas_df(sql='select max(guncelleme_tarihi) son_guncellenme_tarihi from airflow_ms_musteri') 
    return toDateString(data.iloc[0], 'son_guncellenme_tarihi')


@task
def get_data_oracle(sonGuncellenmeTarihi):
    pg_hook= OracleHook(oracle_conn_id='pusula_conn')
    data = pg_hook.get_pandas_df(
         sql=f"""
             SELECT       
                mm.ID,        
                mm.GUNCELLEME_TARIHI,               
                mm.AD,
                mm.SOYAD,
                mm.CINSIYET,
                mm.DOGUM_TARIH,
                mm.YUKSEK_RISK_GRUBUNDA_MI,
                mm.BANK_HESAP_ADI,
                mm.BANK_HESAP_NO,
                mm.YABANCI_AD_UNVAN
            FROM MS_MUSTERI mm
            WHERE GUNCELLEME_TARIHI  > TO_DATE('{sonGuncellenmeTarihi}', 'YYYY-MM-DD HH24:MI:SS')
            """) 
    return data

@task
def update_data_postgers(data):
    oracle_hook= PostgresHook(postgres_conn_id='musteri_postgres_conn')      
    for index, row in data.iterrows():
        update_query= f"""
            update airflow_ms_musteri m
            set
                guncelleme_tarihi = '{row['GUNCELLEME_TARIHI']}',     
                ad = '{row['AD']}',            
                soyad = '{row['SOYAD']}'
            where m.id = {row['ID']} 
        """
        oracle_hook.run(update_query)        

default_args = {
    'owner': 'airflow',    
    'start_date': days_ago(1),
    'retries': 1,
}

with DAG(
    'a-update-temp-airflow-ms-musteri-oracle-postgres',
    default_args=default_args,
    description='Postgres airflow_ms_musteri tablosundaki en yeni guncelleme tarihi ile Oracle MS_MUSTERI tablosunda bu tarihten sonra güncellenmiş kayıtları çeker, postgres tarafında günceller.',
    start_date= dt.datetime(2024,3,1),
    schedule_interval='*/5 * * * *'
    ) as dag:
        sonGuncellenmeTarihi = get_last_update_date_postgres()
        data = get_data_oracle(sonGuncellenmeTarihi)
        update_data_postgers(data)
