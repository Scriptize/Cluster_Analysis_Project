from connect import conn
import pandas as pd

df = pd.read_sql(
"""
SELECT * FROM Test_Table


""", conn)
print(df)

conn.close()