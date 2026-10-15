import numpy as np
from io import StringIO as si
#delemeter
data="1,2,3,4\n4,5,9,8"
view=np.genfromtxt(si(data),delimiter=',')
print(view)

data1="1,2,3/n3445\n892"
view1=np.genfromtxt(si(data),delimiter=2)
print(view1)