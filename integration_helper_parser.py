#Integration Helper Parser
#Edwin Betancourt & ryan :)
from array import *
from pandas.io.html import read_html
from pathlib import Path
from change_log_parser import *
# from sub_process import *
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import subprocess
import urllib
import os, ssl
import pandas as pd
import pprint
import re
import subprocess
# Scraping the networks in the integration logs
# TODO: create function for both behaviors
# class integrationHelperParser:
user_active_networks= {'ad_network':[],'adapter_version':[]}

def get_integration_helper(filename,mediation_sdk_version):
    mediation_sdk_version = mediation_sdk_version
    filename = filename
    file = open(filename,"r")
    #Using regular expressions to detect patterns
    network_info = {'network':'version' }
    network = re.compile("\B([-]{15})\s([a-zA-Z]\w*)")
    adapter = re.compile("(I IntegrationHelper: Adapter) ([0-9.]+\S)( - VERIFIED)")
    changelog_adapter = re.compile("([a-zA-Z])\d")
    changelog_adapter_version = re.compile("([\d.])")
    #creating a network dictionary
    for i, line in enumerate(file):
        # parsing though the logs creating an instance of the network name
            for match in re.finditer(network,line):
                network_name = match.group(2)
            for match in re.finditer(adapter,line):
                adapter_version = match.group(2)
                user_active_networks['ad_network'].append(network_name)
                user_active_networks['adapter_version'].append(adapter_version)
                if (network_name == "IronSource"):
                    ironSourceSDK = network_name
                    ironSourceSDK_version = adapter_version
                    print("IntegrationHelper_temp: ", ironSourceSDK_version)
    # Value Checks
    # print("The ironSourceSDK version: ")
    # print (ironSourceSDK_version)
    # print("Network Name: ")
    # print (ironSourceSDK)
    # print("User Active NetWorks: ")
    # print (user_active_networks)
    # print("ChangeLog networks: ")
    # pprint.pprint(change_log_networks)
    data_df = pd.DataFrame(data)
    app_networks = pd.DataFrame(user_active_networks)
    output = app_networks.merge(data_df[data_df.mediation_sdk_version == mediation_sdk_version], how = 'left') ###define variable for mediation_sdk_version
    output['result'] = ['compatible' if type(x) == str else 'incompatible' for x in output.mediation_sdk_version]
    return output

data = changelogparser().get_change_logs()
# temp_user_logs = get_user_logs()
# print(temp_user_logs)
result = get_integration_helper("recentTest.txt" , "6.18.0")
print(result)

#def main():
#    change_logs = changelogparser.get_change_logs('6.14.0')
#    result = get_integration_helper('test.txt')
#    textfile = 'test.txt'
#    get_integration_helper(textfile)
#    print('=' * 25)
#    change_logs = changelogparser.get_change_logs('6.14.0')
    # breakpoint()
#    for key, change_log_networks in change_logs.items():
#        print('Checking SDK version: ', key)
#        print('-' * 20)
        # print(change_log_networks)
        # breakpoint()
#        compare_items(change_logs, user_active_networks)
#        print('\n')
#main()
     #data = changelogparser.getChangeLogs('6.14.0')
