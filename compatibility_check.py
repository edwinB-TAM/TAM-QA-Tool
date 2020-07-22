import re
from array import *
from changeLogParser import *
from integrationHelperParser import *
#
textfile = input("Enter file name: ")
# print(getintegrationHelper(textfile))
# print(getChangeLogs)

def main():
    ironsource_version = getintegrationHelper.ironSourceSDK_version
    print (ironsource_version)


# def compatibility_check(IronSourceSDK):
#     # temp_adapter = adapter_data
#     # integrationHelperLogs(adapters, ironSourceSDK) --> changeLogs(adapters,ironSourceSDK)
#
#     ironSource = IronSourceSDK
#
#     for ironSource in changeLogParser()
