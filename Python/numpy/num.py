import numpy as np
import math as mt
'''
list=[1,2,3,4,5]#in python we can only put 1D array
print(list)
'''

#if we use numpy we can use 1D/2D/3D array
print("1D array")
a=np.array([1,2,3,4,5])
print (a)
print(a.ndim)
print(a.shape)
print(a.size)
if a.size==mt.prod(a.shape):
    print("True")
print(a.dtype)


print ("2D array")
b=np.array([[1,2,3,4,5,],
            [9,8,7,6,0]])
print (b)
print(b.ndim)
print(b.shape)
print(b.size)
b.size==mt.prod(a.shape)
print(b.dtype)
print("3D array")
c=np.array([[[1,2,3],
            [4,5,6],
            [7,8,9]]])
print(c)
print(c.ndim)
print(c.shape)

# def new_func():
#     print("character array")
#     d=np.array["ass","tits"]
#     print(d)
#     print(d.size)
#     print(d.dtype)

# new_func()

