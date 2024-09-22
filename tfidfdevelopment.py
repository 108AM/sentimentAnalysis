import math
import numpy

def createTfidfMatrix(dataset, wV):

    #initialises 3 matrices
    tf_matrix = []
    idf_matrix = []
    tfidf_matrix = []

    #dataset length is the number of rows
    datasetlength = len(dataset)

    #in the case that a tfidf matrix is being made after training
    if wV is not None:
        wordvector = wV
    #in the case that a tfidf matrix is being made for training (so no wordvector yet)
    else:
        wordvector = []
        for tweet in dataset:
            for word in tweet.split(" "):
                #for each word in dataset, if the word not in the wordvector, add it to the wordvector
                #creating a list of unique words
                if word not in wordvector:
                    wordvector.append(word)

    #variable to hold primitive tfmatrix
    tf_matrix0 = []

    #initialises 2 empty matrices for each row in dataset
    for tweet in dataset:
        tweet_tf_matrix0 = []

        #empty strings vector with length of wordvector
        tweet_tf_matrix1 = ["" for i in range(len(wordvector))]

        #tweetlength is the number of words in the tweet
        tweetlength = len(tweet.split(" "))
        #a dictionary with each unique word in the tweet as the key
        #and the number of times the word occurs is the value
        worddict = {i:tweet.count(i) for i in set(tweet.split(" "))}

        for item in list(worddict.items()):
            #appends tf value of each word
            tweet_tf_matrix0.append([item[0], item[1]/tweetlength])

        for pair in tweet_tf_matrix0:
            if pair[0] in wordvector:
                indexofword = wordvector.index(pair[0])
                #the word and tf are inserted into tweet_tf_matrix1
                tweet_tf_matrix1[indexofword] = pair

        #each word-tf pair is appended to the primitive tfmatrix0
        tf_matrix0.append(tweet_tf_matrix1)

    #primitive matrices initialised
    wordvector_idf_matrix = []
    idf_matrix0 = []

    for word in wordvector:
        tweetcount = 0
        for tweet in dataset:
            #the number of tweets containing that word (for each word in the wordvector) is stored in tweetcount
            if word in tweet.split(" "):
                tweetcount += 1
        wordvector_idf_matrix.append([word,math.log10(datasetlength/(tweetcount+0.0001))])

    for tweet in dataset:
        tweet_idf_matrix = ["" for i in range(len(wordvector))]
        
        for word in wordvector:
            if word in tweet.split(" "):
                #appends idf score and word to the idf matrix for that tweet
                tweet_idf_matrix[wordvector.index(word)] = [word,wordvector_idf_matrix[wordvector.index(word)][1]]
        
        idf_matrix0.append(tweet_idf_matrix)    

    for tweet in tf_matrix0:
        tweetmatrix = []
        for wordpair in tweet:
            #if item in tf_matrix0 is a pair... 
            if len(wordpair)>1:
                #...only the tf score is appended to the tweetmatrix
                tweetmatrix.append(wordpair[1])
            else:
                #...otherwise the tf score is of course 0
                tweetmatrix.append(0)
        #creates final tfmatrix
        tf_matrix.append(tweetmatrix)

    for tweet in idf_matrix0:
        tweetmatrix = []
        for wordpair in tweet:
            if len(wordpair)>1:
                tweetmatrix.append(wordpair[1])
            else:
                tweetmatrix.append(0)
        idf_matrix.append(tweetmatrix)

    #multiplies the matrices cell by cell into the tfidf matrix
    tfidf_matrix = numpy.multiply(tf_matrix, idf_matrix).tolist()

    return tfidf_matrix, wordvector






        




