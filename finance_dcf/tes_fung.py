import re
import json
import csv
from io import StringIO
from bs4 import BeautifulSoup
import requests

# url templates
url_stats = 'https://finance.yahoo.com/quote/{}/key-statistics?p={}'
url_profile = 'https://finance.yahoo.com/quote/{}/profile?p={}'
url_financials = 'https://finance.yahoo.com/quote/{}/financials?p={}'

# the stock I want to scrape
stock = 'AALI.JK'

headers = { 'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15' }
response = requests.get(url_financials.format(stock, stock),headers={'user-agent':'my-app'})

soup = BeautifulSoup(response.text, 'html.parser')
pattern = re.compile(r'\s--\sData\s--\s')
script_data = soup.find('script', text=pattern).contents[0]

# find the starting position of the json string
start = script_data.find("context")-2

# slice the json string
json_data = json.loads(script_data[start:-12])

'''
# income statement
annual_is = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['incomeStatementHistory']['incomeStatementHistory']
quarterly_is = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['incomeStatementHistoryQuarterly']['incomeStatementHistory']
#print(quarterly_is[3])

annual_bs = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['balanceSheetHistory']['balanceSheetStatements']

annual_cf = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['cashflowStatementHistory']['cashflowStatements']
quarterly_cf = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['cashflowStatementHistoryQuarterly']['cashflowStatements']

print(quarterly_cf[3])

BS (Anual)
BS (Q)

IS (anual)
IS (Q)

CF (A)
CF (Q)

'''

is_full = json_data['context']['dispatcher']['stores']['QuoteTimeSeriesStore']['timeSeries']
asme = is_full['annualSellingAndMarketingExpense']
#print(asme)

is_full2 = json_data['context']['dispatcher']['stores']['QuoteTimeSeriesStore']['timeSeries']['annualSellingAndMarketingExpense']



annual_is_stmts = []

# consolidate annual
for s in is_full2:
    statement = {}
    for key, val in s.items():
        try:
            statement[key] = val['raw']
        except TypeError:
            continue
        except KeyError:
            continue
    annual_is_stmts.append(statement)



if annual_is_stmts == []:
    annual_is_stmts = 0
    #print(annual_is_stmts)
else:
    #print("oke lanjut")
    print(annual_is_stmts[0]['reportedValue'])
    print(annual_is_stmts[1]['reportedValue'])
    print(annual_is_stmts[2]['reportedValue'])
    print(annual_is_stmts[3]['reportedValue'])


#coba mau repo

