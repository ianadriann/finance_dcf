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




cash_and_equivalents_changes = json_data_cashflow['context']['dispatcher']['stores']['QuoteTimeSeriesStore']['timeSeries']['annualOtherCashAdjustmentOutsideChangeinCash']




def cash_and_equivalents_changes_new(cash_and_equivalents_changes):
    if cash_and_equivalents_changes == []:
        cash_and_equivalents_changes = [0, 0, 0, 0]
        cash_and_equivalents_changes_new = cash_and_equivalents_changes[3]
    elif cash_and_equivalents_changes == 0:
        cash_and_equivalents_changes = [0, 0, 0, 0]
        cash_and_equivalents_changes_new = cash_and_equivalents_changes[3]
    elif cash_and_equivalents_changes == None:
        cash_and_equivalents_changes = [0, 0, 0, 0]
        cash_and_equivalents_changes_new = cash_and_equivalents_changes[3]
    else:
        cash_and_equivalents_changes
        cash_and_equivalents_changes_tabel = pd.DataFrame(cash_and_equivalents_changes)
        cash_and_equivalents_changes_tabel = cash_and_equivalents_changes_tabel['reportedValue']
        cash_and_equivalents_changes_tabel = len(cash_and_equivalents_changes_tabel)
        cash_and_equivalents_changes_tabel = cash_and_equivalents_changes_tabel -1
        if cash_and_equivalents_changes[cash_and_equivalents_changes_tabel] == None:
            cash_and_equivalents_changes = 0
        else:
            cash_and_equivalents_changes_new = cash_and_equivalents_changes[cash_and_equivalents_changes_tabel]['reportedValue']['raw']
    return cash_and_equivalents_changes_new

def cash_and_equivalents_changes_old(cash_and_equivalents_changes):
    if cash_and_equivalents_changes == []:
        cash_and_equivalents_changes = [0, 0, 0, 0]
        cash_and_equivalents_changes_old = cash_and_equivalents_changes[2]
    elif cash_and_equivalents_changes == 0:
        cash_and_equivalents_changes = [0, 0, 0, 0]
        cash_and_equivalents_changes_old = cash_and_equivalents_changes[2]
    elif cash_and_equivalents_changes == None:
        cash_and_equivalents_changes = [0, 0, 0, 0]
        cash_and_equivalents_changes_old = cash_and_equivalents_changes[2]
    else:
        cash_and_equivalents_changes
        cash_and_equivalents_changes_tabel = pd.DataFrame(cash_and_equivalents_changes)
        cash_and_equivalents_changes_tabel = cash_and_equivalents_changes_tabel['reportedValue']
        cash_and_equivalents_changes_tabel = len(cash_and_equivalents_changes_tabel)
        cash_and_equivalents_changes_tabel = cash_and_equivalents_changes_tabel -2
        if cash_and_equivalents_changes[cash_and_equivalents_changes_tabel] == None:
            cash_and_equivalents_changes = 0
        else:
            cash_and_equivalents_changes_old = cash_and_equivalents_changes[cash_and_equivalents_changes_tabel]['reportedValue']['raw']
    return cash_and_equivalents_changes_old


depreciation_expenses = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['incomeStatementHistory']['incomeStatementHistory']

depreciation_expenses = pd.DataFrame(depreciation_expenses)
depreciation_expenses = depreciation_expenses['incomeBeforeTax']




for i in depreciation_expenses:
    statement = {}
    for key, val in i.items()
    



print(depreciation_expenses)


