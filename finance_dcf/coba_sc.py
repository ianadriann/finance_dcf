import re
import json
import csv
from io import StringIO
from bs4 import BeautifulSoup
import requests
import pandas as pd

# url templates
url_stats = 'https://finance.yahoo.com/quote/{}/key-statistics?p={}'
url_profile = 'https://finance.yahoo.com/quote/{}/profile?p={}'
url_financials = 'https://finance.yahoo.com/quote/{}/financials?p={}'
url_cashflow = 'https://finance.yahoo.com/quote/{}/cash-flow?p={}' #cash flow

# the stock I want to scrape
stock = 'ATIC.JK'

headers = { 'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15' }
response = requests.get(url_financials.format(stock, stock),headers={'user-agent':'my-app'})
response_cachflow = requests.get(url_cashflow.format(stock, stock),headers={'user-agent':'my-app'}) #cash flow

soup = BeautifulSoup(response.text, 'html.parser')
pattern = re.compile(r'\s--\sData\s--\s')
script_data = soup.find('script', text=pattern).contents[0]

soup_cashflow = BeautifulSoup(response_cachflow.text, 'html.parser')
pattern_cashflow = re.compile(r'\s--\sData\s--\s')
script_data_cashflow = soup_cashflow.find('script', text=pattern_cashflow).contents[0]

# find the starting position of the json string
start = script_data.find("context")-2
start_cashflow = script_data_cashflow.find("context")-2

# slice the json string
json_data = json.loads(script_data[start:-12])
json_data_cashflow = json.loads(script_data_cashflow[start:-12])

# income statement
annual_is = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['incomeStatementHistory']['incomeStatementHistory']
quarterly_is = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['incomeStatementHistoryQuarterly']['incomeStatementHistory']

# cash flow statement
annual_cf = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['cashflowStatementHistory']['cashflowStatements']
quarterly_cf = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['cashflowStatementHistoryQuarterly']['cashflowStatements']

# balance sheet
annual_bs = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['balanceSheetHistory']['balanceSheetStatements']
quarterly_bs = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['balanceSheetHistoryQuarterly']['balanceSheetStatements']




fx_rate_effect_on_cash = json_data_cashflow['context']['dispatcher']['stores']['QuoteTimeSeriesStore']['timeSeries']['annualEffectOfExchangeRateChanges']


def fx_rate_effect_on_cash_new(fx_rate_effect_on_cash):
    if fx_rate_effect_on_cash == []:
        fx_rate_effect_on_cash = [0, 0, 0, 0]
        fx_rate_effect_on_cash_new = fx_rate_effect_on_cash[3]
    elif fx_rate_effect_on_cash == 0:
        fx_rate_effect_on_cash = [0, 0, 0, 0]
        fx_rate_effect_on_cash_new = fx_rate_effect_on_cash[3]
    elif fx_rate_effect_on_cash == None:
        fx_rate_effect_on_cash = [0, 0, 0, 0]
        fx_rate_effect_on_cash_new = fx_rate_effect_on_cash[3]
    else:
        fx_rate_effect_on_cash
        if fx_rate_effect_on_cash[3] == None:
            fx_rate_effect_on_cash_new = 0
        else:
            fx_rate_effect_on_cash_new = fx_rate_effect_on_cash[3]['reportedValue']['raw']
    return fx_rate_effect_on_cash_new

def fx_rate_effect_on_cash_old(fx_rate_effect_on_cash):
    if fx_rate_effect_on_cash == []:
        fx_rate_effect_on_cash = [0, 0, 0, 0]
        fx_rate_effect_on_cash_old = fx_rate_effect_on_cash[2]
    elif fx_rate_effect_on_cash == 0:
        fx_rate_effect_on_cash = [0, 0, 0, 0]
        fx_rate_effect_on_cash_old = fx_rate_effect_on_cash[2]
    elif fx_rate_effect_on_cash == None:
        fx_rate_effect_on_cash = [0, 0, 0, 0]
        fx_rate_effect_on_cash_old = fx_rate_effect_on_cash[2]
    else:
        fx_rate_effect_on_cash
        if fx_rate_effect_on_cash[2] == None:
            fx_rate_effect_on_cash_old = 0
        else:
            fx_rate_effect_on_cash_old = fx_rate_effect_on_cash[2]['reportedValue']['raw']
    return fx_rate_effect_on_cash_old

#print(fx_rate_effect_on_cash_old(fx_rate_effect_on_cash))

def fx_rate_effect_on_cash_new(fx_rate_effect_on_cash):
    if fx_rate_effect_on_cash == []:
        fx_rate_effect_on_cash = [0, 0, 0, 0]
        fx_rate_effect_on_cash_new = fx_rate_effect_on_cash[3]
    elif fx_rate_effect_on_cash == 0:
        fx_rate_effect_on_cash = [0, 0, 0, 0]
        fx_rate_effect_on_cash_new = fx_rate_effect_on_cash[3]
    elif fx_rate_effect_on_cash == None:
        fx_rate_effect_on_cash = [0, 0, 0, 0]
        fx_rate_effect_on_cash_new = fx_rate_effect_on_cash[3]
    else:
        fx_rate_effect_on_cash
        if fx_rate_effect_on_cash[3] == None:
            fx_rate_effect_on_cash_new = 0
        else:
            fx_rate_effect_on_cash_new = fx_rate_effect_on_cash[3]['reportedValue']['raw']
    return fx_rate_effect_on_cash_new



#print(tabel2)

#rint(tabel1)
'''
#jumlah = len(fx_rate_effect_on_cash.columns)
tabel = pd.DataFrame(fx_rate_effect_on_cash)
tabel1 = tabel['reportedValue']
tabel2 = pd.DataFrame(tabel1)

tabel3 = len(tabel2)
jumlah = tabel2 - 1
coba = 'ianadrian{}bustan'
coba1 = coba.format(jumlah)

'''
'''
fx_rate_effect_on_cash_tabel = pd.DataFrame(fx_rate_effect_on_cash)
fx_rate_effect_on_cash_tabel = fx_rate_effect_on_cash_tabel['reportedValue']
fx_rate_effect_on_cash_tabel = len(fx_rate_effect_on_cash_tabel)
fx_rate_effect_on_cash_tabel = fx_rate_effect_on_cash_tabel -1


if fx_rate_effect_on_cash[fx_rate_effect_on_cash_tabel] == None:
    print("oke beres")
else:
    print(fx_rate_effect_on_cash[fx_rate_effect_on_cash_tabel]['reportedValue']['raw'])
'''

def fx_rate_effect_on_cash_new(fx_rate_effect_on_cash):
    fx_rate_effect_on_cash_tabel = pd.DataFrame(fx_rate_effect_on_cash)
    fx_rate_effect_on_cash_tabel = fx_rate_effect_on_cash_tabel['reportedValue']
    fx_rate_effect_on_cash_tabel = len(fx_rate_effect_on_cash_tabel)
    fx_rate_effect_on_cash_tabel = fx_rate_effect_on_cash_tabel -1
    if fx_rate_effect_on_cash == []:
        fx_rate_effect_on_cash = [0, 0, 0, 0]
        fx_rate_effect_on_cash_new = fx_rate_effect_on_cash[3]
    elif fx_rate_effect_on_cash == 0:
        fx_rate_effect_on_cash = [0, 0, 0, 0]
        fx_rate_effect_on_cash_new = fx_rate_effect_on_cash[3]
    elif fx_rate_effect_on_cash == None:
        fx_rate_effect_on_cash = [0, 0, 0, 0]
        fx_rate_effect_on_cash_new = fx_rate_effect_on_cash[3]
    else:
        fx_rate_effect_on_cash
        if fx_rate_effect_on_cash[fx_rate_effect_on_cash_tabel] == None:
            fx_rate_effect_on_cash_new = 0
        else:
            fx_rate_effect_on_cash_new = fx_rate_effect_on_cash[fx_rate_effect_on_cash_tabel]['reportedValue']['raw']
    return fx_rate_effect_on_cash_new

print(fx_rate_effect_on_cash_new(fx_rate_effect_on_cash))






