import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

df = pd.read_csv('MLB2.csv')
XT = df[['BA_PtsPC', 'BA_NumPC', 'BA_PercentPC', 'BA_InitLineChance', 'BT_PtsPC', 'BT_NumPC', 'BT_PercentPC', 'BT_CPSpinner', 'BT_CPRotator', 'BE_ParkChance', 'BE_ClimbChance', 'BE_BalanceChance', 'BD_SecDisabledAvg', 'RA_PtsPC', 'RA_NumPC', 'RA_PercentPC', 'RA_InitLineChance', 'RT_PtsPC', 'RT_NumPC', 'RT_PercentPC', 'RT_CPSpinner', 'RT_CPRotator', 'RE_ParkChance', 'RE_ClimbChance', 'RE_BalanceChance', 'RD_SecDisabledAvg']].values
#XP = df[['BA_PtsPC', 'BA_NumPC', 'BA_PercentPC', 'BA_InitLineChance', 'BT_PtsPC', 'BT_NumPC', 'BT_PercentPC', 'BT_CPSpinner', 'BT_CPRotator', 'BE_ParkChance', 'BE_ClimbChance', 'BE_BalanceChance', 'BD_SecDisabledAvg', 'RA_PtsPC', 'RA_NumPC', 'RA_PercentPC', 'RA_InitLineChance', 'RT_PtsPC', 'RT_NumPC', 'RT_PercentPC', 'RT_CPSpinner', 'RT_CPRotator', 'RE_ParkChance', 'RE_ClimbChance', 'RE_BalanceChance', 'RD_SecDisabledAvg']].values
yt = df['PtDifference'].values
model = LinearRegression()
model.fit(XT, yt)

XP = [[1.3,2,0.22,2,1.3,17,0.703,0,0,1,2,1,0,2.8,6,0.688,2.5,1.7,24,0.614,0,0,0.5,1.6,0.8,0]]
showdetails = []
yc = model.predict(XP)
print("-24 real score")
print(yc)
'''

i = 0
for c in yc:
    showdetails.append([c, 0])

for p in yt:
    showdetails[i][1] = p
    i = i + 1

for view in showdetails:
    print(view)

coolscorevariable = model.score(XP, yc)
print(y_pred)
print("Score: " + str(coolscorevariable))'''