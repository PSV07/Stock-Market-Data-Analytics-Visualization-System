import pandas as pd
import os

#load dataset
df = pd.read_csv("data/tcs_stock_data.csv", skiprows = 2)

#column renaming
df.columns = ['Date','Close','High','Low','Open','Volume']

print("\n=========First 5 rows=========")
print(df.head())

print("\n==========Dataset info==========")
print(df.info())

print("\n==========checking null value==========")
print(df.isnull().sum())

print("\n==========Checkig duplicate==========")
print("Duplicate Rows : ",df.duplicated().sum())

# remove duplicates rows
df = df.drop_duplicates()

#Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

#Convert numerical columns
numeric_columns = ['Close','High','Low','Open','Volume']
for col in numeric_columns :
    df[col] = pd.to_numeric(df[col], errors = 'coerce')

#remove rows with null values
df = df.dropna();

print("\n==========CLEANED DATASET==========")
print(df.head())

# create Clean_data folder
os.makedirs("data/cleaned_data", exist_ok = True)

#SAve cleaned dataset
df.to_csv("data/cleaned_data/tcs_cleaned_data.csv", index = False)

print("\nData cleaning completed successfully")
