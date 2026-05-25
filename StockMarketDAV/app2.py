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
st.write("Tcs Stock market Analysis System")

# -------------------------
# LOAD DATA
# -------------------------

uploaded_file = st.file_uploader(
    "Upload Stock Dataset",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)


df['Date'] = pd.to_datetime(df['Date'])

#Daily return
df['Daily Return %'] = df['Close'].pct_change() * 100

#Moving average
df['Moving Average'] = df['Close'].rolling(window = 20).mean()


# -------------------------
# MACHINE LEARNING MODEL
# -------------------------

X = df[['Open','High','Low','Volume']]

y = df['Close']

X_train, X_test , y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

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

st.subheader("Key Performanc Indicators")

col1,col2,col3 = st.columns(3)

col1.metric("Highest Price", round(df['High']).max(), 2)
col2.metric("Lowest Price", round(df['Low']).max(), 2)
col3.metric("Average Closing price",round(df['Close']).max(), 2)

# -------------------------
# Closing Price Trend
# -------------------------

st.subheader("Closing Pric Trend")

fig1,axl = plt.subplots(figsize = (12,6))

axl.scatter(df['Date'], df['Close'])

axl.set_xlabel("Date")
axl.set_ylabel("Closing Price")
axl.set_title("Tcs CLosing Price")

st.pyplot(fig1)

# -------------------------
# Volume Trend
# -------------------------

st.subheader("Volume Trend")

fig2, axl2 = plt.subplots(figsize = (12, 6))

axl2.bar(df['Date'], df['Volume'])

axl2.set_xlabel("Date")
axl2.set_ylabel("Volume")
axl2.set_title("Volume Trend")

st.pyplot(fig2)

# -------------------------
#  Moving Average
# -------------------------

st.subheader("Moving Average Analysis")

fig3, axl3 = plt.subplots(figsize = (12, 6))

axl3.plot(df['Date'], df['Close'], label = "Closing Price")
axl3.plot(df['Date'], df['Moving Average'], label = "20-Day Moving Average")

axl3.legend()
axl3.set_title("Moving Average")

st.pyplot(fig3)

# -------------------------
#  Moving Average
# -------------------------

st.subheader("Correlation HeatMap")

correlation = df[['Close', 'High', 'Low','Open','Volume']].corr()

fig4, axl4 = plt.subplots(figsize = (8,6))

sns.heatmap(correlation, annot = True, ax = axl4)

st.pyplot(fig4)

# -------------------------
# Daily Returns
# -------------------------

st.subheader("Daily Return Analysis")

fig5, axl5 = plt.subplots(figsize = (12,6))

axl5.plot(df['Date'], df['Daily Return %'])
axl5.set_xlabel("Date")
axl5.set_ylabel("Daily Return")

st.pyplot(fig5)

# -------------------------
# STOCK PRICE PREDICTION
# -------------------------

st.subheader("Stock Price Prediction")

open_price = st.number_input("Open Price", value = 1400.0)

High_price = st.number_input("High Price", value = 1489.0)

Low_price = st.number_input("Low Price", value = 1392.0)

Volume = st.number_input("Volume Price", value = 500000.0)

# Prediction Button

if st.button("Predict Closing Price"):

    sample_data = pd.DataFrame({
        'Open' : [open_price],
        'High' : [High_price],
        'Low' :[Low_price],
        'Volume' : [Volume]
        })

    prediction = model.predict(sample_data)

    st.success(f"Prediction Closing Price: ₹ {prediction[0]:.2f}")



    

st.success("DashBoard Loaded Successfully")


            
            












