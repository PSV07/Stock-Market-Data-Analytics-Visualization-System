import pandas as pd
import os

# load dataset
df = pd.read_csv("data/hdfc_data_set.csv",skiprows = 2)

df.columns = ['Date', 'Close', 'High', 'Low', 'Open', 'Volume'] 

print("\n==========First 5 rows==========")
print(df.head())

print("\n==========Dataset info==========")
print(df.info())

print("\n==========Checking null values==========")
print(df.isnull().sum())

print("\n==========Checking Duplicate==========")
print(df.duplicated().sum())

# CLeaning dataset

df = df.drop_duplicates()

df = df.dropna()

df['Date'] = pd.to_datetime(df['Date'])

numeric_columns = ['Close', 'High', 'Low', 'Open', 'Volume']

for col in numeric_columns :
    df[col] = pd.to_numeric(df[col], errors = 'coerce')

print("\n========Cleaned DATASET========")

os.makedirs("date/cleaned_data", exist_ok = True)

df.to_csv("data/cleaned_data/hdfc_cleaned.csv", index = False)

print("Data Cleaned Successfully")
