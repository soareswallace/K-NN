import pandas as pd
import numpy as np
from scipy.io import arff
from sklearn.model_selection import train_test_split
from sklearn import cross_validation, preprocessing
from knn_example import getResponse, getNeighbors, getAccuracy


def main():
    number_of_neighbors = [1,2,3,5,7,9,11,13,15]    
    for k in number_of_neighbors:    
        data_set = pd.read_csv('kc2.data')
        X = np.array(data_set.drop(['problems'], 1))
        y = np.array(data_set['problems'])
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)
        predictions = []
        for x in range(len(X_test)):
            neighbours = getNeighbors(X_train, X_test[x], k)
            result = getResponse(neighbours)
            predictions.append(result)
        accuracy = getAccuracy(X_test, predictions)
        print('Accuracy for k = ' + str(k) + ': ' + repr(accuracy) + '%')

main()
