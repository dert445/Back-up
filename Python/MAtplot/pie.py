import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.read_csv("data.csv",index_col=0)
month=df["Month"]
val=df["Online_Sales"]
plt.pie(val,labels=month,autopct='%.2f%%',explode=[0,0,.2,0,0,.1,0,0,0,.5,.2,0],shadow=True)
plt.show()