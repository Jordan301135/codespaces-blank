# API = Application Programming Interface

# are methods (functions) that allow computer programs to share
# data between each other over the internet/ a network.

import requests
# modules are style of code

# countryData = requests.get(" https://restcountries.com/v3.1/all?fields=name,capital,currencies")


# JSON - JavaScript Object Notation 
# this a object structured for computer and people to easily read
# sort data.



# print(countryData.json())

SouthernCountry = requests.get("https://restcountries.com/v3.1/name/Guyana")

print(SouthernCountry.json())