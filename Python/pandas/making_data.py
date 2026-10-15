import pandas as pd

data={
    "Name":['Ram','Rahim','Ratan'],
    "Age":[10,100,1000],
    "Class":['Garbage','Shit','Sleep']
}

df=pd.DataFrame(data)
print(df)

#df.to_csv("output.csv",index=False)
#Changing to Excel File
'''df.to_excel("output.xlsx")'''
df.to_json("output.json")