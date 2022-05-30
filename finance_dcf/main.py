from calendar import c
from codecs import ignore_errors
from sys import set_coroutine_origin_tracking_depth
from tokenize import Ignore
from webbrowser import get
#from turtle import clear
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

#=======
import re
import json
import csv
from io import StringIO
import requests

########## ============= SCRAPPING WEB =======================############
# url templates
url_stats = 'https://finance.yahoo.com/quote/{}/key-statistics?p={}'
url_profile = 'https://finance.yahoo.com/quote/{}/profile?p={}'
url_financials = 'https://finance.yahoo.com/quote/{}/financials?p={}'
url_cashflow = 'https://finance.yahoo.com/quote/{}/cash-flow?p={}'

#ticker_kode = "AALI.JK"

kode = input("masukkan kode saham= ")
negara = input("masukkan negara= ")
if negara == "Indonesia":
    ticker_kode = kode + ".JK"
else:
    ticker_kode = kode

#headers = { 'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15' }
headers = { 'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36' }
response = requests.get(url_financials.format(ticker_kode, ticker_kode),headers={'user-agent':'my-app'})
response_cachflow = requests.get(url_cashflow.format(ticker_kode, ticker_kode),headers={'user-agent':'my-app'})


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

Selling_Marketing_Expense = json_data['context']['dispatcher']['stores']['QuoteTimeSeriesStore']['timeSeries']['annualSellingAndMarketingExpense']
depreciation_expenses = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['incomeStatementHistory']['incomeStatementHistory']
tax_expenses = json_data['context']['dispatcher']['stores']['QuoteTimeSeriesStore']['timeSeries']['annualNetIncomeContinuousOperations']
after_tax_income_operational = json_data['context']['dispatcher']['stores']['QuoteTimeSeriesStore']['timeSeries']['annualNetIncomeDiscontinuousOperations']
comprehensive_income = json_data['context']['dispatcher']['stores']['QuoteTimeSeriesStore']['timeSeries']['annualBasicEPS'] #EPS
income_per_share = json_data['context']['dispatcher']['stores']['QuoteTimeSeriesStore']['timeSeries']['annualReconciledDepreciation']

fx_rate_effect_on_cash = json_data_cashflow['context']['dispatcher']['stores']['QuoteTimeSeriesStore']['timeSeries']['annualEffectOfExchangeRateChanges']
cash_and_equivalents_changes = json_data_cashflow['context']['dispatcher']['stores']['QuoteTimeSeriesStore']['timeSeries']['annualOtherCashAdjustmentOutsideChangeinCash']


#print(after_tax_income_operational)




#======================akhir========================

ticker_kode = ticker_kode
ticker = yf.Ticker(ticker_kode)
#year = datetime.datetime.now()
#year = year.year

ticker_bs = ticker.balance_sheet
ticker_cf = ticker.cashflow
ticker_is = ticker.financials
#print(ticker_is)

#print(ticker_cf)
year_new = ticker_bs.columns[0]
year_new = year_new.year
year_old = year_new - 1



#tabel bS

def cash_and_equivalents_new(ticker_bs):
    cash_and_equivalents = ticker_bs
    cash_and_equivalents = pd.DataFrame(cash_and_equivalents)
    cash_and_equivalents = cash_and_equivalents.loc['Cash']
    cash_and_equivalents_new = cash_and_equivalents.iloc[ :1]
    cash_and_equivalents_new = cash_and_equivalents_new.values
    return cash_and_equivalents_new

def cash_and_equivalents_old(ticker_bs):
    cash_and_equivalents = ticker_bs
    cash_and_equivalents = pd.DataFrame(cash_and_equivalents)
    cash_and_equivalents = cash_and_equivalents.loc['Cash']
    cash_and_equivalents_min1 = cash_and_equivalents.iloc[1:2]
    cash_and_equivalents_min1 = cash_and_equivalents_min1.values
    #cash_and_equivalents_min1 = cash_and_equivalents.loc[['1']]
    return cash_and_equivalents_min1

def total_current_assets_new(ticker_bs):
    total_current_assets = ticker_bs
    total_current_assets = pd.DataFrame(total_current_assets)
    total_current_assets = total_current_assets.loc['Total Current Assets']
    total_current_assets = total_current_assets.iloc[ :1]
    total_current_assets = total_current_assets.values
    return total_current_assets

def total_current_assets_old(ticker_bs):
    total_current_assets = ticker_bs
    total_current_assets = pd.DataFrame(total_current_assets)
    total_current_assets = total_current_assets.loc['Total Current Assets']
    total_current_assets = total_current_assets.iloc[1:2]
    total_current_assets = total_current_assets.values
    return total_current_assets

def fixed_assets_new(ticker_bs):
    fixed_assets = ticker_bs
    fixed_assets = pd.DataFrame(fixed_assets)
    fixed_assets = fixed_assets.loc['Property Plant Equipment']
    fixed_assets = fixed_assets.iloc[ :1]
    fixed_assets = fixed_assets.values
    return fixed_assets

def fixed_assets_old(ticker_bs):
    fixed_assets = ticker_bs
    fixed_assets = pd.DataFrame(fixed_assets)
    fixed_assets = fixed_assets.loc['Property Plant Equipment']
    fixed_assets = fixed_assets.iloc[1:2]
    fixed_assets = fixed_assets.values
    return fixed_assets


def total_assets_new(ticker_bs):
    total_assets = ticker_bs
    total_assets = pd.DataFrame(total_assets)
    total_assets = total_assets.loc['Total Assets']
    total_assets = total_assets.iloc[ :1]
    total_assets = total_assets.values
    return total_assets

def total_assets_old(ticker_bs):
    total_assets = ticker_bs
    total_assets = pd.DataFrame(total_assets)
    total_assets = total_assets.loc['Total Assets']
    total_assets = total_assets.iloc[1:2]
    total_assets = total_assets.values
    return total_assets

def total_current_liabilities_new(ticker_bs):
    total_current_liabilities = ticker_bs
    total_current_liabilities = pd.DataFrame(total_current_liabilities)
    total_current_liabilities = total_current_liabilities.loc['Total Current Liabilities']
    total_current_liabilities = total_current_liabilities.iloc[ :1]
    total_current_liabilities = total_current_liabilities.values
    return total_current_liabilities

def total_current_liabilities_old(ticker_bs):
    total_current_liabilities = ticker_bs
    total_current_liabilities = pd.DataFrame(total_current_liabilities)
    total_current_liabilities = total_current_liabilities.loc['Total Current Liabilities']
    total_current_liabilities = total_current_liabilities.iloc[1:2]
    total_current_liabilities = total_current_liabilities.values
    return total_current_liabilities

def total_liabilities_new(ticker_bs):
    total_liabilities = ticker_bs
    total_liabilities = pd.DataFrame(total_liabilities)
    total_liabilities = total_liabilities.loc['Total Liab']
    total_liabilities = total_liabilities.iloc[ :1]
    total_liabilities = total_liabilities.values
    return total_liabilities

def total_liabilities_old(ticker_bs):
    total_liabilities = ticker_bs
    total_liabilities = pd.DataFrame(total_liabilities)
    total_liabilities = total_liabilities.loc['Total Liab']
    total_liabilities = total_liabilities.iloc[1:2]
    total_liabilities = total_liabilities.values
    return total_liabilities

#fungtion cashflow

def operating_cash_flow_new(ticker_cf):
    operating_cash_flow = ticker_cf
    operating_cash_flow = pd.DataFrame(operating_cash_flow)
    operating_cash_flow = operating_cash_flow.loc['Total Cash From Operating Activities']
    operating_cash_flow = operating_cash_flow.iloc[ :1]
    operating_cash_flow = operating_cash_flow.values
    return operating_cash_flow

def operating_cash_flow_old(ticker_cf):
    operating_cash_flow = ticker_cf
    operating_cash_flow = pd.DataFrame(operating_cash_flow)
    operating_cash_flow = operating_cash_flow.loc['Total Cash From Operating Activities']
    operating_cash_flow = operating_cash_flow.iloc[1:2]
    operating_cash_flow = operating_cash_flow.values
    return operating_cash_flow

def investing_cash_flow_new(ticker_cf):
    investing_cash_flow = ticker_cf
    investing_cash_flow = pd.DataFrame(investing_cash_flow)
    investing_cash_flow = investing_cash_flow.loc['Capital Expenditures']
    investing_cash_flow = investing_cash_flow.iloc[ :1]
    investing_cash_flow = investing_cash_flow.values
    return investing_cash_flow

def investing_cash_flow_old(ticker_cf):
    investing_cash_flow = ticker_cf
    investing_cash_flow = pd.DataFrame(investing_cash_flow)
    investing_cash_flow = investing_cash_flow.loc['Capital Expenditures']
    investing_cash_flow = investing_cash_flow.iloc[1:2]
    investing_cash_flow = investing_cash_flow.values
    return investing_cash_flow

def fixed_asset_expenditure_new(ticker_cf):
    fixed_asset_expenditure = ticker_cf
    fixed_asset_expenditure = pd.DataFrame(fixed_asset_expenditure)
    fixed_asset_expenditure = fixed_asset_expenditure.loc['Total Cashflows From Investing Activities']
    fixed_asset_expenditure = fixed_asset_expenditure.iloc[ :1]
    fixed_asset_expenditure = fixed_asset_expenditure.values
    return fixed_asset_expenditure

def fixed_asset_expenditure_old(ticker_cf):
    fixed_asset_expenditure = ticker_cf
    fixed_asset_expenditure = pd.DataFrame(fixed_asset_expenditure)
    fixed_asset_expenditure = fixed_asset_expenditure.loc['Total Cashflows From Investing Activities']
    fixed_asset_expenditure = fixed_asset_expenditure.iloc[1:2]
    fixed_asset_expenditure = fixed_asset_expenditure.values
    return fixed_asset_expenditure

def financing_cash_flow_new(ticker_cf):
    financing_cash_flow = ticker_cf
    financing_cash_flow = pd.DataFrame(financing_cash_flow)
    financing_cash_flow = financing_cash_flow.loc['Total Cash From Financing Activities']
    financing_cash_flow = financing_cash_flow.iloc[ :1]
    financing_cash_flow = financing_cash_flow.values
    return financing_cash_flow

def financing_cash_flow_old(ticker_cf):
    financing_cash_flow = ticker_cf
    financing_cash_flow = pd.DataFrame(financing_cash_flow)
    financing_cash_flow = financing_cash_flow.loc['Total Cash From Financing Activities']
    financing_cash_flow = financing_cash_flow.iloc[1:2]
    financing_cash_flow = financing_cash_flow.values
    return financing_cash_flow

def cash_and_equivalents_beginning_new(ticker_bs):
    cash_and_equivalents_beginning = ticker_bs
    cash_and_equivalents_beginning = pd.DataFrame(cash_and_equivalents_beginning)
    cash_and_equivalents_beginning = cash_and_equivalents_beginning.loc['Cash']
    cash_and_equivalents_beginning = cash_and_equivalents_beginning.iloc[1:2]
    cash_and_equivalents_beginning = cash_and_equivalents_beginning.values
    return cash_and_equivalents_beginning

def cash_and_equivalents_beginning_old(ticker_bs):
    cash_and_equivalents_beginning = ticker_bs
    cash_and_equivalents_beginning = pd.DataFrame(cash_and_equivalents_beginning)
    cash_and_equivalents_beginning = cash_and_equivalents_beginning.loc['Cash']
    cash_and_equivalents_beginning = cash_and_equivalents_beginning.iloc[2:3]
    cash_and_equivalents_beginning = cash_and_equivalents_beginning.values
    return cash_and_equivalents_beginning

def cash_and_equivalents_ending_new(ticker_bs):
    cash_and_equivalents_ending = ticker_bs
    cash_and_equivalents_ending = pd.DataFrame(cash_and_equivalents_ending)
    cash_and_equivalents_ending = cash_and_equivalents_ending.loc['Cash']
    cash_and_equivalents_ending = cash_and_equivalents_ending.iloc[ :1]
    cash_and_equivalents_ending = cash_and_equivalents_ending.values
    return cash_and_equivalents_ending

def cash_and_equivalents_ending_old(ticker_bs):
    cash_and_equivalents_ending = ticker_bs
    cash_and_equivalents_ending = pd.DataFrame(cash_and_equivalents_ending)
    cash_and_equivalents_ending = cash_and_equivalents_ending.loc['Cash']
    cash_and_equivalents_ending = cash_and_equivalents_ending.iloc[1:2]
    cash_and_equivalents_ending = cash_and_equivalents_ending.values
    return cash_and_equivalents_ending

#fungtion income statement
def revenues_new(ticker_is):
    revenues = ticker_is
    revenues = pd.DataFrame(revenues)
    revenues = revenues.loc['Total Revenue']
    revenues = revenues.iloc[ :1]
    revenues = revenues.values
    return revenues

def revenues_old(ticker_is):
    revenues = ticker_is
    revenues = pd.DataFrame(revenues)
    revenues = revenues.loc['Total Revenue']
    revenues = revenues.iloc[1:2]
    revenues = revenues.values
    return revenues

def cost_of_goods_sold_new(ticker_is):
    cost_of_goods_sold = ticker_is
    cost_of_goods_sold = pd.DataFrame(cost_of_goods_sold)
    cost_of_goods_sold = cost_of_goods_sold.loc['Cost Of Revenue']
    cost_of_goods_sold = cost_of_goods_sold.iloc[ :1]
    cost_of_goods_sold = cost_of_goods_sold.values
    return cost_of_goods_sold

def cost_of_goods_sold_old(ticker_is):
    cost_of_goods_sold = ticker_is
    cost_of_goods_sold = pd.DataFrame(cost_of_goods_sold)
    cost_of_goods_sold = cost_of_goods_sold.loc['Cost Of Revenue']
    cost_of_goods_sold = cost_of_goods_sold.iloc[1:2]
    cost_of_goods_sold = cost_of_goods_sold.values
    return cost_of_goods_sold

def gross_income_new(ticker_is):
    gross_income = ticker_is
    gross_income = pd.DataFrame(gross_income)
    gross_income = gross_income.loc['Gross Profit']
    gross_income = gross_income.iloc[ :1]
    gross_income = gross_income.values
    return gross_income

def gross_income_old(ticker_is):
    gross_income = ticker_is
    gross_income = pd.DataFrame(gross_income)
    gross_income = gross_income.loc['Gross Profit']
    gross_income = gross_income.iloc[1:2]
    gross_income = gross_income.values
    return gross_income

def sales_expenses_new(Selling_Marketing_Expense):
    if Selling_Marketing_Expense == []:
        Selling_Marketing_Expense = [0, 0, 0, 0]
        sales_expenses_new = Selling_Marketing_Expense[3]
    elif Selling_Marketing_Expense == 0:
        Selling_Marketing_Expense = [0, 0, 0, 0]
        sales_expenses_new = Selling_Marketing_Expense[3]
    elif Selling_Marketing_Expense == None:
        Selling_Marketing_Expense = [0, 0, 0, 0]
        sales_expenses_new = Selling_Marketing_Expense[3]
    else:
        Selling_Marketing_Expense
        Selling_Marketing_Expense_tabel = pd.DataFrame(Selling_Marketing_Expense)
        Selling_Marketing_Expense_tabel = Selling_Marketing_Expense_tabel['reportedValue']
        Selling_Marketing_Expense_tabel = len(Selling_Marketing_Expense_tabel)
        Selling_Marketing_Expense_tabel = Selling_Marketing_Expense_tabel -1
        if Selling_Marketing_Expense[Selling_Marketing_Expense_tabel] == None:
            Selling_Marketing_Expense = 0
        else:
            sales_expenses_new = Selling_Marketing_Expense[Selling_Marketing_Expense_tabel]['reportedValue']['raw']
    return sales_expenses_new

def sales_expenses_old(Selling_Marketing_Expense):
    if Selling_Marketing_Expense == []:
        Selling_Marketing_Expense = [0, 0, 0, 0]
        sales_expenses_old = Selling_Marketing_Expense[2]
    elif Selling_Marketing_Expense == 0:
        Selling_Marketing_Expense = [0, 0, 0, 0]
        sales_expenses_old = Selling_Marketing_Expense[2]
    elif Selling_Marketing_Expense == None:
        Selling_Marketing_Expense = [0, 0, 0, 0]
        sales_expenses_old = Selling_Marketing_Expense[2]
    else:
        Selling_Marketing_Expense
        Selling_Marketing_Expense_tabel = pd.DataFrame(Selling_Marketing_Expense)
        Selling_Marketing_Expense_tabel = Selling_Marketing_Expense_tabel['reportedValue']
        Selling_Marketing_Expense_tabel = len(Selling_Marketing_Expense_tabel)
        Selling_Marketing_Expense_tabel = Selling_Marketing_Expense_tabel -2
        if Selling_Marketing_Expense[Selling_Marketing_Expense_tabel] == None:
            Selling_Marketing_Expense = 0
        else:
            sales_expenses_old = Selling_Marketing_Expense[Selling_Marketing_Expense_tabel]['reportedValue']['raw']
    return sales_expenses_old

def depreciation_expenses_new(depreciation_expenses): 
    depreciation_expenses_new = []
    # consolidate annual
    for s in depreciation_expenses:
        statement = {}
        for key, val in s.items():
            try:
                statement[key] = val['raw']
            except TypeError:
                continue
            except KeyError:
                continue
        depreciation_expenses_new.append(statement)
    get_depreciation_expenses_new = depreciation_expenses_new[0]['incomeBeforeTax']
    if get_depreciation_expenses_new == []:
        get_depreciation_expenses_new = 0
    else:
        get_depreciation_expenses_new = depreciation_expenses_new[0]['incomeBeforeTax']
    return get_depreciation_expenses_new


def depreciation_expenses_old(depreciation_expenses):
    depreciation_expenses_old = []
    # consolidate annual
    for s in depreciation_expenses:
        statement = {}
        for key, val in s.items():
            try:
                statement[key] = val['raw']
            except TypeError:
                continue
            except KeyError:
                continue
        depreciation_expenses_old.append(statement)
    get_depreciation_expenses_old = depreciation_expenses_old[1]['incomeBeforeTax']
    if get_depreciation_expenses_old == []:
        get_depreciation_expenses_old = 0
    else:
        get_depreciation_expenses_old = depreciation_expenses_old[1]['incomeBeforeTax']
    return get_depreciation_expenses_old


def pretax_income_new(ticker_is):
    pretax_income = ticker_is
    pretax_income = pd.DataFrame(pretax_income)
    pretax_income = pretax_income.loc['Income Tax Expense']
    pretax_income = pretax_income.iloc[ :1]
    pretax_income = pretax_income.values
    if pretax_income < 0:
        pretax_income = pretax_income
    else:
        pretax_income > 0
        pretax_income = -pretax_income
    return pretax_income

def pretax_income_old(ticker_is):
    pretax_income = ticker_is
    pretax_income = pd.DataFrame(pretax_income)
    pretax_income = pretax_income.loc['Income Tax Expense']
    pretax_income = pretax_income.iloc[1:2]
    pretax_income = pretax_income.values
    if pretax_income < 0:
        pretax_income = pretax_income
    else:
        pretax_income > 0
        pretax_income = -pretax_income
    return pretax_income


def after_taxes_income_op_new(after_tax_income_operational):
    if after_tax_income_operational == []:
        after_tax_income_operational = [0, 0, 0, 0]
        after_taxes_income_op_new = after_tax_income_operational[3]
    elif after_tax_income_operational == 0:
        after_tax_income_operational = [0, 0, 0, 0]
        after_taxes_income_op_new = after_tax_income_operational[3]
    elif after_tax_income_operational == None:
        after_tax_income_operational = [0, 0, 0, 0]
        after_taxes_income_op_new = after_tax_income_operational[3]
    else:
        after_tax_income_operational
        if after_tax_income_operational[3] == None:
            after_taxes_income_op_new = 0
        else:
            after_taxes_income_op_new = after_tax_income_operational[3]['reportedValue']['raw']
    return after_taxes_income_op_new

def after_taxes_income_op_old(after_tax_income_operational):
    if after_tax_income_operational == []:
        after_tax_income_operational = [0, 0, 0, 0]
        after_taxes_income_op_new = after_tax_income_operational[3]
    elif after_tax_income_operational == 0:
        after_tax_income_operational = [0, 0, 0, 0]
        after_taxes_income_op_new = after_tax_income_operational[3]
    elif after_tax_income_operational == None:
        after_tax_income_operational = [0, 0, 0, 0]
        after_taxes_income_op_new = after_tax_income_operational[3]
    else:
        after_tax_income_operational
        if after_tax_income_operational[2] == None:
            after_taxes_income_op_new = 0
        else:
            after_taxes_income_op_new = after_tax_income_operational[2]['reportedValue']['raw']
    return after_taxes_income_op_new

def after_tax_income_nonoperational_new(ticker_is):
    after_tax_income_nonoperational = ticker_is
    after_tax_income_nonoperational = pd.DataFrame(after_tax_income_nonoperational)
    after_tax_income_nonoperational = after_tax_income_nonoperational.loc['Net Income From Continuing Ops']
    after_tax_income_nonoperational = after_tax_income_nonoperational.iloc[ :1]
    after_tax_income_nonoperational = after_tax_income_nonoperational.values
    return after_tax_income_nonoperational

def after_tax_income_nonoperational_old(ticker_is):
    after_tax_income_nonoperational = ticker_is
    after_tax_income_nonoperational = pd.DataFrame(after_tax_income_nonoperational)
    after_tax_income_nonoperational = after_tax_income_nonoperational.loc['Net Income From Continuing Ops']
    after_tax_income_nonoperational = after_tax_income_nonoperational.iloc[1:2]
    after_tax_income_nonoperational = after_tax_income_nonoperational.values
    return after_tax_income_nonoperational

def comprehensive_income_EPS_new(comprehensive_income):
    if comprehensive_income == []:
        comprehensive_income = [0, 0, 0, 0]
        comprehensive_income_EPS_new = comprehensive_income[3]
    elif comprehensive_income == 0:
        comprehensive_income = [0, 0, 0, 0]
        comprehensive_income_EPS_new = comprehensive_income[3]
    elif comprehensive_income == None:
        comprehensive_income = [0, 0, 0, 0]
        comprehensive_income_EPS_new = comprehensive_income[3]
    else:
        comprehensive_income
        comprehensive_income_tabel = pd.DataFrame(comprehensive_income)
        comprehensive_income_tabel = comprehensive_income_tabel['reportedValue']
        comprehensive_income_tabel = len(comprehensive_income_tabel)
        comprehensive_income_tabel = comprehensive_income_tabel -1
        if comprehensive_income[comprehensive_income_tabel] == None:
            comprehensive_income_EPS_new = 0
        else:
            comprehensive_income_EPS_new = comprehensive_income[comprehensive_income_tabel]['reportedValue']['raw']
    return comprehensive_income_EPS_new

def comprehensive_income_EPS_old(comprehensive_income):
    if comprehensive_income == []:
        comprehensive_income = [0, 0, 0, 0]
        comprehensive_income_EPS_old = comprehensive_income[2]
    elif comprehensive_income == 0:
        comprehensive_income = [0, 0, 0, 0]
        comprehensive_income_EPS_old = comprehensive_income[2]
    elif comprehensive_income == None:
        comprehensive_income = [0, 0, 0, 0]
        comprehensive_income_EPS_old = comprehensive_income[comprehensive_income_tabel]
    else:
        comprehensive_income
        comprehensive_income_tabel = pd.DataFrame(comprehensive_income)
        comprehensive_income_tabel = comprehensive_income_tabel['reportedValue']
        comprehensive_income_tabel = len(comprehensive_income_tabel)
        comprehensive_income_tabel = comprehensive_income_tabel -2
        if comprehensive_income[2] == None:
            comprehensive_income_EPS_old = 0
        else:
            comprehensive_income_EPS_old = comprehensive_income[comprehensive_income_tabel]['reportedValue']['raw']
    return comprehensive_income_EPS_old


def income_per_share_new(income_per_share):
    if income_per_share == []:
        income_per_share = [0, 0, 0, 0]
        income_per_share_new = income_per_share[3]
    elif income_per_share == 0:
        income_per_share = [0, 0, 0, 0]
        income_per_share_new = income_per_share[3]
    elif income_per_share == None:
        income_per_share = [0, 0, 0, 0]
        income_per_share_new = income_per_share[3]
    else:
        income_per_share
        income_per_share_tabel = pd.DataFrame(income_per_share)
        income_per_share_tabel = income_per_share_tabel['reportedValue']
        income_per_share_tabel = len(income_per_share_tabel)
        income_per_share_tabel = income_per_share_tabel -1
        if income_per_share[income_per_share_tabel] == None:
            income_per_share_new = 0
        else:
            income_per_share_new = income_per_share[income_per_share_tabel]['reportedValue']['raw']
    return income_per_share_new

def income_per_share_old(income_per_share):
    if income_per_share == []:
        income_per_share = [0, 0, 0, 0]
        income_per_share_old = income_per_share[2]
    elif income_per_share == 0:
        income_per_share = [0, 0, 0, 0]
        income_per_share_old = income_per_share[2]
    elif income_per_share == None:
        income_per_share = [0, 0, 0, 0]
        income_per_share_old = income_per_share[2]
    else:
        income_per_share
        income_per_share_tabel = pd.DataFrame(income_per_share)
        income_per_share_tabel = income_per_share_tabel['reportedValue']
        income_per_share_tabel = len(income_per_share_tabel)
        income_per_share_tabel = income_per_share_tabel -2
        if income_per_share[income_per_share_tabel] == None:
            income_per_share_old = 0
        else:
            income_per_share_old = income_per_share[income_per_share_tabel]['reportedValue']['raw']
    return income_per_share_old

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
        fx_rate_effect_on_cash_tabel = pd.DataFrame(fx_rate_effect_on_cash)
        fx_rate_effect_on_cash_tabel = fx_rate_effect_on_cash_tabel['reportedValue']
        fx_rate_effect_on_cash_tabel = len(fx_rate_effect_on_cash_tabel)
        fx_rate_effect_on_cash_tabel = fx_rate_effect_on_cash_tabel -1
        if fx_rate_effect_on_cash[fx_rate_effect_on_cash_tabel] == None:
            fx_rate_effect_on_cash_new = 0
        else:
            fx_rate_effect_on_cash_new = fx_rate_effect_on_cash[fx_rate_effect_on_cash_tabel]['reportedValue']['raw']
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
        fx_rate_effect_on_cash_tabel = pd.DataFrame(fx_rate_effect_on_cash)
        fx_rate_effect_on_cash_tabel = fx_rate_effect_on_cash_tabel['reportedValue']
        fx_rate_effect_on_cash_tabel = len(fx_rate_effect_on_cash_tabel)
        fx_rate_effect_on_cash_tabel = fx_rate_effect_on_cash_tabel -2
        if fx_rate_effect_on_cash[fx_rate_effect_on_cash_tabel] == None:
            fx_rate_effect_on_cash_old = 0
        else:
            fx_rate_effect_on_cash_old = fx_rate_effect_on_cash[fx_rate_effect_on_cash_tabel]['reportedValue']['raw']
    return fx_rate_effect_on_cash_old


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


#variable balence sheet
cash_and_equivalents_new = cash_and_equivalents_new(ticker_bs)
cash_and_equivalents_old = cash_and_equivalents_old(ticker_bs)
total_current_assets_new = total_current_assets_new(ticker_bs)
total_current_assets_old = total_current_assets_old(ticker_bs)
fixed_assets_new = fixed_assets_new(ticker_bs)
fixed_assets_old = fixed_assets_old(ticker_bs)
total_assets_new = total_assets_new(ticker_bs)
total_assets_old = total_assets_old(ticker_bs)
total_non_current_assets_new = total_assets_new - total_current_assets_new
total_non_current_assets_old = total_assets_old - total_current_assets_old
total_current_liabilities_new = total_current_liabilities_new(ticker_bs)
total_current_liabilities_old = total_current_liabilities_old(ticker_bs)
total_liabilities_new = total_liabilities_new(ticker_bs)
total_liabilities_old = total_liabilities_old(ticker_bs)
total_non_current_liabilities_new = total_liabilities_new - total_current_liabilities_new
total_non_current_liabilities_old = total_liabilities_old - total_current_liabilities_old
total_equity_new = total_assets_new - total_liabilities_new
total_equity_old = total_assets_old - total_liabilities_old
account_receivables_third_party_new = [0]
account_receivables_third_party_old = [0]
account_receivables_related_party_new = [0]
account_receivables_related_party_old = [0]

#Variable cash flow
operating_cash_flow_new = operating_cash_flow_new(ticker_cf)
operating_cash_flow_old = operating_cash_flow_old(ticker_cf)
investing_cash_flow_new = investing_cash_flow_new(ticker_cf)
investing_cash_flow_old = investing_cash_flow_old(ticker_cf)
fixed_asset_expenditure_new = fixed_asset_expenditure_new(ticker_cf)
fixed_asset_expenditure_old = fixed_asset_expenditure_old(ticker_cf)
financing_cash_flow_new = financing_cash_flow_new(ticker_cf)
financing_cash_flow_old = financing_cash_flow_old(ticker_cf)
cash_and_equivalents_beginning_new = cash_and_equivalents_beginning_new(ticker_bs)
cash_and_equivalents_beginning_old = cash_and_equivalents_beginning_old(ticker_bs)
fx_rate_effect_on_cash_new = [fx_rate_effect_on_cash_new(fx_rate_effect_on_cash)]
fx_rate_effect_on_cash_old = [fx_rate_effect_on_cash_old(fx_rate_effect_on_cash)]
cash_and_equivalents_ending_new = cash_and_equivalents_ending_new(ticker_bs)
cash_and_equivalents_ending_old = cash_and_equivalents_ending_old(ticker_bs)
cash_and_equivalents_changes_new = cash_and_equivalents_changes_new(cash_and_equivalents_changes)
cash_and_equivalents_changes_old = cash_and_equivalents_changes_old(cash_and_equivalents_changes)

#variable incomestatement
revenues_new = revenues_new(ticker_is)
revenues_old = revenues_old(ticker_is)
cost_of_goods_sold_new = cost_of_goods_sold_new(ticker_is)
cost_of_goods_sold_old = cost_of_goods_sold_old(ticker_is)
gross_income_new = gross_income_new(ticker_is)
gross_income_old = gross_income_old(ticker_is)
sales_expenses_new = [sales_expenses_new(Selling_Marketing_Expense)]
sales_expenses_old = [sales_expenses_old(Selling_Marketing_Expense)]
sales_and_admin_expenses_new = [0]
sales_and_admin_expenses_old = [0]
depreciation_expenses_new = [depreciation_expenses_new(depreciation_expenses)]
depreciation_expenses_old = [depreciation_expenses_old(depreciation_expenses)]
pretax_income_new = pretax_income_new(ticker_is)
pretax_income_old = pretax_income_old(ticker_is)
taxes_expenses_new = after_tax_income_nonoperational_new(ticker_is)
taxes_expenses_old = after_tax_income_nonoperational_old(ticker_is)
after_taxes_income_op_new = [after_taxes_income_op_new(after_tax_income_operational)]
after_taxes_income_op_old = [after_taxes_income_op_old(after_tax_income_operational)]
after_tax_income_nonoperational_new = after_tax_income_nonoperational_new(ticker_is)
after_tax_income_nonoperational_old = after_tax_income_nonoperational_old(ticker_is)
after_tax_income_new = [0]
after_tax_income_old = [0]
comprehensive_income_EPS_new = [comprehensive_income_EPS_new(comprehensive_income)]
comprehensive_income_EPS_old = [comprehensive_income_EPS_old(comprehensive_income)]
income_per_share_new = income_per_share_new(income_per_share)
income_per_share_old = income_per_share_old(income_per_share)

#print("=======data terbaru=======")
tabel_bs_new = pd.DataFrame([[cash_and_equivalents_new, account_receivables_third_party_new, account_receivables_related_party_new, total_current_assets_new, fixed_assets_new, total_non_current_assets_new, total_assets_new, total_current_liabilities_new, total_non_current_liabilities_new, total_equity_new, ticker_kode, year_new]],
            #index=[' '], 
            columns=['cash_and_equivalents', 'account_receivables_third_party', 'account_receivables_related_party', 'total_current_assets', 'fixed_assets', 'total_non_current_assets', 'total_assets', 'total_current_liabilities', 'total_non_current_liabilities', 'total_equity', 'ticker_kode', 'year'])
#print(tabel_bs_new)

#print("=======data satu tahun sebelumnya=======")

tabel_bs_old = pd.DataFrame([[cash_and_equivalents_old, account_receivables_third_party_old, account_receivables_related_party_old, total_current_assets_old, fixed_assets_old, total_non_current_assets_old, total_assets_old, total_current_liabilities_old, total_non_current_liabilities_old, total_equity_old, ticker_kode, year_old]],
            #index=[' '], 
            columns=['cash_and_equivalents', 'account_receivables_third_party', 'account_receivables_related_party', 'total_current_assets', 'fixed_assets', 'total_non_current_assets', 'total_assets', 'total_current_liabilities', 'total_non_current_liabilities', 'total_equity', 'ticker_kode', 'year'])
#print(tabel_bs_old)


#print("=======data terbaru=======")
tabel_cf_new = pd.DataFrame([[operating_cash_flow_new, investing_cash_flow_new, fixed_asset_expenditure_new, financing_cash_flow_new, cash_and_equivalents_beginning_new, fx_rate_effect_on_cash_new, cash_and_equivalents_changes_new, cash_and_equivalents_ending_new, ticker_kode, year_new]],
            #index=[' '], 
            columns=['operating_cash_flow', 'investing_cash_flow', 'fixed_asset_expenditure', 'financing_cash_flow', 'cash_and_equivalents_beginning', 'fx_rate_effect_on_cash', 'cash_and_equivalents_changes', 'cash_and_equivalents_ending', 'ticker_kode', 'year'])
#print(tabel_cf_new)

#print("=======data lama=======")
tabel_cf_old = pd.DataFrame([[operating_cash_flow_old, investing_cash_flow_old, fixed_asset_expenditure_old, financing_cash_flow_old, cash_and_equivalents_beginning_old, fx_rate_effect_on_cash_old, cash_and_equivalents_changes_old, cash_and_equivalents_ending_old, ticker_kode, year_old]],
            #index=[' '], 
            columns=['operating_cash_flow', 'investing_cash_flow', 'fixed_asset_expenditure', 'financing_cash_flow', 'cash_and_equivalents_beginning', 'fx_rate_effect_on_cash', 'cash_and_equivalents_changes', 'cash_and_equivalents_ending', 'ticker_kode', 'year'])
#print(tabel_cf_old)

tabel_is_new = pd.DataFrame([[revenues_new, cost_of_goods_sold_new, gross_income_new, sales_expenses_new, sales_and_admin_expenses_new, depreciation_expenses_new, pretax_income_new, taxes_expenses_new, after_taxes_income_op_new, after_tax_income_nonoperational_new, after_tax_income_new, comprehensive_income_EPS_new, income_per_share_new, ticker_kode, year_new]],
            #index=[' '], 
            columns=['revenues', 'cost_of_goods_sold', 'gross_income', 'sales_expenses', 'sales_and_admin_expenses', 'depreciation_expenses', 'pretax_income', 'tax_expenses', 'after_tax_income_operational', 'after_tax_income_nonoperational', 'after_tax_income', 'comprehensive_income', 'income_per_share', 'ticker_kode', 'year'])
#print(tabel_is_new)

tabel_is_old = pd.DataFrame([[revenues_old, cost_of_goods_sold_old, gross_income_old, sales_expenses_old, sales_and_admin_expenses_old, depreciation_expenses_old, pretax_income_old, taxes_expenses_old, after_taxes_income_op_old, after_tax_income_nonoperational_old, after_tax_income_old, comprehensive_income_EPS_old, income_per_share_old, ticker_kode, year_old]],
            #index=[' '], 
            columns=['revenues', 'cost_of_goods_sold', 'gross_income', 'sales_expenses', 'sales_and_admin_expenses', 'depreciation_expenses', 'pretax_income', 'tax_expenses', 'after_tax_income_operational', 'after_tax_income_nonoperational', 'after_tax_income', 'comprehensive_income', 'income_per_share', 'ticker_kode', 'year'])
#print(tabel_is_old)


'''
erorr

sales_and_admin_expenses
after_tax_income_new
account_receivables_third_party
account_receivables_related_party
'''
#========================= start program ================================

file_name_new = tabel_bs_new, tabel_cf_new, tabel_is_new
file_name_old = tabel_bs_old, tabel_cf_old, tabel_is_old

def get_single_dataframe(year):
    if year == year_new:
        file_name_new == 'file_name-{}'.format(year)
        merge = reduce(partial(pandas.merge, on = ('ticker_kode')), (tabel_bs_new, tabel_cf_new, tabel_is_new))
    else:
        year == year_old
        file_name_old == 'file_name-{}'.format(year)
        merge = reduce(partial(pandas.merge, on = ('ticker_kode')), (tabel_bs_old, tabel_cf_old, tabel_is_old))
    return merge


def get_multiple_dataframes(year, subtrahend):
    """
    Returns multiple periods dataframe into a single dataframe.
    
    Arguments:
        - latest_year = four digits integer to get YYYY format.
        - subtrahend = a quantity or number to be subtracted from another.
    """
    
    # if subtrahend is 1 then total periods will be 2 years
    # example: 2018 - 1 = 2017, so it will be between 2017 and 2018
    # year + 1 is needed because otherwise it only ranges from 2017 to 2017
    dfs = []
    for y in range(year - subtrahend, year + 1):
        dfs.append(get_single_dataframe(year=y))
        
    return pandas.concat(dfs, sort = False).reset_index(drop = True)

baseline_dataframe = get_multiple_dataframes(year_new, 1)

def get_free_cash_flow(year):
    """
    Returns free cash flow dataframe.
    
    Argument:
        - year = four digits integer to get YYYY format.
    """
    
    # select necessary variables
    # sort by ticker code in ascending order
    # reset index
    nwc = baseline_dataframe[[
        'year', 
        'ticker_kode', 
        'total_current_assets', 
        'total_current_liabilities'
    ]].sort_values(by=['ticker_kode'], ascending=True) \
    .reset_index(drop=True)

    # add net working capital as a column
    nwc['net_working_capital'] = nwc['total_current_assets'] - nwc['total_current_liabilities']
    
    # changes in net working capital
    nwc['net_working_capital_delta'] = nwc.groupby('ticker_kode')['net_working_capital'].diff()

    # filter dataframe only in year latest year
    nwc = nwc[nwc['year'] == year][[
        'ticker_kode', 
        'net_working_capital_delta'
    ]].reset_index(drop=True)

    # calculate free cash flow
    fcff = baseline_dataframe[baseline_dataframe['year'] == year][[
        'year', 
        'ticker_kode', 
        'pretax_income', 
        'fixed_assets', 
        'tax_expenses'
    ]]

    fcff = pandas.merge(fcff, nwc, how = 'inner', on = 'ticker_kode').reset_index(drop = True)
    
    fcff['free_cash_flow'] = fcff['pretax_income'] \
    - fcff['fixed_assets'] \
    - fcff['net_working_capital_delta'] \
    - fcff['tax_expenses']
    
    return fcff[['year', 'ticker_kode', 'free_cash_flow']].reset_index(drop=True)

fcff = get_free_cash_flow(year_new)

def get_risk_free_rate(negara):
    url = requests.get('http://www.worldgovernmentbonds.com')
    soup = BeautifulSoup(url.text, 'html.parser')
    table = soup.find('table', class_= 'homeBondTable w3-table w3-white table-padding-custom w3-small font-open-sans table-valign-middle')

    headers = []
    headers2 = []

    for area in table.find_all('tbody'):
        rows = area.find_all('tr')
        for row in rows:
            tabel_n = row.find('td', class_ = 'w3-left-align').text.strip()
            headers.append(tabel_n)
            bond_n = row.find('td', class_ = 'w3-right-align w3-bold').text.strip()
            n = 1
            bond_n = bond_n[:-n]
            bond_n = float(bond_n)
            headers2.append(bond_n)
        gabung= pd.DataFrame(headers2,
            index=headers)
        choice_negara = gabung.loc[negara]
    return choice_negara / 100

risk_free_rate = get_risk_free_rate(negara)

def get_cost_of_equity(beta, market_rate):
    
    
    return risk_free_rate + beta * (market_rate - risk_free_rate)

cost_of_equity = get_cost_of_equity(0.05, 0.05)

def get_wacc(year_new, tax_rate=0.25):

    # get capital structure
    wacc = baseline_dataframe[baseline_dataframe['year'] == year_new][[
        'ticker_kode', 
        'total_assets', 
        'total_equity'
    ]].reset_index(drop = True)
    
    wacc['equity_proportion'] = wacc['total_equity'] / wacc['total_assets']
    wacc['liabilities_proportion'] = 1 - wacc['equity_proportion']
    
    # cost of equity
    re = cost_of_equity
    
    # cost of debt
    rd = 1 - tax_rate
    
    # weighted cost of capital
    wacc['wacc'] = (re * wacc['equity_proportion']) + (rd * (1 - wacc['equity_proportion']))
    wacc = wacc[['ticker_kode', 'wacc']]
    
    return wacc

wacc = get_wacc(year_new, 0.05)
fcff = pandas.merge(fcff, wacc, how = 'inner', on = 'ticker_kode')

def get_fair_value(growth_rate, total_period, year):

    fcff['fpycf'] = fcff['free_cash_flow'] * (1 + (growth_rate * total_period))
    fcff['terminal_value'] = (fcff['fpycf'] * (1 + growth_rate)) / (fcff['wacc'] - growth_rate)
    fcff['enterprise_value'] = fcff['free_cash_flow'] / ((1 + growth_rate) ** total_period)
    fcff['fair_value'] = fcff['terminal_value'] - fcff['enterprise_value']
    
    return fcff[['year', 'ticker_kode', 'fair_value']]

final_dataframe = get_fair_value(0.0001, 1, year_new)

print(final_dataframe)