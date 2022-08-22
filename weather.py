#!/usr/bin/env python3
# Weather api

'''
https://www.weatherapi.com/docs/
'''

import requests
import json
from location import get_location
from random import randrange # temp as api not always working 
import os
from dotenv import load_dotenv

load_dotenv()
key = os.environ['WEATHER_API_KEY']
#print(key)

#url = "https://weatherapi-com.p.rapidapi.com/future.json"
url = "http://api.weatherapi.com/v1/current.json"
#key = "67af799529b74426b9621102221906"

def getTemp()->float:
		
	location = get_location()
	location = location['city']

	querystring = {"key": key, "q": location}
	try:
		response = requests.request("GET", url, params=querystring)
		response.raise_for_status()
	except requests.exceptions.HTTPError as err:
		print(err)
		print("Error getting weather")
		return randrange(-20, 40)
		#return 0
	# requests.request("method", "url", **kwargs) kwargs ie parameters, header
	# The Response.text attribute gives you the body of the response, decoded to unicode
	response = requests.request("GET", url, params=querystring).text
	response = json.loads(response) # converts json to dict 

	#print(response['current']['feelslike_c'])

	#return randrange(-20, 41) # delete this for final, api doesnt always work
	return response['current']['feelslike_c']
	
if __name__ == '__main__':
	print(getTemp())