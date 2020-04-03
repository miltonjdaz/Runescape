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
STEP 0
1. Manual Data Creation and recording

STEP 1
1. create S3 bucket through browser
    aws[s3]
2. create airflow IAM user
3. get AWS Credentials into ~/.aws/credentials
    bash, aws-cli
4. change xlsx file to csv

to get started/better at airflow:
    * copy tutorial and edit to fit following job
    * read docs: 
        all of `tutorial`, 
        quick start, 
        tutorial, 
        how-to guides: bashOperator, 
        Concepts: all of `Core Ideas`
        Command Line Interface Reference: list_dags

to get familiar with aws cli:
    look up documentation on aws cli s3 sub-commands:
        https://docs.aws.amazon.com/cli/latest/reference/s3/
        https://docs.aws.amazon.com/cli/latest/reference/s3/sync.html

5. Write an airflow job with single bash operator executing:
    optional test command:
    `aws s3 ls >> /home/milton/github/Runescape/test.txt`
    
    final bash code should look something like this:
    `aws s3 sync /home/milton/gitub/Runescape/*.csv s3://bucketname/data/filename.csv`
    aws-cli, airflow, bash


STEP 2
4. Create redshift database through browser
    aws[redshift]
5. Add to airflow job: data load from s3 csv to redshift
    airflow, sql
6. Add to airflow job: Metrics, Analysis, Averages/counts whatnot
    sql, python, whatever you want
