from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()

def getPolarity(s):
    try:
        sid.polarity_scores(s)
    except:
        print("Error in sentiment analysis.")
        return None
    return sid.polarity_scores(s)

def getSentiment(s):
    sentDict = getPolarity(s)
    if sentDict['compound'] >= 0.5:
        return 'very positive'
    elif sentDict['compound'] > 0 and sentDict['compound'] < 0.5:
        return 'postive'
    elif sentDict['compound'] < 0 and sentDict['compound'] > -0.5:
        return 'negative'
    elif sentDict['compound'] <= -0.5:
        return 'very negative'
    else:    
        return 'neutral'    
    
    