import airflow
from airflow.operators.bash_operator import BashOperator
from airflow.models import DAG
import os

args = {
    'owner': 'airflow',
    'start_date': airflow.utils.dates.days_ago(2)
}

dag = DAG(
    dag_id='example_bash_operator',
    default_args=args,
    schedule_interval=None
)

op = BashOperator(
    task_id = 'task_id',
    bash_command = 'echo Hello people!',
    dag = dag
)
