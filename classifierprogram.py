from trainingprogram import Analyser
from datasetpreparation import cleanDataset, createMatrix
import pandas as pd
import csv
from logisticregressionclassifier import *

def textToMatrix(trainingfilename, applicationfilename):
    #creates word vector and defines training file
    analyser = Analyser()
    analyser.settrainingfile(trainingfilename)
    analyser.setTrainingWordVector()

    #creates feature matrix for file of text to analyse
    newdataset = pd.read_csv(applicationfilename, header=None, names=["text"])
    cleanDataset(newdataset)
    Matrix = createMatrix(newdataset,analyser.trainingwordvector)

    return Matrix

def predictSentiment(matrix, thetafile):

    #parameter vector
    theta = []

    #reads parameters by casting from string to float into thata
    with open(thetafile, "r+", encoding="utf8") as file:
        for row in csv.reader(file):
            if row != []:
                theta = [float(i) for i in row]

    #predicts sentiments
    prepreds = vectorMatrixMultiplication(theta, matrix)
    sigpreds = sigmoid(prepreds)
    preds = predict(sigpreds)

    return preds,sigpreds











