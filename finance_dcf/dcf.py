import os
import pandas
import requests
import string
from bs4 import BeautifulSoup
from functools import partial, reduce
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go


ticker = yf.Ticker("SIDO.JK")

'''''
#Variabel for NetWorkingCapital
total_current_assets_liabilities = ticker.balance_sheet

total_current_assets_liabilities = pd.DataFrame(total_current_assets_liabilities)
total_current_assets = total_current_assets_liabilities.loc['Total Current Assets']
total_current_assets = total_current_assets.iloc[ :1]
#==========
total_current_liabilities = total_current_assets_liabilities.loc['Total Current Liabilities']
total_current_liabilities = total_current_liabilities.iloc[ :1]

#formula NetWorkingCapital
NetWorkingCapital = total_current_assets - total_current_liabilities
print(NetWorkingCapital)
'''

def NetWorkingCapital(ticker):
    #ticker = yf.Ticker("AAPL")
    total_current_assets_liabilities = ticker.balance_sheet
    total_current_assets_liabilities = pd.DataFrame(total_current_assets_liabilities)
    total_current_assets = total_current_assets_liabilities.loc['Total Current Assets']
    total_current_assets = total_current_assets.iloc[ :1]
    total_current_liabilities = total_current_assets_liabilities.loc['Total Current Liabilities']
    total_current_liabilities = total_current_liabilities.iloc[ :1]
    NetWorkingCapital = total_current_assets - total_current_liabilities
    #print(NetWorkingCapital) #untuk menampilkan ke terminal
    return NetWorkingCapital
    
if __name__ == "__main__":
    NetWorkingCapital(ticker)

