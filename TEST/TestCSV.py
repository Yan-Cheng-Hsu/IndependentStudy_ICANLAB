import pandas as pd
import numpy as np
import math

data = np.random.randint(1,100,(5,5))
df = pd.DataFrame(data,  columns=list('ABCDE'))
#print(df)
df.to_csv("TestCSV.csv")
df_load = pd.read_csv("TestCSV.csv",index_col = 0)
#print(df_load)


#Data structure List:

TimeList = list() # = SampleList = []
for i in range(0,300):
    TimeList.append(i)
#print(TimeList)
RSSIList = []
for i in range(0,300):
    RSSIList.append( math.log(10,10) )
#print(RSSIList)


Origin = {'Time' : TimeList, 'RSSIValue' : RSSIList}
#print(Origin)
time = list( Origin.items() )
#print (time) 
#for i in 
#for i in time:
#   print( time[0][i] )

#print(time[0][0])



