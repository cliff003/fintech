import pandas as pd
import yfinance as yf

# Enter ticker list
ticker = "ARMK LOCO W SHAK JAX STAF BH VVI WEN EAT BH CBRL MCD VHI MAR MCS BDL LUB GTIM DIN JACK RAVE DRI YUM ARKR RRGB DPZ TXRH KONA RUTH CMG TAST"

# gather year-end Adjusted Close price
price_2017 = yf.download(ticker, start="2017-12-21", end="2018-01-01")["Adj Close"]
price_2018 = yf.download(ticker, start="2018-12-21", end="2019-01-01")["Adj Close"]
price_2019 = yf.download(ticker, start="2019-12-21", end="2020-01-01")["Adj Close"]

# Combine dataframes together
total = pd.concat([price_2017.iloc[-1:], price_2018.iloc[-1:], price_2019.iloc[-1:]], axis=0, join='inner')

# Switch columns and rows
total = total.transpose()

# Write to csv, can be imported to Excel later
total.to_csv("total.csv")

# Visulize the prices
print(total)