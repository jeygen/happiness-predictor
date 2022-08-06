from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()

def getPolarity(s):
    return sid.polarity_scores(s)

def getSentiment(s):
    sentDict = getPolarity(s)
    if sentDict['compound'] > 0:
        return 'positive'
    elif sentDict['compound'] < 0:
        return 'negative'
    else:    
        return 'neutral'    