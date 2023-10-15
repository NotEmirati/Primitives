import pandas as pd
import numpy as np

# create DataFrame, assign it to variable, print the dataframe and types for values in columns
dict = {'FirstName': ['Alex', 'Mike', 'John'],
        'LastName': ['Michaels', 'Jackson', 'Sage'],
        'Age': [18, 25, 33]}

df = pd.DataFrame(dict)
print(df)
print(df.dtypes)
print(df.head(1))
print(df.tail(1))
