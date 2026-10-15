import numpy as np


# 1D array
vec1=np.array([3,4,2,8,6,5])
vec2=np.array([2,7,4,6,0,1])

print(vec1+vec2)
print(vec1*vec2)
#2d array

vec3=np.array([[1,2,3],[4,5,6]])
vec4=np.array([[0,9],[6,7],[6,3]])
#print(vec3+vec4)
print(np.matmul(vec3,vec4))