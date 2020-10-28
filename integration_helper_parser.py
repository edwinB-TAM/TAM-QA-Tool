#Integration Helper Parser
#Edwin Betancourt & ryan :)
from get_user_logs import *
from change_log_parser import *
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import urllib
import os, ssl
import pandas as pd
from pandas.io.html import read_html
import pprint
import re
from array import *
# Scraping the networks in the integration logs
# TODO: create function for both behaviors
# class integrationHelperParser:
user_active_networks= {'ad_network':[],'adapter_version':[]}

def get_integration_helper(filename, user_os):
# def get_integration_helper(filename):
    # mediation_sdk_version = mediation_sdk_version
    filename = filename
    filename = open(filename,"r")
    #Using regular expressions to detect patterns
    network_info = {'network':'version' }
    # User Network info
    network = re.compile("\B([-]{15})\s([a-zA-Z]\w*)")
    if user_os == 'a':
        # Android integration helper regex
        adapter = re.compile("(I IntegrationHelper: Adapter) ([0-9.]+\S)( - VERIFIED)")
    if user_os == 'i':
        # iOS integration helper regex
        adapter = re.compile("(Adapter - Version )([0-9.]+\S)( - VERIFIED)")
    #creating a network dictionary
    for i, line in enumerate(filename):
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
    data_df = pd.DataFrame(data)
    app_networks = pd.DataFrame(user_active_networks)
    output = app_networks.merge(data_df[data_df.mediation_sdk_version == ironSourceSDK_version], how = 'left') ###define variable for mediation_sdk_version
    output['result'] = ['compatible' if type(x) == str else 'incompatible' for x in output.mediation_sdk_version]
    # print("App networks", app_networks)
    return output



user_os = input("Select (a)Android | (i)iOS: ")
data = changelogparser().get_change_logs(user_os)
if user_os == 'a':
    temp_user_logs = get_user_android_logs()
elif user_os == 'i':
    temp_user_logs = get_user_ios_logs()
else:
    print("Invalid platform selection, try again!")
# temp_user_logs = get_user_logs()
result = get_integration_helper(temp_user_logs, user_os)
# result = get_integration_helper('ios.txt')
print(result)
