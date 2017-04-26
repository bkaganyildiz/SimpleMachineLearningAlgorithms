import csv
import numpy as np
from numpy.linalg import inv
from math import sqrt
import sys
labels = []
features = []
datas = csv.DictReader(open(str(sys.argv[1])))
fields =  datas.fieldnames
for data in datas :
    dataarr = []
    dataarr.append(1)
    for i in range(len(fields)-1) :
        dataarr.append(float(data[fields[i]]))
    features.append(dataarr)
    labels.append(float(data[fields[len(fields)-1]]))
features = np.array(features)
labels = np.array(labels)
transposed = np.transpose(features)
mult = np.dot(transposed,features)
inverse = inv(mult)
mult2 = np.dot(inverse,transposed)
weights = np.dot(mult2,labels)
print "w0 (1.0) = " + str(weights[0])
for i in range(len(fields)-1) :
        print "w"+str(i+1)+" ("+fields[i]+")=" +str(weights[i+1])
sapkalilabels = np.dot(features,weights)
rmss = np.subtract(labels,sapkalilabels)
rmsstranspose = np.transpose(rmss)
rms = np.dot(rmss,rmsstranspose)
print ("\nRMS Error = "+str(sqrt(rms/len(labels))))
