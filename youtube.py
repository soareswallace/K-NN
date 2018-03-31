import pandas as pd
import numpy as np
from scipy.io import arff
from sklearn.model_selection import train_test_split
from sklearn import cross_validation, preprocessing, neighbors
from knn_example import getResponse, getNeighbors, getAccuracy

df = pd.read_csv('kc2.data')
X = np.array(df.drop(['problems'], 1))
y = np.array(df['problems'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print accuracy