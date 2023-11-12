import pandas as pd
import numpy as np

# create DataFrame, assign it to variable, print the dataframe and types for values in columns
dict = {'FirstName': ['Alex', 'Mike', 'John'],
        'LastName': ['Michaels', 'Jackson', 'Sage'],
        'Age': [18, 25, 33]}

df = pd.DataFrame(dict)
# prints DataFrame
print(df)
# prints DataFrame types
print(df.dtypes)
# prints DataFrame rows from head
print(df.head(1))
# prints DataFrame rows from tail
print(df.tail(1))
# prints index labels of the DataFrame
print(df.index)
# prints column labels of the DataFrame
print(df.columns)
# print numpy representation
print(df.to_numpy())
# prints details on numeric values
print(df.describe())
# prints transposed DataFrame
print(df.T)
# prints the sorted along the axis DataFrame, 'axis = 1' for columns, 'axis = 0' for rows. 
print(df.sort_index(axis=0, ascending=False))
# prints the DataFrame sortoed along the values of a given column
print(df.sort_values(by="FirstName"))
# prints given column's values
print(df.FirstName)
# prints selected rows of a DataFrame
print(df[1:3])
# print selected row:
print(df.loc[0])
# prints slice object 
print(df.loc[:, ['LastName']])
# prints a portion of a DataFrame
print(df.loc['0':'1', ['FirstName', 'Age']])
# prints an item from given column and row of a DataFrame
print(df.iloc[2])
# print a portion of a DataFrame
print(df.iloc[1:3, 1:3])
# printt selected values within given rows and columns
print(df.iloc[[0, 2, 4], [1, 3]])
# print row with given index
print(df.iloc[0])
# prints exact value
print(df.iloc[1, 1])
# prints portion of a DataFrame using slicing
print(df.iloc[1:3, :])
print(df.iloc[:, 1:3])
# prints rows with value greater/smaller than given in a column
print(df[df["Age"] > 30])
# prints the copy of a DataFrame
print(df2 = df.copy())
