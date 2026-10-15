import numpy as np

a=np.arange(6)
print(a)
print(a.shape)

a2=a[np.newaxis, : ]
print(a2.shape)

a3=a[: ,np.newaxis]
print(a3.shape)

b=np.expand_dims(a,axis=0)
print(b.shape)