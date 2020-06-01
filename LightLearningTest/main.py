import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

df = pd.read_csv('test2.csv')
XT = df[['BlueA', 'BlueT', 'BlueE', 'RedA', 'RedT', 'RedE']].values
yt = df['BlueWin'].values
model = LogisticRegression()
model.fit(XT, yt)
XP = [[20,20,20,20,30,20],[40,50,10,30,20,20],[20,30,10,30,30,30]]
yc = [0,1,0]
y_pred = model.predict(XP)
coolscorevariable = model.score(XP, yc)
print(y_pred)
print("Score: " + str(coolscorevariable))