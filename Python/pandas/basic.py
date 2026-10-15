import pandas as pd

#reading CSV file into the data frame
'''df=pd.read_csv("data.csv",encoding="UTF-8")
print(df)'''

#reading Json file
df1=pd.read_json("dot_features.json")
print(df1)