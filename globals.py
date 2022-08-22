from happinessPredictor import happinessAlgo

class h(object):
    def __init__(self):
        self.happinessScore = happinessAlgo()
        print(self.happinessScore)

    def getHappinessScore(self):
        return self.happinessScore
    
    def newHappinessScore(self):
        self.happinessScore = happinessAlgo()
        return self.happinessScore

'''
def new_h():
    global new_h_score
    new_h_score = happinessAlgo()


h_score = new_h_score
'''