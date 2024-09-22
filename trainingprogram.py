from datasetpreparation import *
from logisticregressionclassifier import *
import csv

def pretrainPrep(trainfilename):
    #cleans dataset
    dataset = prepareSelectionDataset(trainfilename)
    cleanDataset(dataset)
    return dataset

def learn(iters, alpha, dslen, trainfilename):
    #cleans dataset
    dataset = pretrainPrep(trainfilename)
    #returns word vector for later classification
    permwordV = returnWordVector(dataset, None)
    sentimentV = prepareSelectionSentimentV(dslen)
    trainingtfidfM = createMatrix(dataset, permwordV)
    #initialises the original parameter vector
    initialthV = [1 for i in range(len(permwordV))]

    #runs gradient descent
    thV = runGD(trainingtfidfM, initialthV, sentimentV, iters, alpha)
    return thV

def savethV(iters, alpha, filename, dslen, trainfilename):
    #runs GD
    thV = learn(iters, alpha, dslen, trainfilename)
    #saves parameter vector to output file
    with open(filename, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(thV)

class Analyser:

    #initialises important attributes to be inherited by Trainer
    def __init__(self):
        self.trainingfile = ""
        self.trainingwordvector = []
    
    def settrainingfile(self, filename):
        self.trainingfile = filename

    #creates a word vector from the training file
    def setTrainingWordVector(self):
        newdataset = pretrainPrep(self.trainingfile)
        self.trainingwordvector = returnWordVector(newdataset, None)

class Trainer(Analyser):

    #initialises variables for running gradient descent
    def __init__(self):
        self.outputfile = ""
        self.iterations = 0
        self.learningrate = 0
        self.datasetlength = 0

    #file to contain parameter vector
    def setoutputfile(self, filename):
        self.outputfile = filename

    def setiterations(self, iters):
        self.iterations = iters
    
    def setlearningrate(self, a):
        self.learningrate = a
    
    #number of examples in training file
    def setdatasetlength(self):
        self.datasetlength = len(pd.read_csv(self.trainingfile, sep=";;;"))

    def saveHypothesis(self):
        savethV(self.iterations, self.learningrate, self.outputfile, self.datasetlength, self.trainingfile)



