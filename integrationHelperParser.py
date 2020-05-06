#Integration Helper Parser
#Edwin Betancourt

import re
from array import *
#Using regular expressions to detect patterns

network_info = {'network':'version' }
network = re.compile("\B([-]{15})\s([a-zA-Z]\w*)")
adapter = re.compile("(I/IntegrationHelper: Adapter) ([0-9.]+\S)( - VERIFIED)")
changelog_adapter = re.compile("([a-zA-Z])\d")
changelog_adapter_version = re.compile("([\d.])")
textfile = input("Enter file name: ")


#creating an empty network dictionary
networks= {}

# Scraping the networks in the integration logs
# TODO: create function for both behaviors
def integrationHelperPaser(filename):
    data = open(filename,"r")
    for i, line in enumerate(data):
        # parsing though the logs creating an instance of the network name
            for match in re.finditer(network,line):
                network_name = match.group(2)
                #print (network_name)
            for match in re.finditer(adapter,line):
                # creating an array with the [network,adapter_version]
                adapter_version = match.group(2)
                #print (adapter_version)
                networks[network_name] = adapter_version
                #network_adapter = [network_name,adapter_version]
                #if (network_adapter == ['IronSource', re.compile("[0-9.]+\S")]):
                # if (network_adapter == ['IronSource', "6.14.0"]):
                #     ironSourceSDK = network_adapter
                #     print (ironSourceSDK)
                # else:
                print(networks)


integrationHelperPaser(textfile)


#Adapter Compatibility Scarping
# for i, line in enumerate(open('test_changelog.txt')):
#     for match in re.finditer(changelog_adapter,line):
#         #adapter_missing = match.group(1)
#         changelog_network_name = match.group(1)
#         print (changelog_network_name)
#     for match in re.finditer(changelog_adapter_version,line):
#         changelog_adapter_version = match.group(1)
#         print (changelog_adapter_version)
#         #creating an array with the network and adapter version
#         changelog_network_adapter = [changelog_network_name,changelog_adapter_version]
#         #if (network_adapter == ['IronSource', re.compile("[0-9.]+\S")]):
#         if (changelog_network_adapter == ['IronSource', "6.14.0"]):
#             ironSourceSDK = changelog_network_adapter
#             print (ironSourceSDK)
#         else:
#             print (changelog_network_adapter)
