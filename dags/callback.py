from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
import logging
def on_success_callback(dict):
    logging.info("on_success_dag callback function executed.")
    logging.info(dict)
    print("on_success_dag")
    print(dict)

def on_failure_callback(dict):
    print("on_failure_callback")
    print(dict)

default_args = {
    'owner': 'Airflow',
    'start_date': datetime(2024, 3, 1),
    'retries':3,
    'retry_delay':timedelta(seconds=60),
    'on_success_callback': on_success_callback,
    'on_failure_callback': on_failure_callback
}


dag = DAG(
    'dag_call_back',
    default_args=default_args,
    schedule_interval='*/1 * * * *',
    catchup=False,
  
)

# Define the tasks
with dag:
    # Task 1
    bash_task_1 = BashOperator(task_id='bash_task_1', bash_command="echo 'first task'")

    # Task 2
    bash_task_2 = BashOperator(task_id='bash_task_2', bash_command="echo 'second task'")

    # Set the task sequence
    bash_task_1 >> bash_task_2
