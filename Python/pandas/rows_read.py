import pandas as pd

df=pd.read_csv('data.csv')
'''print("dispaly 10 rows of First")
print(df.head())
print("Displays 10 rows at Last")
print(df.tail())'''
#Cheacking for Basic Infornation
print(df.info())
#Cheacking for statistcal Infornation
print(df.describe())

