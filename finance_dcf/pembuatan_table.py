from calendar import c
import pandas as pd
import yfinance as yf
import datetime

ticker_kode = "ABBA.JK"
ticker = yf.Ticker(ticker_kode)
#year = datetime.datetime.now()
#year = year.year

ticker_bs = ticker.balance_sheet
ticker_cf = ticker.cashflow
print(ticker_cf)
year_new = ticker_bs.columns[0]
year_new = year_new.year
year_old = year_new - 1



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
fx_rate_effect_on_cash_new = 0
fx_rate_effect_on_cash_old = 0
cash_and_equivalents_changes_new = 0
cash_and_equivalents_changes_old = 0
cash_and_equivalents_ending_new = cash_and_equivalents_ending_new(ticker_bs)
cash_and_equivalents_ending_old = cash_and_equivalents_ending_old(ticker_bs)



'''
print("=======data terbaru=======")
tabel_bs_new = pd.DataFrame([[cash_and_equivalents_new, 0, 0, total_current_assets_new, fixed_assets_new, total_non_current_assets_new, total_assets_new, total_current_liabilities_new, total_non_current_liabilities_new, total_equity_new, ticker_kode, year_new]],
            #index=[' '], 
            columns=['cash_and_equivalents', 'account_receivables_third_party', 'account_receivables_related_party', 'total_current_assets', 'fixed_assets', 'total_non_current_assets', 'total_assets', 'total_current_liabilities', 'total_non_current_liabilities', 'total_equity', 'ticker_kode', 'year'])
print(tabel_bs_new)

print("=======data satu tahun sebelumnya=======")

tabel_bs_old = pd.DataFrame([[cash_and_equivalents_old, 0, 0, total_current_assets_old, fixed_assets_old, total_non_current_assets_old, total_assets_old, total_current_liabilities_old, total_non_current_liabilities_old, total_equity_old, ticker_kode, year_old]],
            #index=[' '], 
            columns=['cash_and_equivalents', 'account_receivables_third_party', 'account_receivables_related_party', 'total_current_assets', 'fixed_assets', 'total_non_current_assets', 'total_assets', 'total_current_liabilities', 'total_non_current_liabilities', 'total_equity', 'ticker_kode', 'year'])
print(tabel_bs_old)
'''

print("=======data terbaru=======")
tabel_cf_new = pd.DataFrame([[operating_cash_flow_new, investing_cash_flow_new, fixed_asset_expenditure_new, financing_cash_flow_new, cash_and_equivalents_beginning_new, fx_rate_effect_on_cash_new, cash_and_equivalents_changes_new, cash_and_equivalents_ending_new, ticker_kode, year_new]],
            #index=[' '], 
            columns=['operating_cash_flow', 'investing_cash_flow', 'fixed_asset_expenditure', 'financing_cash_flow', 'cash_and_equivalents_beginning', 'fx_rate_effect_on_cash', 'cash_and_equivalents_changes', 'cash_and_equivalents_ending', 'ticker_kode', 'year'])
print(tabel_cf_new)

print("=======data lama=======")
tabel_cf_old = pd.DataFrame([[operating_cash_flow_old, investing_cash_flow_old, fixed_asset_expenditure_old, financing_cash_flow_old, cash_and_equivalents_beginning_old, fx_rate_effect_on_cash_old, cash_and_equivalents_changes_old, cash_and_equivalents_ending_old, ticker_kode, year_old]],
            #index=[' '], 
            columns=['operating_cash_flow', 'investing_cash_flow', 'fixed_asset_expenditure', 'financing_cash_flow', 'cash_and_equivalents_beginning', 'fx_rate_effect_on_cash', 'cash_and_equivalents_changes', 'cash_and_equivalents_ending', 'ticker_kode', 'year'])
print(tabel_cf_old)
