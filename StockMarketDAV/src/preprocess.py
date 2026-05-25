import pandas as pd
import os

# Load CSV while skipping problematic rows
df = pd.read_csv("data/reliance_stock_data.csv", skiprows=2)

# Rename columns properly
df.columns = ['Date', 'Close', 'High', 'Low', 'Open', 'Volume']


print("\n===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== DATASET INFO =====")
print(df.info())

print("\n===== CHECKING NULL VALUES =====")
print(df.isnull().sum())

print("\n===== CHECKING DUPLICATES =====")
print("Duplicate Rows:", df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])


# Convert numerical columns
numeric_columns = ['Close', 'High', 'Low', 'Open', 'Volume']

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors ='coerce')


# Remove rows with null values
df = df.dropna()

print("\n===== CLEANED DATASET =====")
print(df.head())

# Create cleaned_data folder
os.makedirs("data/cleaned_data", exist_ok=True)

# Save cleaned dataset
df.to_csv("data/cleaned_data/reliance_cleaned.csv", index=False)

print("\nData cleaning completed successfully")
