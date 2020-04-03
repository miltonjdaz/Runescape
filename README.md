# Runescape

I will be recording my drops from brutal black dragons and uploading the drops into GitHub. 

People can use the database for educational purposes. 

Upload the excel file into MySQL or any you prefer to write SQL queries of the drops. 


## Postgres Database commands needed
-- GRANT ALL PRIVILEGES ON DATABASE postgres TO airflow;
-- ALTER ROLE airflow WITH SUPERUSER;

## How to run this job
```bash
airflow webserver -p 8080
airflow scheduler

# optional CLI trigger or UI trigger
airflow trigger_dag runescape
```
## How to Force Kill airflow
In case Airflow is stagnant/still running, kill with following alias defined in my shell rc file
`# alias airflowkill="cat ~/airflow/airflow-webserver.pid | xargs kill"`
```bash
airflowkill
```

## How to confirm Airflow is Running/Not Running
```bash
ps aux | grep airflow
```
