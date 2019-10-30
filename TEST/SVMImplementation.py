import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

#Input Data

InitialDistance = float(input("plz input the initial distance between Alice and Bob:"))
#initial value of drone
InitialPower = 10.0 #unit:dBm



def PathLoss(distance):
    return 75.0+36.1*( math.log( distance/10.0 ) )

PL = []

CurrentDistance = InitialDistance
RSSI = []
for i in range(0,300):
    RSSI.append( ( InitialPower*( 10.0**( -( PathLoss( CurrentDistance + 1/3.0 )/10.0 ) ) ) )-( InitialPower*( 10**( -( PathLoss( CurrentDistance )/10.0 ) ) ) ) )
    CurrentDistance = CurrentDistance + 1/3.0
print(RSSI)





#Data Preprocessing


