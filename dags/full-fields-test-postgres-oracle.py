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
    'a-full-fields-test-postgres-oracle',
    default_args=default_args,
    description='Postgres airflow_testtablosundaki alanları Oracle TEMP_AIRFLOW_TEST tablosuna alan sırasına göre ekler.',
    start_date= dt.datetime(2024,3,1),
    schedule_interval='*/5 * * * *'
)

truncate_main_test=OracleOperator(
    task_id='truncate_test',
    oracle_conn_id='pusula_conn',
    sql='truncate table TEMP_AIRFLOW_TEST',
    dag=dag
)

insert_test = GenericTransfer(
    task_id='insert_test',
    source_conn_id='musteri_postgres_conn',
    sql='select id, adi, soyadi from airflow_test',
    destination_conn_id='pusula_conn',
    destination_table='TEMP_AIRFLOW_TEST',   
    dag=dag
)


truncate_main_test>>insert_test
