from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import urllib
import os, ssl
import pandas as pd
from pandas.io.html import read_html

page = open('knowledge_center.html')
soup = BeautifulSoup(page, 'html.parser')

# all_tables = soup.find_all('tr')
# single_tables = soup.find_all('td')
#
#
# #looping through all <tr> tags
# for item in all_tables:
#     #getting the sdk version and assigning a key
#     for key in item.attrs.keys():
#         if key.startswith('data-sdk'):
#             # print(key, item[key])
#             # print(key, item.attrs[key])
#             print("Attrs: "+ key, item.attrs.values())
#             # print(key, item.attrs.values())
#             # for value in single_tables:
#             #     print("Key: ")
#             #     print(value)

# dfs = pd.read_html('knowledge_center.html', header=0)
# for df in dfs:
#     print(df)

page = 'knowledge_center.html'

tables = read_html(page)
print(tables[1])
# with open('knowledge_center.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')
#
# table = soup.find('table')
# table_rows = soup.find_all('tr')
#
# for tr in table_rows:
#     td = tr.find_all('td')
#     row = [i.text for i in td]
    # print(row)
