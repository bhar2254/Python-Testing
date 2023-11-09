#   Walkthrough with W3 Python Pandas Tutorial 
#       https://www.w3schools.com/python/pandas/

#   Ames housing data accessible at https://www.kaggle.com/datasets/marcopale/housing/
#       Data described by De Cock (2011) where 82 fields were recored for 2930 properties in Ames IA.

#   Collected by Blaine Harper
#       11/09/23

#   Table of Contents               Links to W3 Schools Tutorials
#       Basics              Completed
#           1. Introduction            https://www.w3schools.com/python/pandas/pandas_intro.asp
#           2. Getting Started         https://www.w3schools.com/python/pandas/pandas_getting_started.asp
#           3. Pandas Series           https://www.w3schools.com/python/pandas/pandas_series.asp
#           4. DataFrames              https://www.w3schools.com/python/pandas/pandas_dataframes.asp
#           5. Read CSV                https://www.w3schools.com/python/pandas/pandas_csv.asp
#           6. Read JSON               https://www.w3schools.com/python/pandas/pandas_json.asp
#           7. Analyze Data            https://www.w3schools.com/python/pandas/pandas_analyzing.asp
#       Cleaning Data       WIP
#           8. Clean Data              https://www.w3schools.com/python/pandas/pandas_cleaning.asp
#           9. Clean Empty Cells       https://www.w3schools.com/python/pandas/pandas_cleaning_empty_cells.asp
#           10. Clean Wrong Format      https://www.w3schools.com/python/pandas/pandas_cleaning_wrong_format.asp
#           11. Clean Wrong Data        https://www.w3schools.com/python/pandas/pandas_cleaning_wrong_data.asp
#           12. Remove Duplicates       https://www.w3schools.com/python/pandas/pandas_cleaning_duplicates.asp
#       Advanced            WIP
#           13. Correlations            https://www.w3schools.com/python/pandas/pandas_correlations.asp
#           14. Plotting                https://www.w3schools.com/python/pandas/pandas_plotting.asp
#           
#           

#   import pandas
import pandas as pd #   import pandas using an alias

#   debugging log bools
print_danger = False
print_debugging = True

#   check package version
if(print_debugging):
    print('Pandas version: ' + pd.__version__)

print("3. Series")
#   https://www.w3schools.com/python/pandas/pandas_series.asp

a = [1, 7, 2]

myvar = pd.Series(a)
if(print_debugging):
    print(myvar)
    print('myvar[0] ' + str(myvar[0]))

myvar = pd.Series(a, index = ["x", "y", "z"])

if(print_debugging):
    print(myvar)
    print('myvar["y"] ' + str(myvar["y"]))

#   Key/Value Object as series (Python Dictionary / JSON)

calories = {
    "day1": 420, 
    "day2": 380, 
    "day3": 390
}

myvar = pd.Series(calories)

if(print_debugging):
    print(myvar)

print("4. DataFrames")
#   https://www.w3schools.com/python/pandas/pandas_dataframes.asp

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data)

if(print_debugging):
    if(print_danger):
        print(df)
    #   refer to the row index:
    print(df.loc[0])
    #   use a list of indexes:
    print(df.loc[[0, 1]])

#   With named index

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

if(print_debugging):
    print(df) 
    #refer to the named index:
    print(df.loc["day2"])
    
print("5. Loading data from CSV")
#   https://www.w3schools.com/python/pandas/pandas_csv.asp

ames = pd.read_csv('data/AmesHousing.csv')

if(print_danger):
    print(ames.to_string()) # Don't run this. It's ugly

if(print_debugging):
    print('Max Rows: ' + str(pd.options.display.max_rows))  #   Print Max rows from CSV
    pd.options.display.max_rows = 9999  #   Set Max rows with the same value   
    ames = pd.read_csv('data/AmesHousing.csv')

print("6. Loading data from JSON")
#   https://www.w3schools.com/python/pandas/pandas_json.asp

df = pd.read_json('data/data.json')

if(print_danger):
    print(df.to_string()) 

print("7. Analysing Data")
#   https://www.w3schools.com/python/pandas/pandas_json.asp

df = pd.read_csv('data/data.csv')
if(print_debugging):
    if(print_danger):
        print(df)
    print(df.head(10))
    print(df.head())  #   Head to view the first 5 rows in a DataFrame
    print(df.tail())  #   Head to view the last 5 rows in a DataFrame