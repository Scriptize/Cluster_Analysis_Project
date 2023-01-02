from connect import conn
import pandas as pd

df = pd.read_sql(
"""
SQL Goes Here
""", conn)

print(df)

conn.close()






# We have data from 1980 - 2020
# We only want data from 1990 - 2018

# We want to get data for the days in a month in a year
# We want to average out the data for days in a month
# We want to take those averages and find the overall average for each year from 1990 - 2018


