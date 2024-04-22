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
                mm.AD ad,
                enCinsiyet.ACIKLAMA cinsiyet               
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
    pg_hook.insert_rows(table="airflow_musteri", rows=data.values.tolist(),  target_fields=['ad','cinsiyet'])

default_args = {
    'owner': 'airflow',    
    'start_date': days_ago(1),
    'retries': 1,
}

with DAG(
    'a-fields-enum-airflow-musteri-oracle-postgres',
    default_args=default_args,
    description='Oracle MS_MUSTERI tablosundaki enum değeri içeren alan ile postgres airflow_musteri tablosuna ekler.',
    start_date= dt.datetime(2024,3,1),
    schedule_interval='*/5 * * * *'
    ) as dag:
        data = get_data_oracle()
        insert_data_postgres(data)
