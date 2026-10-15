import numpy as np

# index of a array
a=np.array([1,3,2,4,5,6,4,3,3])
print(a[-5])
print(a[0])

#number slicing

print(a[-1:2:-1])

#greater than

print(a[a>2])

#multiple indeces

indices=[3,5,8]
print(a[indices])

