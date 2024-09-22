import pandas as pd
import re
import string
from nltk import PorterStemmer

import tfidfdevelopment as tfidfdev

def prepareDataset():
    #labelling the initial csv file
    df_columns = ['sentiment','id','date','flag','user','text']
    df = pd.read_csv("sentiment140.csv", header = None, sep = ",", names = df_columns)

    #making a csv containing only the variables we need
    data = df[['sentiment','text']]

    #replacing 4 with 1 (indicating positive sentiment)
    data['sentiment'] = data['sentiment'].replace(4,1)

    #taking a sample of the million tweets
    actual_positive_data = data[data['sentiment'] == 1].head(25000)
    actual_negative_data = data[data['sentiment'] == 0].head(25000)

    #taking a smaller sample for faster ML
    positive_data = data[data['sentiment'] == 1].head(100)
    negative_data = data[data['sentiment'] == 0].head(100)

    #formation of the training dataset
    actual_dataset = pd.concat([actual_negative_data, actual_positive_data])

    #formation of a smaller dataset
    dataset = pd.concat([negative_data, positive_data])

    #cleaning all the data. making text lowercase
    dataset['text'] = dataset['text'].str.lower()

    return dataset

def prepareSelectionDataset(filename):

    #adds ;;; to the end of each row
    with open(filename, "r+", encoding="utf8") as file:
        for row in file:
            row = row + ";;;"
    
    #reads file into pandas dataframe
    df_columns = ['text']
    df = pd.read_csv(filename, header = None, names = df_columns, sep=";;;")
    df['text'] = df['text'].str.lower()

    return df

def prepareSelectionSentimentV(dslen):

    #the first half of dataset is negative (0) and second half is 1
    sentimentV = []
    for i in range(int(dslen/2)):
        sentimentV.append(0)
    for i in range(int(dslen/2)):
        sentimentV.append(1)

    return sentimentV


#removing @, hastags
def atHashRemover(dataset):
    
    for i in range(len(dataset)):
        tweet = dataset['text'].iloc[i]
        #splits each tweet into words
        splitlist = tweet.split(' ')
        #removes words if they begin with @ or #
        for word in splitlist:
            if len(word) > 0 and word[0] == '@':
                splitlist.remove(word)
            elif len(word) > 0 and word[0] == '#':
                splitlist.remove(word)
        #joins words back into tweet
        newtweet = ' '.join(splitlist)
        dataset['text'].iloc[i] = newtweet

#removing urls
def URLremover(tweet):
    return re.sub('((www.[^s]+)|(https?://[^s]+))',' ',tweet)

#removing numbers
def numremover(tweet):
    return re.sub('[0-9]+', '', tweet)

#removing punctuation
def punctuationRemover(dataset):
    punctuations = string.punctuation
    #splits each tweet into a list of characters
    for i in range(len(dataset)):
        tweetlist = [char1 for char1 in dataset['text'].iloc[i]]
        newtweet = []
        for char2 in tweetlist:
            #appends each non-punctuation character to the new tweet as long
            if char2 not in punctuations:
                newtweet.append(char2)
        newtweet = ''.join(newtweet)
        dataset['text'].iloc[i] = newtweet

#removes consecutive repeating characters
def characterRepetitionRemover(dataset):
    for i in range(len(dataset)):
        tweet = dataset['text'].iloc[i]
        #splits each tweet into a list of characters in the tweet
        tweetlist = [char for char in tweet]
        newlist = []
        for j in range(len(tweetlist)-1):
            #if each character is not equal to the consecutive character...
            if tweetlist[j] != tweetlist[j+1]:
                #...it is appended to the new tweet
                newlist.append(tweetlist[j])
        if len(tweetlist) > 0:
            newlist.append(tweetlist[-1])
        dataset['text'].iloc[i] = ''.join(newlist)

#removes stopwords
def stopwordRemover(dataset):
    stopwords = ['a', 'about', 'above', 'after', 'again', 'ain', 'all', 'am', 'an',
             'and','any','are', 'as', 'at', 'be', 'because', 'been', 'before',
             'being', 'below', 'between','both', 'by', 'can', 'd', 'did', 'do',
             'does', 'doing', 'down', 'during', 'each','few', 'for', 'from',
             'further', 'had', 'has', 'have', 'having', 'he', 'her', 'here',
             'hers', 'herself', 'him', 'himself', 'his', 'how', 'i', 'if', 'im','in',
             'into','is', 'it', 'its', 'itself', 'just', 'll', 'm', 'ma',
             'me', 'more', 'most','my', 'myself', 'now', 'o', 'of', 'on', 'once',
             'only', 'or', 'other', 'our', 'ours','ourselves', 'out', 'own', 're','s', 
             'same', 'she', "shes", 'should', "shouldve",'so', 'some', 'such',
             't', 'than', 'that', "thatll", 'the', 'their', 'theirs', 'them',
             'themselves', 'then', 'there', 'these', 'they', 'this', 'those',
             'through', 'to', 'too','under', 'until', 'up', 've', 'very', 'was',
             'we', 'were', 'what', 'when', 'where','which','while', 'who', 'whom',
             'why', 'will', 'with', 'won', 'y', 'you', "youd","youll", "youre",
             "youve", 'your', 'yours', 'yourself', 'yourselves']

    for i in range(len(dataset)):
        tweet = dataset['text'].iloc[i]
        tweetlist = []
        #tweets are split into words
        for word in tweet.split(" "):
            #if word is not a stopword, it is added to new tweet
            if word not in stopwords:
                tweetlist.append(word)
        dataset['text'].iloc[i] = " ".join(tweetlist)

#stemming function
def stemmer(dataset):
    #creates PorterStemmer object
    ps = PorterStemmer()
    for i in range(len(dataset)):
        words = dataset['text'].iloc[i].split(" ")
        #each word in tweet converted to stemmed word
        stemmed_words = [ps.stem(word) for word in words]
        dataset['text'].iloc[i] = " ".join(stemmed_words)
        
# applies all cleaning algorithms
def cleanDataset(dataset):
    #applies to each piece of text in turn
    dataset['text'] = dataset['text'].apply(lambda x: URLremover(x))
    dataset['text'] = dataset['text'].apply(lambda x: numremover(x))
    #applied to total dataset
    atHashRemover(dataset)
    punctuationRemover(dataset)
    stopwordRemover(dataset)
    characterRepetitionRemover(dataset)
    stemmer(dataset)

def createMatrix(dataset, wV):
    tfidfM = tfidfdev.createTfidfMatrix([dataset['text'].iloc[i] for i in range(len(dataset))], wV)[0]
    return tfidfM

def returnWordVector(dataset, wV):
    permanentwordvector = tfidfdev.createTfidfMatrix([dataset['text'].iloc[i] for i in range(len(dataset))], wV)[1]
    return permanentwordvector

def returnSentimentV(dataset):
    sentimentV = [dataset['sentiment'].iloc[i] for i in range(len(dataset))]
    return sentimentV








