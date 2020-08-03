#Integration Helper Parser
#Edwin Betancourt
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

user_active_networks= {}

def get_integration_helper(filename):
    file = open(filename,"r")
    #Using regular expressions to detect patterns
    network_info = {'network':'version' }
    network = re.compile("\B([-]{15})\s([a-zA-Z]\w*)")
    adapter = re.compile("(I/IntegrationHelper: Adapter) ([0-9.]+\S)( - VERIFIED)")
    changelog_adapter = re.compile("([a-zA-Z])\d")
    changelog_adapter_version = re.compile("([\d.])")

    #creating a network dictionary
    for i, line in enumerate(file):
        # parsing though the logs creating an instance of the network name
            for match in re.finditer(network,line):
                network_name = match.group(2)
            for match in re.finditer(adapter,line):
                adapter_version = match.group(2)
                user_active_networks[adapter_version] = network_name
                if (network_name == "IronSource"):
                    ironSourceSDK = network_name
                    ironSourceSDK_version = adapter_version

    change_log_networks = changelogparser.get_change_logs('6.14.0')
    print('=' * 25)
    print(user_active_networks)
    # Value Checks
    # print("The ironSourceSDK version: ")
    # print (ironSourceSDK_version)
    # print("Network Name: ")
    # print (ironSourceSDK)
    # print("User Active NetWorks: ")
    # print (user_active_networks)
    # print("ChangeLog networks: ")
    # pprint.pprint(change_log_networks)



#Compares user integration helper logs to the knowledge center change logs
def user_kc_comparison(user_versions, user_networks, change_log_networks):
    # breakpoint()
    found = False
    for change_log_version in change_log_networks.keys():
        # print('Items: ', change_log_version)
        # print('change_log_networks: ', change_log_networks.keys())
        if (user_versions in change_log_version) and (user_networks in change_log_version):
            # print("here")
            # print('user_versions: ', user_versions)
            # print('change_log_version: ', change_log_version)
            # print('user_networks: ', user_networks)

            found = True
    if found:
        # print("here")
        # print('user_versions: ', user_versions)
        # print('change_log_version: ', change_log_version)
        # print('user_networks: ', user_networks)
        #doesnt look to iterate through all networks
        print(value, ": Compatible")
        return

    print(user_networks, ": Invalid")
    # print('user_versions: ', user_versions)
    # print('change_log_version: ', change_log_version)
    # print('user_networks: ', user_networks)

def compare_items(change_log_networks, user_active_networks):
    # breakpoint()
    for user_versions, user_networks in user_active_networks.items():
        # if (ironSourceSDK_version == change_log_version):
        user_kc_comparison(user_versions,user_networks,change_log_networks)

def main():
    textfile = 'test.txt'
    get_integration_helper(textfile)
    print('=' * 25)
    change_logs = changelogparser.get_change_logs('6.14.0')
    # breakpoint()
    for key, change_log_networks in change_logs.items():
        print('Checking SDK version: ', key)
        print('-' * 20)
        # print(change_log_networks)
        # breakpoint()
        compare_items(change_logs, user_active_networks)
        print('\n')
main()
    # data = changelogparser.getChangeLogs('6.14.0')



    # getDictionary(ironSourceSDK_version)
    # comparingDictionary(networks)
# textfile = input("Enter file name: ")

# def compatibility_check(networks,ironSourceSDK_version):
#     temp_networks = networks
#     temp_ironsourceSDK_version = ironSourceSDK_version
#     print (temp_networks)
#     print (temp_ironsourceSDK_version)

# compatibility_check(networks, ironSourceSDK_version)
# integrationHelperPaser(textfile)
#
# def getDictionary(ironsrc_version):
#     ironsrcSDK_version = ironsrc_version
# #     getChangeLogs(ironsrcSDK_version)
