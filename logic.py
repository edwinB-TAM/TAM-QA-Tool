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
from __main__ import *
# from changeLogParser import *
NetworkName = 0
ironSourceSDK_version = '6.15.0'
user_logs = {'4.1.1': 'Mintegral',
 '4.1.8': 'AdColony',
 '4.1.7': 'UnityAds',
 '4.3.9': 'AdMob',
 '4.3.7': 'AppLovin',
 '4.3.9': 'Facebook',
 '6.14.0': 'IronSource'}

data ={'6.14.0': [{'AdColony', '4.1.8'},
            {'AdMob', '4.3.8', '4.3.9'},
            {'4.3.1', '4.3.2', 'Amazon'},
            {'4.3.8', '4.3.9', 'AppLovin'},
            {'4.1.7', 'Chartboost'},
            {'Facebook', '4.3.10', '4.3.11', '4.3.9'},
            {'4.3.2', 'Fyber'},
            {'HyprMx', '4.1.3'},
            {'4.3.3', 'InMobi'},
            {'Maio', '4.1.4'},
            {'Mintegral', '4.1.3', '4.1.4'},
            {'4.1.2', 'Pangle'},
            {'Tapjoy', '4.1.9'},
            {'UnityAds', '4.1.8'},
            {'Vungle', '4.1.9'}],
 '6.15.0': [{'AdColony', '4.1.8'},
            {'4.3.9', 'AdMob'},
            {'4.3.2', 'Amazon'},
            {'4.3.9', 'AppLovin'},
            {'4.1.7', 'Chartboost'},
            {'Facebook', '4.3.12'},
            {'Fyber', '4.3.2', '4.3.3'},
            {'HyprMx', '4.1.3'},
            {'4.3.3', 'InMobi'},
            {'Maio', '4.1.4'},
            {'Mintegral', '4.1.4'},
            {'4.1.2', 'Pangle'},
            {'Tapjoy', '4.1.9'},
            {'UnityAds', '4.1.8'},
            {'Vungle', '4.1.9'}]}

def check_test_ok(testname, value, case_items):
    found = False
    for item in case_items:
        if (testname in item) and (value in item):
            found = True
    if found:
        print(testname, ": Okay")
    else:
        print(item, ": Invalid")

def check_items(case_items, test_case):
    for testname, value in test_case.items():
        print('='*10)
        print(testname)
        print(value)
        check_test_ok(testname, value, case_items)

for key, case_items in data.items():
    print('Checking items for ', key    )
    print('=' * 25)
    # print(case_items)
    check_items(case_items, user_logs)
    print('\n')


# for items in change_logs.values():
#
#     for given,tests in zip(items,testCase.values()):
#         print(given,' : ',tests)
#         if tests in given:
#             print(testCase.keys() , ": Okay")
#         else:
#             print(testCase.keys() , ": Invalid")

# for items in change_logs.values():
#
#     for ironSourceSDK_version,tests in zip(items,user_logs.values()):
#         print(ironSourceSDK_version,' : ',tests)
#         if tests in ironSourceSDK_version:
#             print(user_logs.keys() , ": Okay")
#         else:
#             print(user_logs.keys() , ": Invalid")
