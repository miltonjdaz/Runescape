import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("/home/milton/github/Runescape/data/drops2.csv")
df.info()
df.head()

