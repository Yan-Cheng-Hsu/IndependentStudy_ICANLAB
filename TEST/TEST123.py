import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, hinge_loss, log_loss
import math


#Input Data
InitialDistance = float(input("plz input the initial distance between Alice and Bob:"))#unit

#initial Power of drone
InitialPower = 10.0 #unit:dBm = 10*log(W/mW)

#initial Channel Offset caused by channel mismatch
InitialChannelMismatchOffsetofSIM = 2540 #unit: Hz
StandardDeviation = 1
MeanofCFO = 0

#Unlabeled Data Preprocessing
SimulationSample = 300

#RSSI List, CurrentDistanceList and CFOList Setup
#RSSI Path Loss Calculation
def PathLoss(d):
    return 75.0 + 36.1*( math.log( d/10, 10.0 ) ) 

#CFO Calculation
def CFOestimation(InitialChannelOffset,Mean, Deviation):
    return InitialChannelOffset + np.random.normal(loc = Mean, scale = Deviation, size = None)


#Sampling every 0.3m 
CurrentDistance = InitialDistance
RSSIList = []
CFOList = []
CurrentDistanceList = []#In case
Y = []
for i in range(SimulationSample):
    RSSIList.append( PathLoss(CurrentDistance) - PathLoss(CurrentDistance + 1/3.0) )
    CFOList.append( CFOestimation(InitialChannelMismatchOffsetofSIM, MeanofCFO, StandardDeviation) )
    CurrentDistanceList.append(CurrentDistance)
    Y.append(1)
    CurrentDistance = CurrentDistance + 1/3.0




for i in range(SimulationSample):
    RSSIList.append( np.random.uniform(-5,5) )
    CFOList.append( CFOestimation(1500, MeanofCFO, StandardDeviation)  )
    CurrentDistanceList.append( np.random.uniform(0,100) )
    Y.append(0)



#Attribute Table setup as DataFrame

AttributesTable = { "RSSI": RSSIList,"CFO": CFOList, "Distance": CurrentDistanceList, 'Y':Y }
AttributesTable = pd.DataFrame(AttributesTable)


AttributesTable.to_excel( "Attributes Table with no difference CFO.xlsx", sheet_name = "Attribute Table")

AttributesColumnNameList = ["RSSI","CFO","Distance",'Y']

for i in AttributesColumnNameList:
    AttributesTable



#Seperate the Data
X = AttributesTable.drop('Y',axis = 1)
Y = AttributesTable['Y']


X_TrainingData, X_TestingData, Y_TrainingData, Y_TestingData = train_test_split(X, Y, test_size = 0.20)





#==============Main Program Start==============#

#Iteration = 10
#AccuracyList = []
#CrossEntopyLossList = []
#HingeLossList = []

#while Iteration <= len(Y_TrainingData):
    #svclassifier = SVC(kernel='rbf')
    #svclassifier.fit( X_TrainingData[0:Iteration], Y_TrainingData[0:Iteration] )
    #Y_PredictionData = svclassifier.predict( X_TestingData )

    #AccuracyList.append( accuracy_score( Y_TestingData, Y_PredictionData ) )
    #HingeLossList.append( hinge_loss( Y_TestingData, Y_PredictionData ) )
    #CrossEntopyLossList.append( log_loss( Y_TestingData, Y_PredictionData ) ) 

    #print( confusion_matrix( Y_TestingData, Y_PredictionData ) )#this is the support vector
    #print( classification_report( Y_TestingData, Y_PredictionData ) )
    #Iteration = Iteration + 1

#TempDict = { "Accuracy":AccuracyList, "HingeLoss": HingeLossList, "CrossEntropy": CrossEntopyLossList }
#EvaluationTable = pd.DataFrame(TempDict)
#EvaluationTable.to_excel( "EvaluationTable.xlsx", sheet_name = "EvaluationTable")


def TrueRSSI(d):
    return 10 - ( 75.0 + 36.1*( math.log( d/10, 10.0 ) ) )

TrueRSSIList = []
TrueCFOList = []
Distance = 5

for i in range(SimulationSample):
    TrueRSSIList.append(TrueRSSI(Distance))
    TrueCFOList.append( CFOestimation(InitialChannelMismatchOffsetofSIM, MeanofCFO, StandardDeviation) )
    Distance = Distance + 1/3

TempDict2 = {"TRUERSSI": TrueRSSIList, "TRUECFO": TrueCFOList}
a = pd.DataFrame(TempDict2)
a.to_excel("TRUEvalue.xlsx", sheet_name = "TRUEvalue")













