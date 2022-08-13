#from locale import getpreferredencoding
from weather import getTemp
from crypto import getPrice
from sentiment import getSentiment
from scrape import get_hl, get_poem

print(getSentiment(get_hl()))
print(getSentiment(get_poem()))
print('Price: ' + str(getPrice()))
print('Temp: ' + str(getTemp()) )

def vader(s):
    switch = {
        'very positve' : 1,
        'positve' : 0.5,
        'neutral' : 0,
        'negative' : -0.5,
        'very negative' : -1 
    }
    return switch.get(s, 0)

