# TAM-QA-Tool

## Objective

To help the TAM team automate components of the QA process by utilizing the data from IntegrationHelperlogs and comparing them to our knowledge center changelogs. This will help us determine whether an adapter is compatible with the SDK in testing.

## Prerequisites

`pip install panda`

`pip install selenium`

`pip install beautifulsoup`

## Getting Started

This tool will eventually be ran via a terminal command, will insert instructions when ready :)

#### Milestone #1

Scrape the changelogs and store them in a dictionary **Done**

- [x] Scrape IntegrationHelperLogs.txt
- [x] Create a dict and store keys,values
- [ ] [*Feature*]Get input(logs) from command line

#### Milestone #2
Using beautifulSoup, scrape the knowledge center changelogs for SDK and network adapter compatibility **In Progress**

- [ ] Scrape KC unsing selenium webdriver
- [x] [*Workaround*]Scrape HTML
- [x] Isolate the compatibility table
- [x] Create a dict with values, keys
- [x] Store values according to ironsource SDK and adapters

##### Blocker: (Fixed)
Looking for a way to lookup by 'data-sdk' version and comparing networks, network_version to integrationHelperParser results. At the moment I'm able to scrape the tables but not by version.
```
<tr data-sdk="6.14.0">
    <td>UnityAds</td>
    <td>4.1.8</td>
</tr>'
```
Actual Results:
```
  ['AdColony', '4.1.6']
  ['AdMob', '4.3.6,4.3.7']
  ['Amazon', '4.3.0']
  ['AppLovin', '4.3.6']
  ['Chartboost', '4.1.6']
  ...
```
##### Blocker:
Was able to get passed the previous blocker, need to find a better way to structure the data at the moment to be able to manupulate. My actual results are stored as strings in my dictionary and makes it more difficult to access and compare

What I'm looking for:
```
{'6.14.0': {
            'AdColony': ['4.1.8'],
            'AdMob':[ '4.3.8', '4.3.9'],
            'Amazon':['4.3.1', '4.3.2']
            }
```
Actual Results:
```
{'Name': 'Amazon', 'Version': '4.3.1, 4.3.2'},
```

#### Milestone #3

- [x] Retrieve values from both ***Milestones 1+2*** and compare values
- [ ] Output results(_email|.txt_)
- [ ] [*Feature*]Create script; user will only need to input integrationHelperLogs .txt file

#### Milestone #4 7/24
- [ ] Beta version done; Fix bugs

## Built With

* python3 [https://www.python.org/download/releases/3.0/]
