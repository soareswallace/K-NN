import csv
import random
import math
import operator

def loadDataset(filename, split, traningSet = [], testSet = []):
    with open(filename, 'rb') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)-1):
            for y  in range(4):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:
                traningSet.append(dataset[x])
            else:
                testSet.append(dataset[x])

def euclideanDistance(instance1, instance2, vector_size):
	distance = 0
	for x in range(vector_size):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)


def getNeighbors(trainingSet, testInstance, k):
	distances = []
	vector_size = len(testInstance)-1
	print "lenght -> " + str(vector_size)
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], vector_size)
		distances.append((trainingSet[x], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors

trainSet = [[2, 2, 2, 'a'], [4, 4, 4, 'b'], [4, 5, 5, 'c']]
testInstance = [5, 5, 5]
k = 1
neighbors = getNeighbors(trainSet, testInstance, 2)
print(neighbors)	


#trainingSet=[]
#testSet=[]
#loadDataset('iris.data', 0.66, trainingSet, testSet)
#print 'Length of Train: ' + repr(len(trainingSet))
#print 'Length of Test: ' + repr(len(testSet))
#data1 = [2, 2, 2, 'a']
#data2 = [4, 4, 4, 'b']
#distance = euclideanDistance(data1, data2, 3)
#print 'Distance: ' + repr(distance)