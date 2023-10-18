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
