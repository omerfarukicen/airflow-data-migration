from airflow import DAG
import datetime as dt
from airflow.providers.oracle.operators.oracle import OracleOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',    
    'start_date': days_ago(1),
    'retries': 1,
    'depends_on_past': False  # Görevlerin geçmiş duruma bağlı olarak tekrar çalışmasını önler
}

dag = DAG(
    'a-create-oracle-temp-airflow-test',
    default_args=default_args,
    description='Oracle üzerinde temp_airflow_test tablosunu oluşturur.',
    schedule_interval=None,  # DAG'un otomatik tekrarlanmasını engeller
    catchup=False
)

create_table_task=OracleOperator(
    task_id='create_table_task',
    sql='sql/oracle/create-airflow-test.sql',
    oracle_conn_id='pusula_conn',
    dag=dag
)

create_table_task