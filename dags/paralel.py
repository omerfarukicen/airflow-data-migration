from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
import datetime as dt
default_args = {
    'owner': 'airflow',    
    'start_date': days_ago(1),
    'retries': 1
}
def process(p1):
    print(p1)
    return 'done'

with DAG(dag_id='parallel_dag', schedule_interval='0 0 * * *', default_args=default_args, catchup=False) as dag:
    
    tasks = [BashOperator(task_id='task_{0}'.format(t), bash_command='sleep 5'.format(t)) for t in range(1, 4)]

    task_4 = PythonOperator(task_id='task_4', python_callable=process, op_args=['my super parameter'])

    task_5 = BashOperator(task_id='task_5', bash_command='echo "pipeline done"')

    tasks >> task_4 >> task_5
        