
import random 
# random just return one object
import numpy as np 
# use numpy.random  will return one or an array object
 
a = random.random()
# return one object
#aa = random.random(10)
# fail, because it only return one object
 
b = random.randint(10,20)
# return an int object between 10~20
for i in range(10):   
    print(random.uniform(10,20))

#return an object between 10~20
 
d = random.randrange(10,20,3)
#return an int object in range 10~20 (such 10, 13,16,19)
 
e = random.choice(('pass','fail','null'))
# random choice one object
 
 
 
A = np.random.random()
# same as random.random()
 
AA = np.random.random(10) # 更新：不建議這樣用，因為np.random.random(10,4)的矩陣會回報錯
# can return an array
 
G = np.random.rand(10)   # 更新：np.random.rand(10,4)的矩陣仍可以過 所以用矩陣的話寫rand就好
# same as np.random.random(10)
 
F = np.random.randn()
# return an normal distribution or Gaussian distribution object in random
FF=  np.random.randn(10)
# return an normal distribution or Gaussian distribution array in random
 
 
 
B = np.random.randint(10,20)
# same as random.randint(10,20)
 
CC = np.random.uniform(10,20)
# same as random.uniform(10,20)
 
#DD = np.random.randrange(10,20,3)
# fail, becauseno attribute randrange in np.random