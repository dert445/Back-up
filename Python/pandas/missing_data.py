import pandas as pd
import numpy as np

df=pd.read_csv("data.csv")
#finding the missing data
# print(df.isnull().sum())
# for droping the row
'''df.dropna(inplace=True)
print(df)'''
#filling the space
print(df.duplicated().sum())
df=df.drop_duplicates()
df['Calories']=df['Calories'].fillna(df['Calories'].mean())
#print(df)

# Drops the very first column (index 0)


df=df.drop(columns=["Date"])
#df.loc[0,'Date']='2020/12/01'
#df.loc[30,'Date']='2020/12/31'
tarik=pd.date_range(start='2020/12/01',periods=len(df),freq='D')

df.insert(1,'Date',tarik)

df.loc[7,"Duration"]=45
print(df)

df.to_csv('output.csv')
# df["Date"]=pd.to_numeric(pd.to_datetime(df['Date']))
# df["Date"]=df["Date"].interpolate(method='linear')
# df['Date']=pd.to_datetime(df['Date'])