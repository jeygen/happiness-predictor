#!/usr/bin/env python3
# Weather api

'''
https://www.weatherapi.com/docs/
'''

import requests
import json
from location import get_location

#url = "https://weatherapi-com.p.rapidapi.com/future.json"
url = "http://api.weatherapi.com/v1/current.json"
key = "67af799529b74426b9621102221906"

def getTemp()->float:
		
	location = get_location()
	# print(location['city'])
	location = location['city']

	querystring = {"key": key, "q": location}

	# requests.request("method", "url", **kwargs) kwargs ie parameters, header
	# The Response.text attribute gives you the body of the response, decoded to unicode
	response = requests.request("GET", url, params=querystring).text
	response = json.loads(response) # converts json to dict 

	#print(response['current']['feelslike_c'])

	return response['current']['feelslike_c']
	
