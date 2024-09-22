import numpy as np
from convertfromsparse import CSRmatrixVectorMultiplication, sparseToCSR

def vectorMatrixMultiplication(hypothesisvector, featurematrix):
    hv = hypothesisvector
    fm = featurematrix
    #initialised output vector with same length as the no. rows in fm
    output_vector = [0 for i in fm]
    for row in fm:
        sum = 0
        #performs matrix multiplication
        for i in range(len(row)):
            sum += row[i] * hv[i]
        #sum is written to correct index of output vector
        output_vector[fm.index(row)] = sum
    return output_vector

def sigmoid(testvector):
    x = testvector
    #return sigmoid() for each value in vector
    return [1/(1+np.exp(-i)) for i in x]

def predict(nauttooneV):
    predictions = []
    for x in nauttooneV:
        #if prediction is over 0.5 round to 1 - positive
        if x >= 0.5:
            predictions.append(1)
        else:
            predictions.append(0)
    return predictions

#this returns the cost of each prediction, the total cost as a tuple
def cost(actual, hypothesis):
    y = actual
    hx = hypothesis
    #logistic regression cost function
    costlist = [-y[i] * np.log(hx[i]) + (1-y[i])*np.log(1-hx[i]) for i in range(len(y))]
    absolutecostlist = []
    totalcost = 0
    #only the magnitude of the cost should be added to totalcost
    for i in costlist:
        if i >= 0:
            absolutecostlist.append(i)
            totalcost += i
        else:
            absolutecostlist.append(-i)
            totalcost += -i
        
    return absolutecostlist, totalcost

def featureScalingStandardise(CSRmatrix):
    #initialises matrix to return
    newCSRmatrix = [[],CSRmatrix[1], CSRmatrix[2]]
    sumx = 0
    sumx2 = 0
    n = 0
    for value in CSRmatrix[0]:
        sumx += value
        sumx2 += value**2
        n += 1
    #calcalates mean
    mean = sumx/n
    #calculates standard deviation
    std = np.sqrt(sumx2/n - mean**2)
    
    newCSRrow0 = []
    for element in CSRmatrix[0]:
        #standardised value (centered around 0)
        newCSRrow0.append((element-mean)/std)
    newCSRmatrix[0] = newCSRrow0
    return(newCSRmatrix)

def featureScalingNormalise(CSRmatrix):
    newCSRmatrix = [[],CSRmatrix[1],CSRmatrix[2]]
    xmin = min(CSRmatrix[0])
    xmax = max(CSRmatrix[0])
    for x in CSRmatrix[0]:
        newCSRmatrix[0].append((x-xmin)/(xmax-xmin))
    return(newCSRmatrix)

def workOutCost(CSRM, lenM, thetaV, yV):
    normalCSRM = featureScalingNormalise(CSRM)
    guessyV = CSRmatrixVectorMultiplication(normalCSRM, thetaV, lenM)
    sigV = sigmoid(guessyV)
    costV = cost(yV, sigV)
    return costV

def gradientDescent(yV, hxV, xM, thV, a):
    newthV = []
    #2D array of 'coordinates' of values in CSR matrix
    colrowpairs = [[xM[1][i],xM[2][i]] for i in range(len(xM[0]))]
    loc = 0
    #iterates through parameter vector
    for i in range(len(thV)):
        #initialises gradient of parameter's predictions
        difsum = 0
        #iterates through actual values
        for j in range(len(yV)):
            #if there is a value in the matrix at this location...
            if [i,j] in colrowpairs:
                loc = colrowpairs.index([i,j])
                #...the gradient for that prediction is incremented
                difsum += (hxV[j]-yV[j])*xM[0][loc]
        #new parameter a small step in the opposite direction to the gradient
        newthV.append(thV[i] - a*difsum)
    return newthV

def runGD(M, thV, yV, iters, alpha):
    #initialises parameter vector
    tempthV = thV
    CSRM = sparseToCSR(M)[0]
    lenCSRM = sparseToCSR(M)[1]
    #mormalises matrix values
    nCSRM = featureScalingNormalise(CSRM)
    #updates parameter vector 'iters' times
    for i in range(iters):
        cost = workOutCost(CSRM, lenCSRM, tempthV, yV)
        print(cost)
        #multiplies matrix and parameters
        productV = CSRmatrixVectorMultiplication(nCSRM, tempthV, lenCSRM)
        predictionV = sigmoid(productV)
        #runs gradient descent once
        newthV = gradientDescent(yV, predictionV, nCSRM, tempthV, alpha)
        #updates parameter vector
        tempthV = newthV
    return tempthV

