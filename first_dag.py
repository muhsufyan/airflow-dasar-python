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
    default_args = default_param,
    start_date = datetime(2022, 7, 13, 2),
    schedule_interval="@daily"
) as dag:
    task1 = BashOperator(
        task_id = "first_task_v2",
        bash_command="echo hello world with BashOperator"
    )
    # buat task 2 yg operator nya adlh BashOperator
    task2 = BashOperator(
        task_id='task_2',
        bash_command="echo execute/running after task 1 complete, running bersamaan dg task3"
    )
    task3 = BashOperator(
        task_id="task_3",
        bash_command="echo execute/running after task 1 complete, running bersamaan dg task2"
    )
    # # run task (task dependencies cara 1)
    # # task2 & task3 running scra bersamaan after task1 finish
    # # cara 1
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)

    # # run task (task dependencies cara 2)
    # task1 >> task2
    # task1 >> task3

    # run task (task dependencies cara 3)
    task1 >> [task2, task3]
