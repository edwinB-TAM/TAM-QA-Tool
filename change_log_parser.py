from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import urllib
import os, ssl
import pandas as pd
from pandas.io.html import read_html
import pprint
from __main__ import *

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

#alternate way to retrieve table
# #looping through all <tr> tags
#looping through all <tr> tags

class changelogparser:
    def getChangeLogs(ironsrc_version):
        page = open('knowledge_center.html')
        soup = BeautifulSoup(page, 'html.parser')

        all_tables = soup.find_all('tr')
        single_tables = soup.find_all('td')
        data = {}

        temp_version  = ironsrc_version
        for coll in all_tables:
            for keys in coll.attrs.keys():
                if keys.startswith('data-'):
                    #'6.16.1' is a placeholder for a dynamic ironsource sdk versions
                    # will pass ironSourceSDK version from integrationHelperPaser
                # if (coll[keys] =='6.16.1'):
                    # print(coll[keys])
                    rows = coll.find_all('td')
                    adapter_name = rows[0].text
                    # print('adapter_name:', adapter_name)
                    adapter_version = rows[1].text
                    # print('adapter_version:', adapter_version)
                    if coll[keys] not in data:
                        # print("Coll is here: ")
                        # print(coll)
                        data[ coll[keys] ] = []
                    # data[ coll[keys] ].append({
                    #     'Name': rows[0].text,
                    #     'Version': rows[1].text,
                    data[ coll[keys] ].append({
                        rows[0].text,rows[1].text,
                    }
                    )

        # pprint.pprint(data)
        return data
        #
        # pprint.pprint(data)

    # x = "6.10.0"
    # changeLog_dict = getChangeLogs(x)
