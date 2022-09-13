from datetime import datetime, timedelta
from airflow import DAG 
from airflow.operators.python_operator import PythonOperator
param = {
    "owner":"home",
    "retries":5,
    "retry_delay":timedelta(minutes=2)
}

# func ini akan running oleh dag
def greet(name, age):
    print(f"hallo world. My name {name}, age {age}")
with DAG(
    default_args=param,
    dag_id="dag_v1",
    description="ini adalah dag dg python operator",
    start_date=datetime(2022, 9,13),
    schedule_interval="@daily"
) as dag:
    task1 = PythonOperator(
        task_id="task_1",
        # passing the func as param & run it
        python_callable=greet
        # pass as param the func greet
        op_kwargs={"name":"udin","age":32}
    )
    # task dependencies
    task1