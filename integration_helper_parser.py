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

networks= {}

def getIntegrationHelper(filename):
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
                networks[adapter_version] = network_name
                if (network_name == "IronSource"):
                    ironSourceSDK = network_name
                    ironSourceSDK_version = adapter_version

#Compares user integration helper logs to the knowledge center change logs
def user_kc_comparison(testname, value, case_items):
    found = False
    for item in case_items:
        if (testname in item) and (value in item):
            found = True
    if found:
        print(value, ": Okay")
        print(item)
        return
    print(value, ": Invalid")
    print(item)

def compare_items(case_items, test_case):
    for testname, value in test_case.items():
        user_kc_comparison(testname, value, case_items)

def main():
    textfile = 'test.txt'
    getIntegrationHelper(textfile)
    print('=' * 25)
    data = changelogparser.getChangeLogs('6.14.0')
    pprint.pprint(data)
    for key, case_items in data.items():
        print('Checking items for ', key)
        print('=' * 25)
        compare_items(case_items, networks)
        print('\n')
main()
    # data = changelogparser.getChangeLogs('6.14.0')
    # pprint.pprint(data)
    # print("The ironSourceSDK version: ")
    # print (ironSourceSDK_version)
    # print("Network Name: ")
    # print (ironSourceSDK)
    # pprint.pprint(networks)
    # print(networks.keys())


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
