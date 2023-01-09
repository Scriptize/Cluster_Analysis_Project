import pandas
from pprint import pprint

initial = "1980/12/02"

date_list = initial.split("/")

new_date = "{}/{}/{}".format(date_list[2],date_list[1],date_list[0])


data = {
  "Date": ["1980/12/02", "1980/12/03","1980/12/04","1980/12/05"],
  "Open":[0.179688,0.177734,0.181641,0.175781],
  "High": [0.183594,0.177734,0.183594,0.175781],
  "Low": [0.1835940,.177734,0.183594,0.175781]
}

#Make a function that takes in a list as a parameter and reformats the dates in the list and returns the reformatted dates


def reformater(dates):
  final=[] #initialize final list
  for x in dates: #loop thru date list
    split_date = x.split("/") # split each date by the slash
    new_date = "{}/{}/{}".format(split_date[2],split_date[1],split_date[0]) # reformat the date
    final.append(new_date) # add the new date to the final list
  return final



data["Date"] = reformater(data["Date"]) # reformats the values in the list value of the Date key

pprint(data)