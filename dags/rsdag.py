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
upload = BashOperator(
    task_id = 'upload_to_s3',
    bash_command = 'aws s3 cp /home/milton/github/Runescape/drops.csv s3://runescape-bucket/data/drops.csv',
    dag = dag
)

# t2 
download = BashOperator(
    task_id = 'download_from_s3',
    bash_command = 'aws s3 cp s3://runescape-bucket/data/drops.csv /home/milton/github/Runescape/drops2.csv', 
    dag = dag
)
sql_cmds = []

sql_cmds.append("""
    DROP TABLE IF EXISTS rstable;
    """
    )

sql_cmds.append("""
    CREATE TABLE rstable
        (
        Day DATE,
        Dragon_Bones INT,
        Black_dragonhide INT,
        Dragon_platelegs INT,
        Dragon_plateskirt INT,
        Dragon_spear INT,
        Uncut_dragonstone INT,
        Rune_hasta INT,
        Rune_spear INT,	
        Rune_platelegs INT,	
        Rune_full_helm INT,	
        Rune_dart INT,	
        Rune_longsword INT,	
        Black_dhide_body INT,	
        Rune_knife INT,	
        Rune_thrownaxe INT,	
        Black_dhide_vamb INT,	
        Rune_platebody INT,	
        Dragon_med_helm INT,	
        Dragon_longsword INT,	
        Dragon_dagger INT,
        Rune_javelin INT,	
        Blood_rune INT,	
        Soul_rune INT,	
        Death_rune INT,	
        Law_rune INT,
        Rune_arrow INT,	
        Lava_scale INT,	
        Dragon_dart_tip INT,	
        Runite_ore INT,	
        Dragon_arrowtips INT,	
        Dragon_javelin_heads INT,	
        Coins INT,	
        Anglerfish INT,	
        Uncut_sapphire INT,	
        Uncut_emerald INT,	
        Loop_half_of_key INT,	
        Tooth_half_of_key INT,	
        Uncut_ruby INT,	
        Runite_bar INT,	
        Nature_talisman INT,	
        Uncut_diamond INT,	
        Nature_rune INT,	
        Rune_2h_sword INT,	
        Rune_battleaxe INT,	
        Steel_arrow INT,	
        Adamant_javelin INT,	
        Rune_sq_shield INT,	
        Dragonstone INT,	
        Silver_ore INT,	
        Rune_kiteshield INT,	
        Shield_left_half INT,	
        Ensouled_dragon_head INT,	
        Clue_scroll_hard INT,	
        Clue_scroll_elite INT,
        Draconic_visage INT,	
        Ancient_shard INT,	
        Dark_totem_base INT,	
        Dark_totem_middle INT,	
        Dark_totem_top INT);
    """)

sql_cmds.append("""
    COPY rstable 
    FROM '/home/milton/github/Runescape/drops2.csv'
    DELIMITER ',' CSV HEADER;
    """ 
    )

rs_drops_report = PostgresOperator(
    task_id='rs_drops_report',
    sql=sql_cmds,
    postgres_conn_id=POSTGRES_CONN_ID,
    dag=dag
)
# import ipdb; ipdb.set_trace()
upload >> download  >> rs_drops_report
