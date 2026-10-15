import matplotlib.pyplot as plt
import numpy as np


x=np.random.randint(1,100000,size=10)
y=np.random.randint(20,100000,size=10)

plt.scatter(x,y)
plt.show()