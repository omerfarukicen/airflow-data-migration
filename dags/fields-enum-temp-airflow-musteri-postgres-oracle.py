import datetime as dt
from airflow import DAG
from airflow.decorators import task
from airflow.providers.oracle.hooks.oracle import OracleHook
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.utils.dates import days_ago


@task
def get_data():
    postgres_hook= PostgresHook(postgres_conn_id='musteri_postgres_conn')
    data = postgres_hook.get_pandas_df(
         sql="""
                SELECT
                    mm.ID,
                    mm.ad,
                    enCinsiyet.deger AS cinsiyet
                FROM airflow_musteri mm
                    LEFT JOIN airflow_gnl_enum_deger enCinsiyet ON mm.cinsiyet::text = enCinsiyet.aciklama
                WHERE enCinsiyet.tablo = 'MS_MUSTERI'  AND enCinsiyet.kolon = 'CINSIYET'
            """)
    return data


@task
def insert_data(data):
    oracle_hook= OracleHook(oracle_conn_id='pusula_conn')
    oracle_hook.insert_rows(table="TEMP_AIRFLOW_MS_MUSTERI", rows=data.values.tolist(), target_fields=['ID','AD','CINSIYET'])

default_args = {
    'owner': 'airflow',    
    'start_date': days_ago(1),
    'retries': 1,
}

with DAG(
    'a-fields-enum-temp-airflow-musteri-postgres-oracle',
    default_args=default_args,
    description='Postgres MS_MUSTERI tablosundaki enum değeri içeren alan ile oracle TEMP_AIRFLOW_MS_MUSTERI tablosuna ekler.',
    start_date= dt.datetime(2024,3,1),
    schedule_interval='*/5 * * * *'
    ) as dag:
        data = get_data()
        insert_data(data)
