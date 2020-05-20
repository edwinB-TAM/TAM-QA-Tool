from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import urllib
import os, ssl
import pandas as pd
from pandas.io.html import read_html

# TODO: Same as other attempt, figure out how to search by <tr> content
# Output:
# ['AdColony', '4.1.6']
# ['AdMob', '4.3.6,4.3.7']
# ['Amazon', '4.3.0']
# ['AppLovin', '4.3.6']
# ['Chartboost', '4.1.6']
# ...
#Creates an array, organzing data by [network, adapter_version]
table = soup.find('table')
table_rows = soup.find_all('tr')
for tr in table_rows:
    #Looking up the network as a key, versions as values
    for key in tr.attrs.keys():
        if key.startswith('data-sdk'):
            td = tr.find_all('td')
            row = [i.text for i in td]
            print(row)


#Gets the Compatibility tables
# TODO: Find a way to retrieve <td data-sdk=[version]

#alternate way to retrieve table
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
