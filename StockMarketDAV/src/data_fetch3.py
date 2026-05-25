import yfinance as yf
import pandas as pd

stock = yf.download("HDFCBANK.NS", start = "2024-01-01", end = "2025-01-01")

print(stock.head())

stock.to_csv("data/hdfc_data_set.csv")

print("Data saved Successfully")
