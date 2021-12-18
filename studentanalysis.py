import pandas as pd 
import csv
import plotly.graph_objects as go 

df=pd.read_csv('gamedata.csv')
student=df.loc[df['student_id']=="TRL_987"]
print(student.groupby("level")["attempt"].mean())
graph=go.Figure(go.Bar(x=student.groupby("level")["attempt"].mean(), y=['level1', 'level2', 'level3', 'level4'],orientation='h'))
graph.show()