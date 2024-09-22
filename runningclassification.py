from logisticregressionclassifier import runGD, vectorMatrixMultiplication
from datasetpreparation import tfidfM, sentimentV

#print(tfidfM)
#print(len(tfidfM))
for i in range(len(tfidfM)):
    #print(tfidfM[i])
    #print(len(tfidfM[i]))
    pass

mytweets = ["I seriously hate everyone. #angryme"]


thetaV = [1 for i in range(len(tfidfM[0]))]
actualsentimentV = sentimentV
newthetaV = runGD(tfidfM, thetaV, actualsentimentV, 50, 0.5)
vectorMatrixMultiplication()





