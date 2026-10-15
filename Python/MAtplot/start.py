import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,4,1,4])
y=np.array([4,4,1,1])
y1=np.array([1,2,6,9])
line_style=dict(marker='.',markersize=10,markerfacecolor="#750e0e",linestyle="dashdot",linewidth=3,color="#1d7310")
# plt.plot(x,y,**line_style)
plt.title("This is Z",fontsize=25,family='Arial',fontstyle="italic")
plt.xlabel("Base of Z")
plt.ylabel("baka dag of Z")
plt.xticks(x)
plt.yticks(y1)
plt.grid()
plt.plot(x,y,**line_style)
plt.show()