import csv
import random
import math
import operator

def loadDataset(filename, split, traningSet = [], testSet = []):
    with open(filename, 'rb') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)-1):
            for y  in range(4): # por conta dos atributos que eu quero usar na distancia euclidiana
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

# def main():
# 	# prepare data
# 	trainingSet=[]
# 	testSet=[]
# 	split = 0.67
# 	#nao eh um proporcao, eh uma fator que pode determinar se o dado eh de test ou de treinamento. 
# 	loadDataset('iris.data', split, trainingSet, testSet)
# 	print 'Train set: ' + repr(len(trainingSet))
# 	print 'Test set: ' + repr(len(testSet))
# 	# generate predictions
# 	predictions=[]
# 	k = 3
# 	for x in range(len(testSet)):
# 		neighbors = getNeighbors(trainingSet, testSet[x], k)
# 		result = getResponse(neighbors)
# 		predictions.append(result)
# 	accuracy = getAccuracy(testSet, predictions)
# 	print('Accuracy: ' + repr(accuracy) + '%')
	
# main()