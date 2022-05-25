from calendar import c
from codecs import ignore_errors
from lib2to3.pgen2.pgen import DFAState
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




tabel_1 = pd.DataFrame([[222, 345, 223, 'AAA', 2020]],
        columns=['A', 'B', 'C', 'kode', 'tahun'])

tabel_2 = pd.DataFrame([[233, 232, 123, 'AAA', 2020]],
        columns=['D', 'E', 'F', 'kode', 'tahun'])




file_name = tabel_1, tabel_2
dfs = []
for i in file_name:
    dfs.append(file_name)

aaa = reduce(lambda left,right: pd.merge(left,right,on=('kode','tahun')), (tabel_1,tabel_2))
bbb = reduce(partial(pandas.merge, on = ('kode','tahun')), (tabel_1, tabel_2))
ccc = reduce(partial(pandas.merge, on = ('kode','tahun')), [dfs])
print(ccc)
print("="*70)
print(bbb)


'''
tabel1 = pd.DataFrame([[222, 345, 223, 'AAA', 2020]],
        columns=['A', 'B', 'C', 'kode', 'tahun'])

tabel_2 = pd.DataFrame([[233, 232, 123, 'AAA', 2020]],
        columns=['D', 'E', 'F', 'kode', 'tahun'])

year = 2020
tabel1 == 'tabel_1{}'.format(year)
new = tabel1

tabel_2 = 'tabel_2{}'
tabel_2 = tabel_2.format(year)

def get_year(year):
    if 'tabel_1{}'.format(year):
        new == 'tabel_1{}'.format(year)
    return new

print(get_year(2020))

'''