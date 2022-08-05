import json
import requests


api_url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
response = requests.get(api_url).text
response = json.loads(response)

def getPrice():
	return response["bitcoin"]["usd"]


#print(f"Bitcoin price is currently {price} USD.")
