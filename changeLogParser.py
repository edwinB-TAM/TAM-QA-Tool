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
# table = soup.find('table')
# table_rows = soup.find_all('tr')
# for tr in table_rows:
#     #Looking up the network as a key, versions as values
#     for key in tr.attrs.keys():
#         if key.startswith('data-sdk'):
#             td = tr.find_all('td')
#             row = [i.text for i in td]
#             print(row)


#Gets the Compatibility tables
# TODO: Find a way to retrieve <td data-sdk=[version]

#alternate way to retrieve table
# #looping through all <tr> tags
#looping through all <tr> tags
for item in all_tables:
    for key in item.attrs.keys():
        if key.startswith('data-'):
            #'6.16.1' is a placeholder for a dynamic ironsource sdk versions
            # will pass ironSourceSDK version from integrationHelperPaser
            if (item[key] =='6.16.1'):
                print(item[key])
                rows = item.find_all('td')
                adapter_name = rows[0].text
                print('adapter_name:', adapter_name)
                adapter_version = rows[1].text
                print('adapter_version:', adapter_version)

# Output:
# 6.16.1
#      Name: AdColony
#   Version: 4.3.0
# 6.16.1
#      Name: AdMob
#
#   Version: 4.3.10
# 6.16.1
#      Name: Amazon
#   Version: 4.3.3
# 6.16.1
#      Name: AppLovin
#   Version: 4.3.10
# 6.16.1
#      Name: Chartboost
#   Version: 4.3.0
# 6.16.1
#      Name: Facebook
#   Version: 4.3.14
# 6.16.1
#      Name: Fyber
#   Version: 4.3.4
# 6.16.1
#      Name: HyprMx
#   Version: 4.1.3
# 6.16.1
#      Name: InMobi
#   Version: 4.3.3
# 6.16.1
#      Name: Maio
#   Version: 4.1.4
# 6.16.1
#      Name: Mintegral
#   Version: 4.3.1
# 6.16.1
#      Name: Pangle
#   Version: 4.1.3
# 6.16.1
#      Name: Tapjoy
#   Version: 4.1.10
