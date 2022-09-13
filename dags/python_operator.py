from datetime import datetime, timedelta
from airflow import DAG 
from airflow.operators.python_operator import PythonOperator
param = {
    "owner":"home",
    "retries":5,
    "retry_delay":timedelta(minutes=2)
}


# func ini akan running oleh dag task operator pythonOperator
# func ini akan share information berupa name ke func lainnya dimana task dr funcnya berbeda (ex task 1 adlh func yg menerima info name dari func get_name sedangkan get_name itu ada di task2 & task 2 akan share information of name)
# the name value from get_name share to greet with different task
def get_name():
    return 'badut'

# kita pull nama badut (from return func get_name) ke func greet menggunakan xcom_pull
# func ini akan running oleh dag task operator pythonOperator
def greet(age, nameFrom_get_name):
    # get name from task2 (the value from func get_name)
    name = nameFrom_get_name.xcom_pull(task_id="task_2")
    print(f"hallo world. My name {name}, age {age}")
with DAG(
    default_args=param,
    dag_id="dag_v1",
    description="ini adalah dag dg python operator",
    start_date=datetime(2022, 9, 13),
    schedule_interval="@daily"
) as dag:
    task1 = PythonOperator(
        task_id="task_1",
        # passing the func as param & run it
        python_callable=greet,
        # pass as param the func greet
        op_kwargs={"age":32}
    )
    task2 = PythonOperator(
        task_id="task_2",
        python_callable=get_name
    )
    # task dependencies. after finish task2 maka running/execute task1
    task2 >> task1