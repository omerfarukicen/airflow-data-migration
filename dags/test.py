import datetime as dt
from airflow import DAG
from airflow.providers.oracle.operators.oracle import OracleOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.generic_transfer import GenericTransfer
from airflow.utils.dates import days_ago
from airflow.utils.trigger_rule import TriggerRule
from airflow.operators.python import PythonOperator
from airflow.decorators import task
from airflow.providers.oracle.hooks.oracle import OracleHook
from airflow.providers.postgres.hooks.postgres import PostgresHook
import uuid
import logging
from datetime import timedelta
default_args = {
    'owner': 'airflow',    
    'start_date': days_ago(1),
  #  'retries': 2,
  #  'retry_delay': timedelta(minutes=1),
  #  'retry_exponential_backoff': True,
  #  'max_retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'data-pipeline-flag',
    default_args=default_args,
    start_date= dt.datetime(2024,3,1),
    schedule_interval='*/15 * * * *',
    catchup=False
)

def get_last_update_date_airflow():
    pg_hook = PostgresHook(postgres_conn_id='musteri_postgres_staging')
    data = pg_hook.get_pandas_df(sql="select max(start_time) son_guncellenme_tarihi from airflow_task_management where task='MUSTERI_AKTARIM'") 
    son_guncellenme_tarihi = str(data.iloc[0]['son_guncellenme_tarihi'])
    logging.info("AIRFLOW SON ÇALIŞMA ZAMANI: "+son_guncellenme_tarihi)
    return son_guncellenme_tarihi

son_guncellenme_tarihi =get_last_update_date_airflow()

def transfer_records(**kwargs):
    logging.info('SON GÜNCELLEME:'+son_guncellenme_tarihi)
    oracle_hook= OracleHook(oracle_conn_id='pusula_betadb_conn')
    data = oracle_hook.get_pandas_df(
        sql=f"""
            SELECT COUNT(*)
            FROM MS_MUSTERI_TEST mm
            WHERE AKTARIM = 0 
              AND OLUSTURULMA_TARIHI BETWEEN TO_TIMESTAMP('{son_guncellenme_tarihi}', 'YYYY-MM-DD HH24:MI:SS.FF') AND SYSTIMESTAMP
        """
    )
    record_count = data.iloc[0, 0] 
    if record_count > 0:
        print("Record Sayısı Fazla: " + str(record_count))  # record_count'i string'e dönüştür
        logging.info("Record Sayısı Fazla: " + str(record_count))
        pass
    else:
        print("Aktarılacak kayıt bulunamadı.")


transfer_records_task = PythonOperator(
    task_id='transfer_records',
    python_callable=transfer_records,
    dag=dag
)
# Bağımlılıkları belirt
transfer_records_task