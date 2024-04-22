from airflow import DAG
import datetime as dt
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',    
    'start_date': days_ago(1),
    'retries': 1,
    'depends_on_past': False  # Görevlerin geçmiş duruma bağlı olarak tekrar çalışmasını önler
}

dag = DAG(
    'a-create-postgres-gnl-enum-deger',
    description='Postgres üzerinde gnl_enum_deger tablosunu oluşturur.',
    default_args=default_args,
    schedule_interval=None,  # DAG'un otomatik tekrarlanmasını engeller
    catchup=False
)

create_enum_type_task = PostgresOperator(
        task_id='create-gnl-enum-deger_task',
        sql='sql/postgres/create-gnl-enum-deger.sql',
        postgres_conn_id='musteri_postgres_conn',
        dag=dag
)

create_enum_type_task