import pandas as pd
import numpy as np
from scipy.io import arff
from sklearn.model_selection import train_test_split
from sklearn import cross_validation, preprocessing
from knn_example import getResponse, getNeighbors, getAccuracy


def main():
    data = arff.loadarff('kc2.arff')
    data_set = pd.DataFrame(data[0])
    X = np.array(data_set.ix[:, 0:21])
    y = np.array(data_set['problems'])
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    
    predictions = []
    k = 1
    for x in range(len(X_test)):
        neighbours = getNeighbors(X_train, X_test[x], k)
        result = getResponse(neighbours)
        predictions.append(result)
    accuracy = getAccuracy(X_test, predictions)
    print('Accuracy: ' + repr(accuracy) + '%')


main()
