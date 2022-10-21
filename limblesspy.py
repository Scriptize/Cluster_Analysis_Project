from connect import conn
import pandas as pd

df = pd.read_sql(
"""
SQL Goes Here
""", conn)
print(df)

conn.close()



#Welcome to your python file! Here is where you'll work on making your "puzzle piece"

#From top to bottom:
#1) The two lines up top are the imports; u need these to access the database!(Check out the connect.py file. It has our login info; its not in here for security puposes)
#2) Next is your bread and butter, should be familiar if you've taken a look at pandas. this line takes in a sql query as a string and converts it into a pandas dataframe. The next line prints it out so you have a good idea of what it looks like.
#3) Finally, we use conn.close() to log out of the database and disconnect.