import pandas as pd
from sqlalchemy import create_engine
import os

db_user = os.environ.get('DB_USER')
db_pw = os.environ.get('DB_PASS')

# example dialect+driver://username:password@host:port/database

engine = create_engine('postgresql+psycopg2://{login}:{pass}@localhost/postgres'.format(login=db_user, pass=db_pw))

