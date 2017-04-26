import csv
import sys
import numpy as np
from math import sqrt
datas = csv.DictReader(open(str(sys.argv[1])))
knn = int(sys.argv[2])
k = int(sys.argv[3])
predict = []
for i in range(k) :
    predict.append(float(sys.argv[i+4]))
print "k = " + str(knn)
labels = []
features = []
weights = []
distance =  []

for i in range(len(datas.fieldnames)):
    weights.append(float(0))
fields =  datas.fieldnames
for data in datas :
    dataarr = []
    for i in range(len(fields)-1) :
        dataarr.append(float(data[fields[i]]))
    features.append(dataarr)
    labels.append(float(data[fields[len(fields)-1]]))

for feature in features :
    distanceSum = 0
    #print feature
    #print predict
    for k in range(len(predict)) :
        distanceSum += (feature[k] - predict[k])*(feature[k] - predict[k])
    distance.append(sqrt(distanceSum))

for i in range(len(fields)-1) :
        print "Attribute "+str(i+1)+" ("+fields[i]+")  =  " + str(predict[i])
print "\n"
arr = np.array(distance)
indexs = arr.argsort()[:knn]
myfinalsum = 0
multiplexer = 0
i=1
for it in indexs :
    multiplexer += (1/distance[it])
    myfinalsum += (1/distance[it]) * labels[it]
    print("Instance " + str(i) + " : Index = " + str(it) + " , "
        + str(features[it]) + " , Class Label = " + str(labels[it])
        + " , Distance = " + str(distance[it]) + " , Weight = " + str(1/distance[it])
        )
    i += 1

print ("\n\nWeighted class label ("+fields[len(fields)-1]+") = " + str(myfinalsum*(1/multiplexer)))
