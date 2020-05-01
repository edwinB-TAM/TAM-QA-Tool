#Integration Helper Parser
#Edwin Betancourt

import re
#Using regular expressions to detect patterns
network = re.compile("\B([-]{15})\s([a-zA-Z]\w*)")
adapter = re.compile("(I/IntegrationHelper: Adapter) ([0-9.]+\S)( - VERIFIED)")
changelog_adapter = re.compile("([a-zA-Z])\")
changelog_adapter_version = re.compile("([\d.])")
#network_name = pattern.sub('\1',(open()'test.txt')

Scraping the networks in the integration logs
for i, line in enumerate(open('test.txt')):
    for match in re.finditer(network,line):
        #adapter_missing = match.group(1)
        network_name = match.group(2)
        #print (network_name)
    for match in re.finditer(adapter,line):
        adapter_version = match.group(2)
        #print (adapter_version)
        #creating an array with the network and adapter version
        network_adapter = [network_name,adapter_version]
        #if (network_adapter == ['IronSource', re.compile("[0-9.]+\S")]):
        if (network_adapter == ['IronSource', "6.14.0"]):
            ironSourceSDK = network_adapter
            print (ironSourceSDK)
        else:
            print (network_adapter)
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
