from datetime import datetime, timedelta
from airflow.decorators import dag, task

default_param = {
    "owner":"abdi",
    "retries":5,
    'retry_delay':timedelta(minutes=5)
}


# define dag with decorator.
# and create func
@dag(dag_id="dag_1",
    default=default_param,
    start_date=datetime(2022, 9, 13),
    schedule_interval='@daily'
    )
def hello_world_etl():
    # ini didalam dag. kita akan dibuat 3 task with decorator. nama task akan == nama func
    @task()
    def get_name():
        return 'ujang'
    
    @task()
    def get_age():
        return 54
    
    @task()
    def greet(name, age):
        print(f"hello world, my name {name} and age {age}")
    # running, task dependencies. first run get_name & get_age pd 1 waktu yg sama
    # second after 2 func tsb finish lanjutkan ke greet
    name = get_name()
    age = get_age()
    greet = greet(name=name, age=age)

greet_dag = hello_world_etl()