from connect import conn
import pandas as pd

from connect import conn
import pandas as pd

df = pd.read_sql(
"""
SELECT  * FROM Life_Expectancy 
""", conn) 

# Define a custom function to sort the words in each cell
def alphabetize(s):
    return ' '.join(sorted(s.split()))

# Apply the custom function to the 'words' column
df['country'] = df['country'].apply(alphabetize)

# Convert all the data in the Year Columns from an object data type to a numeric data type
columns = ['1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016']
df[columns] = df[columns].apply(pd.to_numeric)

# Round values to the nearest tenth
df =df.round(decimals=1)

#creates subset of list between 1990 and 2016
df_subset = df.loc[:, '1990':'2016']

print(df_subset)


conn.close()