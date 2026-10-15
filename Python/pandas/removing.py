import pandas as pd
import numpy as np

df=pd.read_csv("data.csv")

df.drop(columns=["Pulse"],inplace=True)
print(df)