import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#load cleaned dataset
df = pd.read_csv("data/cleaned_data/tcs_cleaned_data.csv")

#Convert Date Column
df['Date'] = pd.to_datetime(df['Date'])

print("\n=======DATASET OVERVIEW========")
#print(df.head())

print("\n=======STATISTICAL SUMMARY=======")
#print(df.describe())

# Daily retin calcultion
df['Daily Return %'] = df['Close'].pct_change() * 100

# Moving Average
df['Moving Average 20'] = df['Close'].rolling(window =20).mean()

print("\n=======Daily Return=========")
#print(df[['Date', 'Daily Return %']].head())

# -------------------------------
# Visualization 1: Closing Price Trend
# -------------------------------

plt.figure(figsize = (12,6))
plt.plot(df['Date'], df['Close'])
plt.title("TCS Closing Price Trend")
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.grid(False)
#plt.show()

# -------------------------------
# Visualization 2: Volume Trend
# -------------------------------

plt.figure(figsize = (12, 6))
plt.plot(df['Date'], df['Volume'])
plt.title("Volume Trend")
plt.xlabel(df["Date"])
plt.ylabel(df["Volume"])
#plt.show()


# -------------------------------
# Visualization 3: Moving Average
# -------------------------------

plt.figure(figsize=(12,6))
plt.plot(df['Date'], df['Close'], label = 'Closing Price')
plt.plot(df['Date'], df['Moving Average 20'], label='20-Day Moving Average')
plt.title("Moving Average")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(False)
plt.show()


# -------------------------------
# Visualization 4: Correlation Heatmap
# -------------------------------

plt.figure(figsize=(8,6))
correlation = df[['Close','High', 'Low','Open', 'Volume']].corr()

sns.heatmap(correlation, annot = True)

plt.title("Correlation Heatmap")
plt.show()

print("\n EDA Completed Successfully")























