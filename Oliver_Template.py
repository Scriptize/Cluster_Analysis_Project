from connect import conn
import pandas as pd

df = pd.read_sql(
    """
  SELECT Year, FedMinWage, HouseParty, SenParty, PresParty
    FROM US_Min_Wage
      WHERE Year > 1997 and Year < 2019

""", conn)


numHouse = 0
df["Rep Control"] = 0
df["Dem Control"] = 0


df.loc[df['HouseParty'] == "Republican", "Rep Control"] += 33.33333333
df.loc[df['SenParty'] == "Republican", "Rep Control"] += 33.33333333
df.loc[df['PresParty'] == "Republican", "Rep Control"] += 33.33333333

df.loc[df['HouseParty'] == "Democrat", "Dem Control"] += 33.33333333
df.loc[df['SenParty'] == "Democrat", "Dem Control"] += 33.33333333
df.loc[df['PresParty'] == "Democrat", "Dem Control"] += 33.33333333


df_rounded = df.round()
print(df_rounded)

conn.close()

# Welcome to your python file! Here is where you'll work on making your "puzzle piece"

# From top to bottom:
# 1) The two lines up top are the imports; u need these to access the database!(Check out the connect.py file. It has our login info; its not in here for security puposes)
# 2) Next is your bread and butter, should be familiar if you've taken a look at pandas. this line takes in a sql query as a string and converts it into a pandas dataframe. The next line prints it out so you have a good idea of what it looks like.
# 3) Finally, we use conn.close() to log out of the database and disconnect.
