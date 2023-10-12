import pandas as pd

# create DataFrame, assign it to variable, print it
dict = {'FirstName': ['Alex', 'Mike', 'John'],
        'LastName': ['Michaels', 'Jackson', 'Sage'],
        'Age': [18, 25, 33]}

df = pd.DataFrame(dict)
print(df)
