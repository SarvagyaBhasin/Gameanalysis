import pandas as pd 
import csv
import plotly.graph_objects as go 

df=pd.read_csv('gamedata.csv')
print(df.groupby("level")["attempt"].mean())
graph=go.Figure(go.Bar(x=df.groupby("level")["attempt"].mean(), y=['level1', 'level2', 'level3', 'level4'],orientation='h'))
graph.show()