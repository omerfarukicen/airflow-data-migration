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
    'test_data_transfer',
    default_args=default_args,
    start_date= dt.datetime(2024,3,1),
    schedule_interval='*/5 * * * *'
)


truncate_musteri_main_test=PostgresOperator(
    task_id='truncate_musteri_test',
    postgres_conn_id='musteri_postgres_conn',
    sql='truncate table musteri',
    dag=dag
)


insert_musteri_test = GenericTransfer(
    task_id='insert_musteri_test',
    source_conn_id='pusula_conn',
    sql='select * from Musteri',
    destination_conn_id='musteri_postgres_conn',
    destination_table='musteri',   
    dag=dag
)

truncate_musteri_main_test>>insert_musteri_test
