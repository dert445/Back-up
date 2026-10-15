import matplotlib.pyplot as plt
import numpy as np
import math
p=math.pi
x=np.linspace(-p,p,50000)

y=np.sin(x)

plt.plot(x,y)
#plt.plot(x,y1)

plt.show()