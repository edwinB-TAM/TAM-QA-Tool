#parsing the knowledgecenter changelog_adapters
#Edwin

network_info = {'network':'version' }
ironsource_network = re.compile("data-sdk="[0-9.]+[]"")
changelog_adapter = re.compile("([a-zA-Z])\d")
changelog_adapter_version = re.compile("([\d.])")
textfile = input("Enter file name: ")
