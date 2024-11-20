# Creating a DAG that runs a different sleep time
# Using this for chainging multiple DAGs to emulate a process

from time import sleep
from datetime import datetime
from random import randint
import time

import sys
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator


def admin_process_17():
    timer = randint(1, 600)
    for i in reversed(range(timer)):
        sys.stderr.write(f'\rsleeping for {i} seconds')
        sleep(1)

dag = DAG('admin_process_17', description='Admin Processing Step 17',
          schedule_interval='0 12 * * *',
          start_date=datetime(2017, 3, 20), catchup=False)

admin_process_17_operator = PythonOperator(task_id='admin_process_17_task', python_callable=admin_process_17, dag=dag)

admin_process_17_operator
