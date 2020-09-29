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