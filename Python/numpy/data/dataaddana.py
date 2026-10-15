import numpy as np
import matplotlib.pyplot as plt


total=2000
sales_data=np.array([
    [1,200],
    [2,180],
    [3,150],
    [4,100],
    [5,250]
])
print(sales_data.shape)
print(np.sum(sales_data[0:5,1],axis=0))
print(np.min(sales_data[:,1],axis=0))
print(np.max(sales_data[:,1],axis=0))

#plot graph

plt.figure(figsize=(16,10))
plt.plot(sales_data[:,1])
plt.title("data for expendaure")
plt.xlabel("days")
plt.ylabel("expendature")
plt.grid(True)
plt.show()