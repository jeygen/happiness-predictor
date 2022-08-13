#from locale import getpreferredencoding
from weather import getTemp 
from crypto import getPrice
from sentiment import getSentiment 
from scrape import get_hl, get_poem

print(getSentiment(get_hl()))
print(getSentiment(get_poem()))
print('Price: ' + str(getPrice()))
print('Temp: ' + str(getTemp()) )

def sentiToValue(s):
    switch = {
        'very positve' : 1,
    'positve' : 0.5,
        'neutral' : 0,
        'negative' : -0.5,
        'very negative' : -1 
    }
    return switch.get(s, 0)

def cryptoToValue(p):
    value = p * 5e-05 - 1
    return 1 if value > 1 else value

def weatherToValue(t):
    if t > 36:
        return -1
    elif t > 30:
        return 0.8
    elif t > 26:
        return 0.9
    elif t > 21:
        return 1 
    elif t > 17:
        return 0.9 
    elif t > 15:
        return 0.8 
    elif t > 11:
        return 0.7 
    elif t > 6:
        return 0.2 
    elif t > 0:
        return 0.1 
    elif t > -5:
        return -0.3 
    elif t > -10:
        return -0.6
    elif t > -15:
        return -0.8
    elif t > -20: 
        return -0.9
    else:
        return -1 

def happinessAlgo():
    happiness = sentiToValue(get_hl()) + sentiToValue(get_poem()) + 2*cryptoToValue(getPrice()) + 2*weatherToValue(getTemp()) 
    happiness /= 6

