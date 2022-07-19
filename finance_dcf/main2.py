from calendar import c
from codecs import ignore_errors
from sys import set_coroutine_origin_tracking_depth
from tokenize import Ignore
from tracemalloc import start
from urllib import response
from webbrowser import get
from numpy import append
import pandas as pd
import pandas
import yfinance as yf
import datetime
import os
import string
from bs4 import BeautifulSoup
from functools import partial, reduce
import plotly.graph_objects as go
import re
import json
import csv
from io import StringIO
import requests


ticker_kode = "AAPL"
ticker = yf.Ticker(ticker_kode)

ticker_is = ticker.financials
ticker_bs = ticker.balance_sheet


#==============url=======
url_bs = 'https://finance.yahoo.com/quote/{}/balance-sheet?p={}'

headers = { 'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36' }
response_bs = requests.get(url_bs.format(ticker_kode, ticker_kode),headers={'user-agent':'my-app'})
soup_bs = BeautifulSoup(response_bs.text, 'html.parser')
pattern_bs = re.compile(r'\s--\sData\s--\s')
script_data_bs = soup_bs.find('script', text=pattern_bs).contents[0]
start_bs = script_data_bs.find("context")-2
json_data_bs = json.loads(script_data_bs[start_bs:-12])
ppe = json_data_bs['context']['dispatcher']['stores']['QuoteTimeSeriesStore']['timeSeries']['annualNetPPE']


def ebit_new(ticker_is):
    ebit = ticker_is
    ebit = pd.DataFrame(ebit)
    ebit = ebit.loc['Ebit']
    ebit_new = ebit.iloc[ :1]
    ebit_new = ebit_new.values
    return ebit_new

def pre_tax_income_new(ticker_is):
    pre_tax_income = ticker_is
    pre_tax_income = pd.DataFrame(pre_tax_income)
    pre_tax_income = pre_tax_income.loc['Income Before Tax']
    pre_tax_income_new = pre_tax_income.iloc[ :1]
    pre_tax_income_new = pre_tax_income_new.values
    return pre_tax_income_new

def taxes_paid_new(ticker_is):
    taxes_paid = ticker_is
    taxes_paid = pd.DataFrame(taxes_paid)
    taxes_paid = taxes_paid.loc['Income Tax Expense']
    taxes_paid_new = taxes_paid.iloc[ :1]
    taxes_paid_new = taxes_paid_new.values
    return taxes_paid_new

def ppe_new(ppe):
    if ppe == []:
        ppe = [0, 0, 0, 0]
        ppe_new = ppe[3]
    elif ppe == 0:
        ppe = [0, 0, 0, 0]
        ppe_new = ppe[3]
    elif ppe == None:
        ppe = [0, 0, 0, 0]
        ppe_new = ppe[3]
    else:
        ppe
        ppe_tabel = pd.DataFrame(ppe)
        ppe_tabel = ppe_tabel['reportedValue']
        ppe_tabel = len(ppe_tabel)
        ppe_tabel = ppe_tabel -1
        if ppe[ppe_tabel] == None:
            ppe_new = 0
        else:
            ppe_new = ppe[ppe_tabel]['reportedValue']['raw']
    return ppe_new
#==========================

Ebit = ebit_new(ticker_is)
pre_tax_income =  pre_tax_income_new(ticker_is)
taxes_paid = taxes_paid_new(ticker_is)
ppe = ppe_new(ppe)


#=========================
'''
Calculating the unlevered free cash flows (FCF)
Here is the unlevered free cash flow formula:

FCF = EBIT x (1- tax rate) + D&A + NWC - Capital expenditures
**
    Tax Rate = taxes_paid ÷ pre_tax_income
    D&A = Depreciation & Amortization 
        Depreciation = (Total PP&E Cost - Salvage Value) / Useful Life Assumption

'''
number_years = 1
tax_rate = taxes_paid / pre_tax_income
salvage_value = ppe/number_years
depreciation = (ppe - salvage_value) / number_years

fcf = Ebit * (1-tax_rate)
print(depreciation)