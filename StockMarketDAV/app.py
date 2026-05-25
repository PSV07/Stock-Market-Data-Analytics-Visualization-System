import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# -------------------------
# PAGE TITLE
# -------------------------

st.title("Stock Market Data Analytics Dashboard")

st.write("Reliance Stock Market Analysis System")

# -------------------------
# LOAD DATA
# -------------------------

df = pd.read_csv("data/cleaned_data/reliance_cleaned.csv")

df['Date'] = pd.to_datetime(df['Date'])

# Daily Return
df['Daily Return %'] = df['Close'].pct_change() * 100

# Moving Average
df['Moving Average 20'] = df['Close'].rolling(window=20).mean()

# -------------------------
# MACHINE LEARNING MODEL
# -------------------------

X = df[['Open', 'High', 'Low', 'Volume']]

y = df['Close']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

# -------------------------
# DATA PREVIEW
# -------------------------

st.subheader("Dataset Preview")

st.dataframe(df.head())

# -------------------------
# KPI SECTION
# -------------------------

st.subheader("Key Performance Indicators")

col1, col2, col3 = st.columns(3)

col1.metric("Highest Price", round(df['High'].max(), 2))
col2.metric("Lowest Price", round(df['Low'].min(), 2))
col3.metric("Average Closing Price", round(df['Close'].mean(), 2))

# -------------------------
# Closing Price Trend
# -------------------------

st.subheader("Closing Price Trend")

fig1, ax1 = plt.subplots(figsize=(12,6))

ax1.plot(df['Date'], df['Close'])

ax1.set_xlabel("Date")
ax1.set_ylabel("Closing Price")
ax1.set_title("Reliance Closing Price")

st.pyplot(fig1)

# -------------------------
# Volume Chart
# -------------------------

st.subheader("Trading Volume")

fig2, ax2 = plt.subplots(figsize=(12,6))

ax2.bar(df['Date'], df['Volume'])

ax2.set_xlabel("Date")
ax2.set_ylabel("Volume")
ax2.set_title("Trading Volume")

st.pyplot(fig2)

# -------------------------
# Moving Average
# -------------------------

st.subheader("Moving Average Analysis")

fig3, ax3 = plt.subplots(figsize=(12,6))

ax3.plot(df['Date'], df['Close'], label="Closing Price")

ax3.plot(df['Date'], df['Moving Average 20'], label="20-Day Moving Average")

ax3.legend()

ax3.set_title("Moving Average")

st.pyplot(fig3)

# -------------------------
# Correlation Heatmap
# -------------------------

st.subheader("Correlation Heatmap")

correlation = df[['Close', 'High', 'Low', 'Open', 'Volume']].corr()

fig4, ax4 = plt.subplots(figsize=(8,6))

sns.heatmap(correlation, annot=True, ax=ax4)

st.pyplot(fig4)

# -------------------------
# Daily Returns
# -------------------------

st.subheader("Daily Return Analysis")

fig5, ax5 = plt.subplots(figsize=(12,6))

ax5.plot(df['Date'], df['Daily Return %'])

ax5.set_title("Daily Return %")

st.pyplot(fig5)

# -------------------------
# STOCK PRICE PREDICTION
# -------------------------

st.subheader("Stock Price Prediction")

open_price = st.number_input("Open Price", value=1400.0)

high_price = st.number_input("High Price", value=1415.0)

low_price = st.number_input("Low Price", value=1395.0)

volume = st.number_input("Volume", value=5000000.0)

# Prediction Button

if st.button("Predict Closing Price"):

    sample_data = pd.DataFrame({
        'Open': [open_price],
        'High': [high_price],
        'Low': [low_price],
        'Volume': [volume]
    })

    prediction = model.predict(sample_data)

    st.success(f"Predicted Closing Price: ₹ {prediction[0]:.2f}")



st.success("Dashboard Loaded Successfully")
