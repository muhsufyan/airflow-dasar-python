from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator
# dict for arg
default_param = {
    # owner dr dag
    "owner":"sufyan",
    # waktu maksimum untuk mencoba lagi (retries) sebanyak 5 kali
    "retries": 5,
    # retry delay untuk setiap kali retry adlh 2 menit
    "retry_delay": timedelta(minutes=2)
}
# instance dag dg with statement
with DAG(
    # parameter
    dag_id = "first_dag",
    describe = "ini adalah deskripsi(metadata/info tambahan) dari dag pertama kita",
     # untuk arg/param umumnya kita buat dulu dlm dict baru dimasukkan kesini
    default_args = default_param,
    # kita tentukan pertama kali apa yg akan dilakukan oleh dag first_dag ini & sbrapa sering kita akan mengeksekusinya
    # pertama dag akan start dr 13 september 2022 dan run setiap hari pd jam 2pm
    start_date = datetime(2022, 7, 13, 2),
    schedule_interval="@daily"
) as dag:
    # kode ini dlm scope instance dag
    # kita buat simple dag menggunakan BashOperator (untuk mengeksekusi perintah bash).
    # task yg akan dilakukan adlh print out tulisan hello world with BashOperator
    task1 = BashOperator(
        task_id = "first_task_v2",
        bash_command="echo hello world with BashOperator"
    )
    # buat task 2 yg operator nya adlh BashOperator
    task2 = BashOperator(
        task_id='task_2',
        bash_command="i am execute/running after task 1 complete"
    )
    # run task (task dependencies)
    # task2 running after task1 finish
    task1.set_downstream(task2)
