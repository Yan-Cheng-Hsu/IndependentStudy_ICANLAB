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


#Data Preprocessing


#RSSI List and CurrentDistanceList Setup
#RSSI Path Loss Calculation
def PathLoss(d):
    return 75.0 + 36.1*( math.log( d/10, 10.0 ) )
#Sampling every 0.3m 
CurrentDistance = InitialDistance
RSSIList = []
CurrentDistanceList = []#In case
for i in range(0,300):
    RSSIList.append( PathLoss(CurrentDistance) - PathLoss(CurrentDistance + 1/3.0) )
    CurrentDistanceList.append(CurrentDistance)
    CurrentDistance = CurrentDistance + 1/3.0

#Attribute Table setup as DataFrame
AttributesTable = {"RSSI": RSSIList}
AttributesTable = pd.DataFrame(AttributesTable)
#Output as CSV
AttributesTable.to_csv("Test.csv")











