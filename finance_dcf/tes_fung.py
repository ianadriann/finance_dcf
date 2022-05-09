import pandas as pd
import yfinance as yf



ticker_kode = "AALI.JK"
ticker = yf.Ticker(ticker_kode)
#year = datetime.datetime.now()
#year = year.year

ticker_bs = ticker.cashflow
print(ticker_bs)

