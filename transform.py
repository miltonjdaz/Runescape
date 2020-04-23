import pandas as pd
from sqlalchemy import create_engine 
import os
import psycopg2

db_user = os.environ.get('DB_USER')
db_pw = os.environ.get('DB_PASS')

# example dialect+driver://username:password@host:port/database

engine = create_engine('postgresql://{login}:{pw}@localhost/postgres'.format(login=db_user, pw=db_pw))

query_one = pd.read_sql_query('SELECT COUNT(Dragon_bones), Day FROM rstable GROUP BY Day ORDER BY Day', engine)
print(query_one)

query_two = pd.read_sql_query('SELECT COUNT(Rune_hasta), Day FROM rstable GROUP BY Day ORDER BY Day', engine)
print(query_two)

query_three = pd.read_sql_query('SELECT AVG(Rune_Hasta), Day FROM rstable GROUP BY Day ORDER BY Day', engine)
print(query_three)

query_four = pd.read_sql_query('SELECT COUNT(Clue_scroll_hard), Day FROM rstable GROUP BY Day ORDER BY Day', engine)
print(query_four)

query_five = pd.read_sql_query('SELECT AVG(Clue_scroll_hard), Day FROM rstable GROUP BY Day ORDER BY Day', engine)
print(query_five)

import ipdb; ipdb.set_trace()