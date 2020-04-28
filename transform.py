import pandas as pd
from sqlalchemy import create_engine 
import os
import psycopg2

db_user = os.environ.get('DB_USER')
db_pw = os.environ.get('DB_PASS')

# example dialect+driver://username:password@host:port/database

engine = create_engine('postgresql://{login}:{pw}@localhost/postgres'.format(login=db_user, pw=db_pw))

query_one = pd.read_sql_query('SELECT COUNT(Dragon_bones) AS Dragon_bones, Day FROM rstable GROUP BY Day ORDER BY Day', engine)
print(query_one)

df1 = pd.DataFrame(query_one) 
  
# saving the dataframe 
df1.to_csv('/home/milton/github/Runescape/results/results_q1.csv') 

query_two = pd.read_sql_query('SELECT COUNT(Rune_hasta) AS Rune_hasta, Day FROM rstable GROUP BY Day ORDER BY Day', engine)
print(query_two)

df2 = pd.DataFrame(query_two) 
  
# saving the dataframe 
df2.to_csv('/home/milton/github/Runescape/results/results_q2.csv') 

query_three = pd.read_sql_query('SELECT COUNT(Blood_rune) AS Blood_rune, Day FROM rstable GROUP BY Day ORDER BY Day', engine)
print(query_three)

df3 = pd.DataFrame(query_three) 
  
# saving the dataframe 
df3.to_csv('/home/milton/github/Runescape/results/results_q3.csv') 

query_four = pd.read_sql_query('SELECT COUNT(Dragon_platelegs) AS Dragon_platelegs, Day FROM rstable GROUP BY Day ORDER BY Day', engine)
print(query_four)

df4 = pd.DataFrame(query_four) 
  
# saving the dataframe 
df4.to_csv('/home/milton/github/Runescape/results/results_q4.csv') 

# '/home/milton/github/Runescape/Results.csv'

import ipdb; ipdb.set_trace()