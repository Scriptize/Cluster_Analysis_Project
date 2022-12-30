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
df_new = df.drop('Country Code', axis=1)

#Prints DataFrame that excludes Country Code
print(df_new)

# Prints DataFrame that includes Country Code
print(df)

conn.close()
