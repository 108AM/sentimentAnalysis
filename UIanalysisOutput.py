import matplotlib.pyplot as plt
import numpy as np

def sentimentAnalysis(predictions):
    pos = 0
    neg = 0
    #sums no. 1s and 0s
    for pred in predictions:
        if pred == 1:
            pos += 1
        else:
            neg += 1
    #variables to be passed as arguments into pie chart function
    preds = np.array([pos, neg])
    labels0 = ["positive", "negative"]
    colors0 = ["green", "red"]
    #in the case that there is only 1 colour (want only 1 label)
    if pos == 0:
        labels0 = ["", "negative"]
    if neg == 0:
        labels0 = ["positive", ""]
    plt.pie(preds, labels = labels0, colors=colors0)
    plt.show()
    #scales sentiment to -100 to 100
    return (((pos-neg)*100)/(pos+neg))
def subjectivityAnalysis(predictions):
    total = 0
    #calculates total of all predictions
    for pred in predictions:
        total += pred
    #returns average value
    return total/len(predictions)
def strengthAnalysis(predictions):
    strength = 0
    #magnitude of difference between number and 0.5 (neutral)
    for i in predictions:
        if i - 0.5 > 0:
            strength += i - 0.5
        else:
            strength += 0.5 - i
    #scales strength from 0-100
    return round((strength*200)/len(predictions),3)
def emotionAnalysis(predictions):
    #each index represents an emotion
    emotionlist = [0,0,0,0,0]
    for pred in predictions:
        #index corresponding to that emotion is incremented
        emotionlist[pred] += 1
    labels0 = ["happiness", "sadness", "anger", "fear", "surprise"]
    plt.bar(labels0, emotionlist)
    plt.show()
def keywordAnalysis(predictions):
    pass

