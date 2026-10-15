import numpy as np

# slicing of array
'''a=np.arange(1,11)
print(a)
arr1=a[3:4]
print(arr1)'''

#stacking of array one after one
'''a1=np.array([[1,2,3],[2,3,4]])
print(a1)
a2=np.array([[9,8,7],[8,7,6]])
print(a2)
new=np.vstack((a1,a2))
print(new)
print(new.shape)'''

# stacking of array one beside one
'''a1=np.array([[1,2,3],[2,3,4]])
print(a1)
a2=np.array([[9,8,7],[8,7,6]])
print(a2)
new=np.hstack((a1,a2))
print(new)
print(new.shape)'''

# spliting of array

'''a=np.arange(1,21).reshape(4,5)
#print(a)
b=np.hsplit(a,(5,4))
print(b)'''