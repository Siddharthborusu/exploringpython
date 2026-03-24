import pandas as pd

data = {
    "Name": ["Siddharth", "Albert", "Neitzche"],
    "Age": [25, 30, 35],
    "Salary": [50000, 60000, 70000]
}

df = pd.DataFrame(data)

print(df)
print(df['Name'])
print(df[['Name', 'Age']])

# First row (by index)
print(df.iloc[0]) 

# Row with label 1
print(df.loc[1])           