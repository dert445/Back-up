import pandas as pd
import numpy as np

df=pd.read_csv("output.csv",index_col=0)
#print(df.info())
df.columns = df.columns.str.strip()
df=df.sort_values(by='Pulse',ascending=False)
df=df.groupby("Duration")['Calories'].sum()
print(df)