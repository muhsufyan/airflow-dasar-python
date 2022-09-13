from datetime import datetime, timedelta
from airflow import DAG 
from airflow.operators.python_operator import PythonOperator
param = {
    "owner":"home",
    "retries":5,
    "retry_delay":timedelta(minutes=2)
}

def get_name(ti):
    # push multiple value melalui xcoms (publish data from xcom)
    ti.xcom_push(key="firstname", value="badut")
    ti.xcom_push(key="lastname", value="lucu")

def get_age(ti):
    ti.xcom_push(key="age", value=15)

def greet(ti):
    # (consume data from xcom)
    firstname = ti.xcom_pull(task_id="task_2", key="firstname")
    lastname = ti.xcom_pull(task_id="task_2", key="lastname")
    age = ti.xcom_pull(task_id="task_3", key="age")
    print(f"hallo world. My firstname {firstname} and lastname {lastname}, age {age}")

with DAG(
    default_args=param,
    dag_id="dag_v1",
    description="ini adalah dag dg python operator",
    start_date=datetime(2022, 9, 13),
    schedule_interval="@daily"
) as dag:
    task1 = PythonOperator(
        task_id="task_1",
        python_callable=greet,
    )
    task2 = PythonOperator(
        task_id="task_2",
        python_callable=get_name
    )
    task3 = PythonOperator(
        task_id="task_3",
        python_callable=get_age
    )
    # task dependencies. after finish task2 maka running/execute task1
    [task2, task3] >> task1