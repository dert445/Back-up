import pandas as pd


df=pd.read_csv('data.csv')

#getting the shape and coloums name
'''print(df.shape)
print(df.columns)'''

#print(df["Date"])

'''subset=df[['Pulse','Maxpulse']]
print(subset)'''

#Rows filtering
high_pulse=df[df['Pulse']>110]
print(high_pulse)