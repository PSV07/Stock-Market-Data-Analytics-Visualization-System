import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("data/cleaned_data/reliance_cleaned.csv")

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

print("\n===== DATASET OVERVIEW =====")
print(df.head())

print("\n===== STATISTICAL SUMMARY =====")
print(df.describe())

# Daily Return Calculation
df['Daily Return %'] = df['Close'].pct_change() * 100

# Moving Average
df['Moving Average 20'] = df['Close'].rolling(window=20).mean()

print("\n===== DAILY RETURNS =====")
print(df[['Date', 'Daily Return %']].head())

# -------------------------------
# Visualization 1: Closing Price Trend
# -------------------------------

plt.figure(figsize=(12,6))
plt.plot(df['Date'], df['Close'])
plt.title("Reliance Closing Price Trend")
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.grid(True)
plt.show()

# -------------------------------
# Visualization 2: Volume Trend
# -------------------------------

plt.figure(figsize=(12,6))
plt.bar(df['Date'], df['Volume'])
plt.title("Trading Volume")
plt.xlabel("Date")
plt.ylabel("Volume")
plt.show()

# -------------------------------
# Visualization 3: Moving Average
# -------------------------------

plt.figure(figsize=(12,6))
plt.plot(df['Date'], df['Close'], label='Closing Price')
plt.plot(df['Date'], df['Moving Average 20'], label='20-Day Moving Average')
plt.title("Closing Price vs Moving Average")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.show()

# -------------------------------
# Visualization 4: Correlation Heatmap
# -------------------------------

plt.figure(figsize=(8,6))

correlation = df[['Close', 'High', 'Low', 'Open', 'Volume']].corr()

sns.heatmap(correlation, annot=True)

plt.title("Correlation Heatmap")
plt.show()

print("\nEDA Completed Successfully")
