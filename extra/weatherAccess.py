#if you're using VS code just make sure that you're not using 3.13 not 3.14
# conda activate pythonTest

#pip > npm (package manager for nodes—used for node.js)
#pip is basically a standard tool that gets installed with python

import requests

#city argument
#this can also be dynamic
city="Montreal"

#sabine's API key
api_key = "2ba267fc5ab5b4c99201b8efab509d99" 

#it's expecting that the api key is part of the URL
url_with_city ="http://api.openweathermap.org/data/2.5/weather?q=" +city

# we need API key to use APPID
url_to_send = url_with_city + "&APPID=" + api_key

#request get method > there are different action words that you use with http, one of them being get
response = requests.get(url_to_send)

data = response.json() 

print(data)