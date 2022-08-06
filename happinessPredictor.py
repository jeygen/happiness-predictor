#from locale import getpreferredencoding
from weather import getTemp
from crypto import getPrice
from sentiment import getSentiment

print(getSentiment("bob is very bad."))
print('Price: ' + str(getPrice()))
print('Temp: ' + str(getTemp()) )

