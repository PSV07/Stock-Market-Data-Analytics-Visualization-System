import yfinance as yf
import pandas as pd

#Fetch stock data
stock = yf.download("RELIANCE.NS" , start = "2024-01-01", end = "2025-01-01")

#show first 5 rows
print(stock.head())

#Save data
stock.to_csv("data/reliance_stock_data.csv")

print("Data saved Successfully") 
