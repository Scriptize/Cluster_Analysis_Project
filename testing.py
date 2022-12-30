from connect import conn
import pandas as pd

df = pd.read_sql(
"""
SELECT * FROM GDP_GLOBAL
""", conn)

# Convert all the data in the Year Columns from an object data type to a numeric data type
columns = ['1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
df[columns] = df[columns].apply(pd.to_numeric)

# Round all the values in the DataFrame to the nearest thousandths
df = df.round(decimals=3)

# Remove the "Country Code" from the Data Frame
df = df.drop('Country Code', axis=1)

print(df)

dataframe2 = 

conn.close()

#Welcome to your python file! Here is where you'll work on making your "puzzle piece"

#From top to bottom:
#1) The two lines up top are the imports; u need these to access the database!(Check out the connect.py file. It has our login info; its not in here for security puposes)
#2) Next is your bread and butter, should be familiar if you've taken a look at pandas. this line takes in a sql query as a string and converts it into a pandas dataframe. The next line prints it out so you have a good idea of what it looks like.
#3) Finally, we use conn.close() to log out of the database and disconnect.