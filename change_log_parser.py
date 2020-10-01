from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.chrome.service as service
import urllib
import os, ssl
from pandas.io.html import read_html
import pprint
import time
import pandas as pd

class changelogparser:
    def __init__(self):
        pass
    def get_change_logs(self, user_os):
        #Will open browser to retrive HTML
        driver = webdriver.Chrome()
        if user_os == 'a':
            driver.get('https://developers.ironsrc.com/ironsource-mobile/android/mediation-networks-android')
        else:
            driver.get('https://developers.ironsrc.com/ironsource-mobile/ios/mediation-networks-ios/')
        try:
            el = WebDriverWait(driver, 10).until(lambda d: d.find_element_by_tag_name("td"))
        finally:
            html = driver.page_source
            driver.quit()
        print('Retrieved mediation networks page')
        # html = driver.page_source
        soup = BeautifulSoup(html, "lxml")
        all_tables = soup.find_all('tr')
        # single_tables = soup.find_all('td')
        data = {'mediation_sdk_version':[],'ad_network':[],'adapter_version':[]}
        for coll in all_tables:
            for keys in coll.attrs.keys():
                # breakpoint()
                if keys.startswith('data-'):
                    rows = coll.find_all('td')
                    adapter_name = rows[0].text
                    # print('adapter_name:', adapter_name)
                    adapter_version = rows[1].text
                    # print('adapter_version:', adapter_version)
                    for i in adapter_version.split(', '):
                        data['mediation_sdk_version'].append(coll[keys])
                        data['ad_network'].append(adapter_name)
                        data['adapter_version'].append(i)
        data['os'] = ['TBD' for x in data['mediation_sdk_version']]
        pd.DataFrame(data)
        # print("Printing Data: ")
        # pprint.pprint(data)
        return data
    #x = "foo"
    #changeLog_dict = get_change_logs(x)
