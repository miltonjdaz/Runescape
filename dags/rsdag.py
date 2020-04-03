from datetime import timedelta

from airflow import DAG

from airflow.operators.bash_operator import BashOperator
from airflow.operators.postgres_operator import PostgresOperator
from airflow.utils.dates import days_ago

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
    default_args = default_args,
    description = 'A brutal black dragon drops DAG',
    schedule_interval = timedelta(days=1),
)

# Setting variables and connections
POSTGRES_CONN_ID = 'pgdb'

# t1
t1 = BashOperator(
    task_id = 'upload_to_s3',
    bash_command = 'aws s3 sync /home/milton/gitub/Runescape/drops.csv s3://runescape-bucket/data/drops.csv',
    dag = dag
)

# t2 
t2 = BashOperator(
    task_id = 'download csv data',
    bash_command = 'aws s3 cp s3://runescape-bucket/data/drops.csv /home/milton/gitub/Runescape/drops2.csv', 
    dag = dag
)
sql_cmds = []
sql_cmds.append("""
    CREATE TABLE rstable
        (
        'Date' DATE,
        'Dragon Bones' INT,
        'Black dragonhide' INT,
        'Dragon platelegs' INT,
        'Dragon plateskirt' INT,
        'Dragon spear' INT,
        'Uncut dragonstone' INT,
        'Rune hasta' INT,
        'Rune spear' INT,	
        'Rune platelegs' INT,	
        'Rune full helm' INT,	
        'Rune dart' INT,	
        'Rune longsword' INT,	
        'Black d’hide body' INT,	
        'Rune knife' INT,	
        'Rune thrownaxe' INT,	
        'Black d’hide vamb' INT,	
        'Rune platebody' INT,	
        'Dragon med helm' INT,	
        'Dragon longsword' INT,	
        'Dragon dagger' INT,
        'Rune javelin' INT,	
        'Blood rune' INT,	
        'Soul rune' INT,	
        'Death rune' INT,	
        'Law rune' INT,
        'Rune arrow' INT,	
        'Lava scale' INT,	
        'Dragon dart tip' INT,	
        'Runite ore' INT,	
        'Dragon arrowtips' INT,	
        'Dragon javelin heads' INT,	
        'Coins' INT,	
        'Anglerfish' INT,	
        'Uncut sapphire' INT,	
        'Uncut emerald' INT,	
        'Loop half of key' INT,	
        'Tooth half of key' INT,	
        'Uncut ruby' INT,	
        'Runite bar' INT,	
        'Nature talisman' INT,	
        'Uncut diamond' INT,	
        'Nature rune' INT,	
        'Rune 2h sword' INT,	
        'Rune battleaxe' INT,	
        'Steel arrow' INT,	
        'Adamant javelin' INT,	
        'Rune sq shield' INT,	
        'Dragonstone' INT,	
        'Silver ore' INT,	
        'Rune kiteshield' INT,	
        'Shield left half' INT,	
        'Dragon spear' INT,	
        'Ensouled dragon head' INT,	
        'Clue scroll (hard)' INT,	
        'Clue scroll (elite)' INT,
        'Draconic visage' INT,	
        'Ancient shard' INT,	
        'Dark totem base' INT,	
        'Dark totem middle' INT,	
        'Dark totem top' INT);
    """)

sql_cmds.append("""
    COPY rstable 
    FROM '/home/milton/gitub/Runescape/drops2.csv'
    DELIMITER ',' CSV HEADER;
    """ 
    )

t3 = PostgresOperator(
    task_id='rs_drops_report',
    sql=create_rs_table,
    postgres_conn_id=POSTGRES_CONN_ID,
    dag=dag
)

t1 >> t2 >> t3
