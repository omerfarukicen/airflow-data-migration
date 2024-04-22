import datetime as dt
from airflow import DAG
from airflow.decorators import task
from airflow.providers.oracle.hooks.oracle import OracleHook
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.utils.dates import days_ago

@task
def get_data():
    postgres_hook= PostgresHook(postgres_conn_id='musteri_postgres_conn')
    data = postgres_hook.get_pandas_df(
         sql="""
              SELECT
                mm.AD ad,
              	mm.OLUSTURULMA_TARIHI olusturma_tarihi,
                mm.GUNCELLEME_TARIHI guncelleme_tarihi,
                mm.DOGUM_TARIH dogum_tarih
            FROM airflow_ms_musteri mm
            WHERE mm.DOGUM_TARIH is not null
            LIMIT 5
            """) 
    return data


@task
def insert_data(data):
    oracle_hook = OracleHook(oracle_conn_id='pusula_conn')
    data['olusturma_tarihi'] = data['olusturma_tarihi'].apply(lambda x: x.strftime('%Y-%m-%d %H:%M:%S'))
    data['guncelleme_tarihi'] = data['guncelleme_tarihi'].apply(lambda x: x.strftime('%Y-%m-%d %H:%M:%S'))
    data['dogum_tarih'] = data['dogum_tarih'].apply(lambda x: x.strftime('%Y-%m-%d'))
    
    for index, row in data.iterrows():
        insert_query = f"""
        INSERT INTO TEMP_AIRFLOW_MS_MUSTERI (
            OLUSTURULMA_TARIHI,
            GUNCELLEME_TARIHI,
            DOGUM_TARIH,
            AD
        )VALUES (
            TO_DATE('{row['olusturma_tarihi']}', 'YYYY-MM-DD HH24:MI:SS'), 
            TO_DATE('{row['guncelleme_tarihi']}', 'YYYY-MM-DD HH24:MI:SS'), 
            TO_DATE('{row['dogum_tarih']}', 'YYYY-MM-DD'), 
            '{row['ad']}')
        """        
        oracle_hook.run(insert_query)


default_args = {
    'owner': 'airflow',    
    'start_date': days_ago(1),
    'retries': 1,
}

with DAG(
    'a-fields-date-timestamp-postgres-oracle',
    default_args=default_args,
    description='Postgres airflow_ms_musteritablosundaki tarih alanlarını modify yapılarak, oracle TEMP_AIRFLOW_MS_MUSTERI ekler.',
    start_date= dt.datetime(2024,3,1),
    schedule_interval='*/5 * * * *'
    ) as dag:
        data = get_data()        
        insert_data(data)
