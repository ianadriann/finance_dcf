import pandas as pd
import yfinance as yf



ticker_kode = "ABBA.JK"
ticker = yf.Ticker(ticker_kode)
#year = datetime.datetime.now()
#year = year.year

ticker_bs = ticker.balance_sheet
print(ticker_bs)

Cash                 =             2.672453e+10 , 2.337615e+10 , 3.615378e+10 , 4.756197e+10