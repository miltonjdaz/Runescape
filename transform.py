import pandas as pd
from sqlalchemy import create_engine 
import os
import psycopg2

db_user = os.environ.get('DB_USER')
db_pw = os.environ.get('DB_PASS')

# example dialect+driver://username:password@host:port/database

engine = create_engine('postgresql://{login}:{pw}@localhost/postgres'.format(login=db_user, pw=db_pw))

query = pd.read_sql_query('SELECT COUNT(Dragon_bones) FROM rstable', engine)
print(query)
import ipdb; ipdb.set_trace()