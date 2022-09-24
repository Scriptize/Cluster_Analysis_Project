from connect import conn
import pandas as pd

df = pd.read_sql(
"""
SQL Goes Here
""", conn)
print(df)

conn.close()