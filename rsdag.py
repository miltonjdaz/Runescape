from datetime import timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to operate!
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    
}
dag = DAG(
    'runescape',
    default_args=default_args,
    description='A brutal black dragon drops DAG',
    schedule_interval=timedelta(days=1),
)

# t1
t1 = BashOperator(
    task_id='upload_to_s3',
    bash_command='aws s3 sync /home/milton/gitub/Runescape/drops.csv s3://runescape-bucket/data/drops.csv',
    dag=dag
)

# t2 
t2 = BashOperator(
    task_id='download csv data',
    bash_command='aws s3 cp s3://runescape-bucket/data/drops.csv /home/milton/gitub/Runescape/drops2.csv', 
    dag=dag
)