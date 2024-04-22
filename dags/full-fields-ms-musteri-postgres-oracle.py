import datetime as dt
from airflow import DAG
from airflow.providers.oracle.operators.oracle import OracleOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.generic_transfer import GenericTransfer
from airflow.utils.dates import days_ago
from airflow.utils.trigger_rule import TriggerRule


default_args = {
    'owner': 'airflow',    
    'start_date': days_ago(1),
    'retries': 1,
}

dag = DAG(
    'a-full-fields-ms-musteri-postgres-oracle',
    default_args=default_args,
    description='(Veri tipi dönüşümü gerektirdiğinden çalışmaz) Postgres airflow_ms_musteri tablosundaki alanların tamamını, oracle TEMP_AIRFLOW_MS_MUSTERI tablosuna ekler.',
    start_date= dt.datetime(2024,3,1),
    schedule_interval='*/5 * * * *'
)

truncate_musteri_main_test=OracleOperator(
    task_id='truncate_musteri_test',
    oracle_conn_id='pusula_conn',
    sql='truncate table TEMP_AIRFLOW_MS_MUSTERI',
    dag=dag
)

# Bu işlemde veri tipi uyumsuzluğu olmasından kaynaklı aktarım yapılamıyor.
insert_musteri_test = GenericTransfer(
    task_id='insert_musteri_test',
    source_conn_id='musteri_postgres_conn',
    sql='select * from airflow_ms_musteri',
    destination_conn_id='pusula_conn',
    destination_table='TEMP_AIRFLOW_MS_MUSTERI',
    dag=dag
)


truncate_musteri_main_test>>insert_musteri_test
