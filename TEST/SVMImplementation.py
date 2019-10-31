import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
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
for i in range(SimulationSample):
    RSSIList.append( PathLoss(CurrentDistance) - PathLoss(CurrentDistance + 1/3.0) )
    CurrentDistanceList.append(CurrentDistance)
    CurrentDistance = CurrentDistance + 1/3.0

#Attribute Table setup as DataFrame

AttributesTable = { "RSSI": RSSIList, "Distance": CurrentDistanceList }
AttributesTable = pd.DataFrame(AttributesTable)

#Output as CSV

AttributesTable.to_excel("Test.xlsx", sheet_name = 'AttributesTable',index = False)

#Unlabeled Data preprocess ends 



#reload the Labeled Data

LabeledAttributesTable = pd.read_excel("Test_Labeled.xlsx")

#Seperate Data to Training Data and Testing Data

X = LabeledAttributesTable.drop('Y',axis = 1)
Y = LabeledAttributesTable['Y']


X_TrainingData, X_TestingData, Y_TrainingData, Y_Testing = train_test_split(X, Y, test_size = 0.20)



#Main Program

Iteration = 0

while Iteration < len( Y_TrainingData ):
    















