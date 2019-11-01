import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, hinge_loss, log_loss
import math
#Input Data

InitialDistance = float(input("plz input the initial distance between Alice and Bob:"))#unit
#initial value of drone
InitialPower = 10.0 #unit:dBm = 10*log(W/mW)


#Unlabeled Data Preprocessing
SimulationSample = 300

#RSSI List and CurrentDistanceList Setup
#RSSI Path Loss Calculation
def PathLoss(d):
    return 75.0 + 36.1*( math.log( d/10, 10.0 ) )
#Sampling every 0.3m 
CurrentDistance = InitialDistance
RSSIList = []
CurrentDistanceList = []#In case
Y = []
for i in range(SimulationSample):
    RSSIList.append( PathLoss(CurrentDistance) - PathLoss(CurrentDistance + 1/3.0) )
    CurrentDistanceList.append(CurrentDistance)
    Y.append(1)
    CurrentDistance = CurrentDistance + 1/3.0

for i in range(SimulationSample):
    RSSIList.append( np.random.uniform(-10,10) )
    CurrentDistanceList.append( np.random.uniform(0,100) )
    Y.append(0)

    
#Attribute Table setup as DataFrame

AttributesTable = { "RSSI": RSSIList, "Distance": CurrentDistanceList, 'Y':Y }
AttributesTable = pd.DataFrame(AttributesTable)




#Seperate the Data
X = AttributesTable.drop('Y',axis = 1)
Y = AttributesTable['Y']


X_TrainingData, X_TestingData, Y_TrainingData, Y_TestingData = train_test_split(X, Y, test_size = 0.20)

#==============Main Program Start==============

Iteration = 10
AccuracyList = []
CrossEntopyLossList = []
HingeLossList = []

while Iteration =< len(Y_TrainingData):
    svclassifier = SVC(kernel='rbf')
    svclassifier.fit( X_TrainingData[0:Iteration], Y_TrainingData[0:Iteration] )
    Y_PredictionData = svclassifier.predict( X_TestingData )

    AccuracyList.append( accuracy_score( Y_TestingData, Y_PredictionData ) )
    HingeLossList.append( hinge_loss( Y_TestingData, Y_PredictionData ) )
    CrossEntopyLossList.append( log_loss( Y_TestingData, Y_PredictionData ) ) 

    print( confusion_matrix( Y_TestingData, Y_PredictionData ) )#this is the support vector
    print( classification_report( Y_TestingData, Y_PredictionData ) )
    Iteration = Iteration + 1


TempDict = { "Accuracy":AccuracyList, "HingeLoss": HingeLossList, "CrossEntropy": CrossEntopyLossList }
EvaluationTable = pd.DataFrame(TempDict)
EvaluationTable.to_excel( "EvaluationTable.xlsx", sheet_name = "EvaluationTable", index = False )












