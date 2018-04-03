import csv
import random
from euclideanDistance import euclideanDistance
import operator
import random

def getNeighbors(trainingSet, testInstance, k):
	distances = []
	vector_size = len(testInstance)-1
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], vector_size)
		distances.append((trainingSet[x], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors

def getResponse(neighbors):
	#esta funcao olha os vizinhos, ve qual a classe e joga em um dicionario.
	classVotes = {}
	for x in range(len(neighbors)):
		response = neighbors[x][-1] #-1 quer dizer que estamos indo da direita para esquerda. ou seja, aqui eu pego a classe.
		if response in classVotes:
			classVotes[response] += 1 # caso existir uma classe com o nome la, coloque +1
		else:
			classVotes[response] = 1 #caso nao, eh criado uma e igualado a 1.
	sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]

def getAccuracy(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		#print('> predicted=' + predictions[x] + ', actual=' + testSet[x][-1])
		if testSet[x][-1] in predictions:
			correct += 1
	return (correct/float(len(testSet))) * 100.0	

trainingSet=[]
testSet=[]
loadDataset('kc2.data', 0.66, trainingSet, testSet)
print 'Train: ' + repr(len(trainingSet))
print 'Test: ' + repr(len(testSet))
print trainingSet