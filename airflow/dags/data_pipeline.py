from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'data_continuum_pipeline',
    default_args=default_args,
    description='A simple data pipeline DAG for Data-Continuum',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=['continuum'],
) as dag:

    def verify_db_connections():
        print("Verifying connections to Postgres and MongoDB...")
        # In a real scenario, use Airflow Hooks/Connections here
        return True

    verify_task = PythonOperator(
        task_id='verify_connections',
        python_callable=verify_db_connections,
    )

    # A mock PySpark job for data cleaning and joining
    run_pyspark_job = BashOperator(
        task_id='run_pyspark_cleaning',
        bash_command='echo "Simulating PySpark spark-submit job to clean and join Postgres & Mongo data..." && sleep 5',
    )

    # Trigger ML Training Service
    trigger_ml_training = BashOperator(
        task_id='trigger_ml_training',
        bash_command='curl -X POST http://api:8001/train || echo "ML service not reachable from here"',
    )

    verify_task >> run_pyspark_job >> trigger_ml_training
