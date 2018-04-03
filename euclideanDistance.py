import math

def euclideanDistance(instance1, instance2, vector_size):
	distance = 0
	for x in range(vector_size):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)