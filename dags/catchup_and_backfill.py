from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_param = {
    "owner":"desktip",
    'retries':5,
    'retry_delay':timedelta(minutes=2)
}
# create simple dag
with DAG(
    dag_id="catchup_and_backfill_v1",
    default_args=default_param,
    start_date=datetime(2022, 9, 20),
    schedule_interval='@daily',
    # by default catchup is True (sehingga scheduler akan mengeksekusi dag mulai dr waktu start (20-09-2022) sampai dg hari ini (current time))
    # sedangkan jika False maka scheduler akan mengeksekusi dag satu kali saja
    # untuk lebih jelasnya & mengetahui perbedaan antara catchup dengan backfill maka catchup dibawah ini ubah jd False
    catchup=True
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command='echo simple dag'
    )
    task1