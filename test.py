#Own reference
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import urllib
import os, ssl
import pandas as pd
from pandas.io.html import read_html

page = open('knowledge_center.html')
soup = BeautifulSoup(page, 'html.parser')

all_tables = soup.find_all('tr')
single_tables = soup.find_all('td')


#looping through all <tr> tags
for item in all_tables:
    for key in item.attrs.keys():
        if key.startswith('data-'):
            if (item[key] =='6.16.1'):
                print(item[key])
                #print(key, item.attrs[key])
                #print(key, item.attrs.get(key))
                rows = item.find_all('td')
                adapter_name = rows[0].text
                print('     Name:', adapter_name)
                adapter_version = rows[1].text
                print('  Version:', adapter_version)



# dfs = pd.read_html('knowledge_center.html', header=0)
# for df in dfs:
#     print(df)
#
# page = 'knowledge_center.html'

#Gets the Compatibility tables
# TODO: Find a way to retrieve <td data-sdk=[version]
# Output:
#      Ad Network Adapter Version
# 0      AdColony           4.1.6
# 1         AdMob      4.3.64.3.7
# 2        Amazon           4.3.0
# 3      AppLovin           4.3.6
# 4    Chartboost           4.1.6
# ..          ...             ...
# 145   Mintegral           4.3.1
# 146      Pangle           4.1.3
# 147      Tapjoy          4.1.10
# 148    UnityAds           4.3.1
#
# 149      Vungle           4.3.0
#
# [150 rows x 2 columns]

# tables = read_html(page)
# version_compat = tables[1]
# print(version_compat)

#alternate way to retrieve table
# table = soup.find('table')
# table_rows = soup.find_all('tr')

# for item in all_tables:
#     #getting the sdk version and assigning a key
#     for key in item.attrs.keys():
#         if key.startswith('data-sdk'):
# TODO: Same as other attempt, figure out how to search by <tr> content
# Output:
# ['AdColony', '4.1.6']
# ['AdMob', '4.3.6,4.3.7']
# ['Amazon', '4.3.0']
# ['AppLovin', '4.3.6']
# ['Chartboost', '4.1.6']

# for tr in table_rows:
#     for key in tr.attrs.keys():
#         if key.startswith('data-sdk'):
#             td = tr.find_all('td')
#             row = [i.text for i in td]
#             print(row)
