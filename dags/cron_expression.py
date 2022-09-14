from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_param = {
    'owner': 'test',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    default_args = default_param,
    dag_id = "dag_with_cron_expression",
    start_date = datetime(2022, 9, 10),
    # run setiap hari jumat jam 23
    schedule_interval = '0 23 * * 5',
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command="echo dag with cron expression!"
    )
    task1