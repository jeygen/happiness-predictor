# Weather api

'''
https://www.weatherapi.com/docs/
'''

import requests
import json

#url = "https://weatherapi-com.p.rapidapi.com/future.json"
url = "http://api.weatherapi.com/v1/current.json"
key = "67af799529b74426b9621102221906"

#querystring = {"q":"London","dt":"2022-12-25"}
querystring = {"key": key, "q":"London"}

response = requests.request("GET", url, params=querystring).text # requests.request("method", "url", **kwargs) kwargs ie parameters, header
response = json.loads(response) # converts json to dict 

print(response['current']['feelslike_c'])
