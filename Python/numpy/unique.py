import numpy as np

a=np.array([2,2,3,1,8,3,5,6,3,12,1,1,3,2,2,1,1,13,5,7,32,2,1,6])
unique=np.unique(a)
print(unique)

count=np.unique(a,return_counts=True)
print(count)