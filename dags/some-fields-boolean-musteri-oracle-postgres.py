import datetime as dt
from airflow import DAG
from airflow.decorators import task
from airflow.providers.oracle.hooks.oracle import OracleHook
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.utils.dates import days_ago

@task
def get_data_oracle():
    oracle_hook= OracleHook(oracle_conn_id='pusula_conn')
    data = oracle_hook.get_pandas_df(
         sql="""
            SELECT       
                mm.OLUSTURULMA_TARIHI,
                mm.GUNCELLEME_TARIHI,
                mm.ID,
                enDurum.ACIKLAMA DURUM,
                mm.AD,
                mm.SOYAD,
                enCinsiyet.ACIKLAMA CINSIYET,
                mm.DOGUM_TARIH,
                mm.YUKSEK_RISK_GRUBUNDA_MI,
                mm.BANK_HESAP_ADI,
                mm.BANK_HESAP_NO,
                mm.YABANCI_AD_UNVAN               
            FROM MS_MUSTERI mm 
                LEFT JOIN GNL_ENUM_DEGER enCinsiyet ON mm.CINSIYET=enCinsiyet.DEGER 
                LEFT JOIN GNL_ENUM_DEGER enDurum ON mm.DURUM =enDurum.DEGER 
            WHERE enCinsiyet.TABLO ='MS_MUSTERI' AND enCinsiyet.KOLON='CINSIYET'
                AND enDurum.TABLO ='MS_MUSTERI' AND enDurum.KOLON ='DURUM'
                AND  ROWNUM <= 5
            """) 
    return data


@task
def insert_data_postgres(data):
    pg_hook= PostgresHook(postgres_conn_id='musteri_postgres_conn')
    data['YUKSEK_RISK_GRUBUNDA_MI'] = data['YUKSEK_RISK_GRUBUNDA_MI'].apply(lambda x: False if x == 0 else True)
  
    for index, row in data.iterrows():       
        insert_query = f"""
                insert into airflow_musteri (olusturma_tarihi, guncelleme_tarihi, p_musteri_id, ad, soyad, cinsiyet, dogum_tarihi, yuksek_risk_grubunda_mi, bank_hesap_adi, bank_hesap_no, yabanci_ad_unvan)
                values (
                 '{row['OLUSTURULMA_TARIHI']}',
                 '{row['GUNCELLEME_TARIHI']}',
                 '{row['ID']}',
                 '{row['AD']}',
                 '{row['SOYAD']}',
                 '{row['CINSIYET']}',
                 '{row['DOGUM_TARIH']}',
                 '{row['YUKSEK_RISK_GRUBUNDA_MI']}',
                 '{row['BANK_HESAP_ADI']}',
                 '{row['BANK_HESAP_NO']}',
                 '{row['YABANCI_AD_UNVAN']}'
                )
        """
        pg_hook.run(insert_query)        

default_args = {
    'owner': 'airflow',    
    'start_date': days_ago(1),
    'retries': 1,
}

with DAG(
    'a-some-fields-boolean-musteri-oracle-postgres',
    default_args=default_args,
    description='Oracle MS_MUSTERI tablosundan bazı alanları çeker, boolean alan için veri dönüşümü yapar, postgres airflow_musteri tablosuna ekler.',
    start_date= dt.datetime(2024,3,1),
    schedule_interval='*/5 * * * *'
    ) as dag:
        data = get_data_oracle()
        insert_data_postgres(data)
