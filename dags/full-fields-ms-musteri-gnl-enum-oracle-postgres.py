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
    'a-full-fields-ms-musteri-gnl-enum-oracle-postgres',
    default_args=default_args,
    description='Oracle MS_MUSTERI, GNL_ENUM_DEGER tablosundaki tüm alanları postgres airflow_ms_musteri, airflow_gnl_enum_deger tablosuna ekler.',
    start_date= dt.datetime(2024,3,1),
    schedule_interval=None,  # DAG'un otomatik tekrarlanmasını engeller
    catchup=False
)

truncate_musteri_main_test=PostgresOperator(
    task_id='truncate_musteri_test',
    postgres_conn_id='musteri_postgres_conn',
    sql="""
        truncate table airflow_ms_musteri;
        truncate table airflow_gnl_enum_deger;
        """,
    dag=dag
)

insert_musteri_test = GenericTransfer(
    task_id='insert_musteri_test',
    source_conn_id='pusula_conn',
    sql='select * from MS_MUSTERI',
    destination_conn_id='musteri_postgres_conn',
    destination_table='airflow_ms_musteri',   
    dag=dag
)


insert_gnl_enum_deger_test = GenericTransfer(
    task_id='insert_gnl_enum_deger_test',
    source_conn_id='pusula_conn',
    sql='select * from GNL_ENUM_DEGER',
    destination_conn_id='musteri_postgres_conn',
    destination_table='airflow_gnl_enum_deger',   
    dag=dag
)


truncate_musteri_main_test>>insert_musteri_test>>insert_gnl_enum_deger_test
