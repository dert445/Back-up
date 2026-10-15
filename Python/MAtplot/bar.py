import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.read_csv("data.csv",index_col=0)
month=df["Month"]
val=df["Online_Sales"]
plt.bar(month,val)
plt.show()