import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC


#Data Preprocessing
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# Assign colum names to the dataset
colnames = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']

# Read dataset to pandas dataframe
irisdata = pd.read_csv(url, names=colnames)
irisdata.to_csv("Test.csv")

X = irisdata.drop('Class', axis=1)#x = pd.DataFrame
y = irisdata['Class']#y = pd.Series
#x.iloc[0:150]
#y is equal to list
#print(X)
#print(type(X))



#Seperate Data from 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)


svclassifier = SVC(kernel='rbf')
svclassifier.fit(X_train, y_train)

y_pred = svclassifier.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, y_pred))
print("=========================")
print( type(confusion_matrix(y_test, y_pred)) )
print(classification_report(y_test, y_pred))
print( type(classification_report(y_test, y_pred)) )


################################################################



RSSI = []
for i in range(300):
    RSSI.append(i)

CIR = []
for i in range(300):
    CIR.append(299-i)

dictionary = {"RSSI": RSSI}



AttributesTable = pd.DataFrame(dictionary)

Y = []
for i in range(150):
    Y.append(1)
for i in range(150):
    Y.append(0)
Ytable = pd.Series(Y)


#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)


#svclassifier = SVC(kernel='rbf')
#svclassifier.fit(AttributesTable, Ytable)

#y_pred = svclassifier.predict(AttributesTable)

#print(y_pred)
#print("===================")

#from sklearn.metrics import classification_report, confusion_matrix
#print(confusion_matrix(Ytable, y_pred))#this is the support vector
#print(classification_report(Ytable, y_pred))




                                              