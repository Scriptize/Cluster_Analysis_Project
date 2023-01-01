from connect import conn
import pandas as pd

from connect import conn
import pandas as pd

df = pd.read_sql(
"""
SELECT  * FROM Life_Expectancy 
""", conn) 

print(df)


conn.close()