given = '6.15.0'
testCase = {
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
 '6.15.0': [{'4.1.8','AdColony'},
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

for items in data.values():

    for given,tests in zip(items,testCase.values()):
        print(given,' : ',tests)
        if tests in given:
            print(test , ": Okay")
        else:
            print(testCase.keys() , ": Invalid")
