import pandas

initial = "1980/12/02"

date_list = initial.split("/")



new_date = "{}/{}/{}".format(date_list[2],date_list[1],date_list[0])

#print(new_date)


data = {
  "Date": ["1980-12-02", "1980-12-03","1980-12-04","1980-12-05"],
  "Open": [0.179688,0.177734,0.181641,0.175781],
  "High": [0.183594,0.177734,0.183594,0.175781],
  "Low": [0.1835940,.177734,0.183594,0.175781]
}
#print(data["Date"])
# Loop thru the dates
# Format the dates
# Change the dates to the correct format

def add(x,y):
    final = x + y
    
    return
new_list = []
initial = "1980/12/02"
date_list = initial.split("/")
new_date = "{}/{}/{}".format(date_list[2],date_list[1],date_list[0])

# Create a function that accepts a list as a parameter,loops through each date in the list, reformats it, and returns a new list

def transfer(x):
