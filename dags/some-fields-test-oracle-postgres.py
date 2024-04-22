import datetime as dt
from airflow import DAG
from airflow.decorators import task
from airflow.providers.oracle.hooks.oracle import OracleHook
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.utils.dates import days_ago


@task
def get_data_oracle():
    oracle_hook= OracleHook(oracle_conn_id='pusula_conn')
    data = oracle_hook.get_pandas_df(sql="SELECT ADI, SOYADI FROM TEMP_AIRFLOW_TEST") 
    return data

@task
def insert_data_postgres(data):
    pg_hook= PostgresHook(postgres_conn_id='musteri_postgres_conn')
    pg_hook.insert_rows(table="airflow_test", rows=data.values.tolist(), target_fields=['adi','soyadi'])

default_args = {
    'owner': 'airflow',    
    'start_date': days_ago(1),
    'retries': 1,
}

with DAG(
    'a-some-fields-test-oracle-postgres',
    default_args=default_args,
    description='Oracle TEMP_AIRFLOW_TEST tablosundan veri çeker, postgres airflow_test tablosuna bazı alanlarını ekler.',
    start_date= dt.datetime(2024,3,1),
    schedule_interval='*/5 * * * *'
    ) as dag:        
        data = get_data_oracle()
        insert_data_postgres(data)
