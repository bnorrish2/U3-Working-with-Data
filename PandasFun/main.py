import pandas as pd 

# the major shortcoming of using 2D lists to represent
# tabular data in Python is the lack of label-based
# indexing
# example: header row
# enter pandas!! pandas has two highly optimized
# highly versatile, highly popular objects for
# data science with label-based indexing
# 1D data can be stored in a pandas Series
# 2D data can be stored in pandas DataFrame

# we will start with Series
# there are many ways to make a Series!!
populations = [219190, 744955, 147599, 2010]
cities = ["Spokane", "Seattle", "Bellevue", "Leavenworth"]

# creating
pop_ser = pd.Series(populations) # passing in data
print(pop_ser)
pop_ser = pd.Series(populations, index=cities)
print(pop_ser)
# we can add a name for our series
# useful if we add Series as a column to a DataFrame
pop_ser.name = "Population"
print(pop_ser)

# indexing/slicing
print(pop_ser["Seattle"])
print(pop_ser.iloc[1])
labels = ["Seattle", "Spokane"]
print(pop_ser[labels])
print(pop_ser.iloc[:2])

# summary stats!! (and other methods...)
print(pop_ser.mean())
print(pop_ser.std())
# many others!!!

# can add new entries to a Series like you can dictionary
pop_ser["Pullman"] = 34019
print(pop_ser)

# we can make an empty series
pop_ser2 = pd.Series() 
print(pop_ser2)
pop_ser2["Pullman"] = 34019
print(pop_ser2)

# next we are moving on to dataframes
# lets start with creating a dataframe from a 2D list
df = pd.DataFrame([[0, "a", 1.5], [1, "b", 12.0], [2, "z", -12.2]])
print(df) 
# DataFrames are used to store 2D data
# you can use labels for your rows and for your columns
# example
# creating
data = [["Spokane", 219190, "Medium"], ["Seattle", 744955, "Big"], 
["Bellevue", 147599, "Medium"], ["Leavenworth", 2010, "Small"]]
header = ["City", "Population", "Class"] # labeled data
pop_df = pd.DataFrame(data)
print(pop_df)
# set the labels for the columns to be header
pop_df = pd.DataFrame(data, columns=header)
print(pop_df)
# the labels for the rows are called the Index
# the labels for the columns are called columns
pop_df = pop_df.set_index("City")
print(pop_df)

# indexing/slicing
# grab a column by its label
pop_ser = pop_df["Population"] # returns a Series!!
print(pop_ser)
# grab a row by its label using loc
seattle_ser = pop_df.loc["Seattle"] # returns a Series!!
print(seattle_ser)
# grab a value by its row label and column label
print(pop_df.loc["Seattle", "Population"])
# grab a value by its row position and column position using iloc
print(pop_df.iloc[1, 0])
# slicing
print(pop_df.loc["Spokane": "Bellevue"]) # inclusive of stop value
print(pop_df.iloc[0:2]) # exclusive of stop value
print(pop_df.iloc[0:2, 1])

# creating a data frame from a CSV file
region_df = pd.read_csv("regions.csv", index_col=0)
print(region_df)

# lets do a join on "City"
# we want to merge pop_df and region_df into one DataFrame
# (just like the example from Tabular Data Notes)
# use the merge DataFrame method
merged_df = pop_df.merge(region_df, on="City")
print(merged_df)
# lets write merged_df to a file called merged.csv
merged_df.to_csv("merged.csv")

# last DataFrame topic for PandasFun!!
# data aggregation: gathering and summarizing data
# split-apply-combine
# split a table (dataframe) by the values of an attribute
# create "sub-tables" or "sub-dataframes"
# use the pandas DataFrame method groupby to do this
grouped_by_class = merged_df.groupby("Class") 
# makes 3 "sub-tables" because there are 3 unique values in the Class column
for group_name, group_df in grouped_by_class:
    print("*******")
    print(group_name)
    print(group_df)
    print()

# apply: apply a function to each of the data frames (e.g. mean)
# combine: combine the function results into a new data frame
# (e.g. a data frame of all the group means)