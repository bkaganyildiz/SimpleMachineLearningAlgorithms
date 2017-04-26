import csv
import sys
#import numpy as np
from math import sqrt
datas = csv.DictReader(open(str(sys.argv[1])))
mu = float(sys.argv[2])
minchange = float(sys.argv[3])
labels = []
features = []
weights = []

for i in range(len(datas.fieldnames)):
    weights.append(float(0))
fields =  datas.fieldnames

for data in datas :
    dataarr = []
    dataarr.append(1)
    for i in range(len(fields)-1) :
        dataarr.append(float(data[fields[i]]))
    features.append(dataarr)
    labels.append(float(data[fields[len(fields)-1]]))

def calculateTranspose(matrix):
    ''' TODO : get matrix len and return transpose of it  '''
    ''' var matrix : nxm matrix type : list[list] '''
    transposed = []
    if not matrix : #.any() :
        ''' Check if list is empty then return it back '''
        return matrix
    if any(isinstance(i,list) for i in matrix) :
        for i in range(len(matrix[0])):
            inner = []
            for j in range(len(matrix)):
                inner.append(matrix[j][i])
            transposed.append(inner)
    else :
        for i in matrix :
            transposed.append([i])
    return transposed



def subtractMatricies(matrix1 , matrix2):
    ''' TODO : subtract two matricies and return the subtraction '''
    ''' var matrix1 : nxm matrix type : list[list] ,
        var matrix2 : nxm matrix type : list[list] '''
    result = []
    for i in range(len(matrix1)) :
        result.append(matrix1[i] - matrix2[i])
    return result

def ElementWiseMultiplication(list1, list2):
	return [ list1[i] * list2[i] for i in range(len(list1))]

def dotMatrices(matrix1 , matrix2):
    ''' TODO :  get dot product of  two matricies and return the result '''
    ''' var matrix1 : nxm matrix type : list[list] ,
        var matrix2 : nxm matrix type : list[list] '''
    returner = []
    if any(isinstance(i,list) for i in matrix1) :
        for mat in matrix1 :
            mysum = 0
            summatrix = ElementWiseMultiplication(mat,matrix2)
            for i in summatrix :
                mysum += i
            returner.append(mysum)
    else :
        mysum = 0
        for i in range(len(matrix1)) :
            mysum += matrix1[i] * matrix2[i][0]
        return mysum
    return returner

def calculateRMS(weightMatrix):
    ''' TODO : RMS calculater for given weight matrix '''
    ''' var weightMatrix : 1xn matrix type : list '''
    #print features , weightMatrix
    sapkalilabels1 = dotMatrices(features,weightMatrix)
    #sapkalilabels = np.dot(features,weightMatrix) #dotMatrices
    #print sapkalilabels1
    #print sapkalilabels
    #rmss = np.subtract(labels,sapkalilabels) #subtractMatricies
    rmss1 = subtractMatricies(labels,sapkalilabels1)
    #rmsstranspose = np.transpose(rmss) #calculateTranspose
    rmsstranspose1 = calculateTranspose(rmss1)
    #rms = np.dot(rmss,rmsstranspose) #dotMatrices
    rms1 = dotMatrices(rmss1,rmsstranspose1)
    #print (rms,rms1)
    return sqrt(rms1/len(labels))

def updateWeight(index) :
    ''' TODO : update weight at the index of data row '''
    ''' var index : type int '''
    mysum = 0
    for j in range(len(labels)):
        aj = features[j][index]
        b = labels[j]
        weisum = 0
        for k in range(len(weights)) :
            weisum += weights[k]*features[j][k]
        mysum += (-1)*aj*(b-weisum)
    return (2*mysum)/len(labels)

counter = 0
newrms = 0
while True :
    oldrms = calculateRMS(weights)
    print "Iteration "+str(counter) + " : "+str(weights) + ", RMS Error = " + str(oldrms)
    updatedWeight = []
    for i in range(len(weights)) :
        updatedWeight.append(updateWeight(i))
    for i in range(len(updatedWeight)) :
        weights[i] = weights[i] - mu*updatedWeight[i]
    newrms = calculateRMS(weights)
    counter += 1
    if (oldrms-newrms) < minchange :
        print "Iteration "+str(counter) + " : "+str(weights) + ", RMS Error = " + str(newrms) + "\n"
        break ;
print "w0 (1.0) = " + str(weights[0])
for i in range(len(fields)-1) :
        print "w"+str(i+1)+" ("+fields[i]+")=" +str(weights[i+1])
print "\nRMS Error = "+str(newrms)
