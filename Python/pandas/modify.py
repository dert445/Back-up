import pandas as pd
import numpy as np

df=pd.read_csv("data.csv")

# print(df.info())

#adding columns
# condition=np.random.randint(50,71)
# df.insert(3,"Min Pulse",condition)

# print(df)

df.loc[22,"Date"]="'2020/12/22'"
df.loc[26,"Date"]="'2020/12/26'"

df.loc[18,"Calories"]=df["Calories"].mean()
df.loc[28,"Calories"]=df["Calories"].mean()
print(df)


df.to_csv("output.csv")