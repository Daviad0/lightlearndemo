import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

df = pd.read_csv('MLB2.csv')
XT = df[['BA_PtsPC', 'BA_NumPC', 'BA_InitLineChance', 'BT_PtsPC', 'BT_NumPC', 'BT_CPSpinner', 'BT_CPRotator', 'BE_ParkChance', 'BE_ClimbChance', 'BE_BalanceChance', 'BD_SecDisabledAvg', 'RA_PtsPC', 'RA_NumPC', 'RA_InitLineChance', 'RT_PtsPC', 'RT_NumPC', 'RT_CPSpinner', 'RT_CPRotator', 'RE_ParkChance', 'RE_ClimbChance', 'RE_BalanceChance', 'RD_SecDisabledAvg']].values
#XP = df[['BA_PtsPC', 'BA_NumPC', 'BA_PercentPC', 'BA_InitLineChance', 'BT_PtsPC', 'BT_NumPC', 'BT_PercentPC', 'BT_CPSpinner', 'BT_CPRotator', 'BE_ParkChance', 'BE_ClimbChance', 'BE_BalanceChance', 'BD_SecDisabledAvg', 'RA_PtsPC', 'RA_NumPC', 'RA_PercentPC', 'RA_InitLineChance', 'RT_PtsPC', 'RT_NumPC', 'RT_PercentPC', 'RT_CPSpinner', 'RT_CPRotator', 'RE_ParkChance', 'RE_ClimbChance', 'RE_BalanceChance', 'RD_SecDisabledAvg']].values
yt = df['PtDifference'].values
model = LinearRegression()
model.fit(XT, yt)

XP = [[2.8,6,2,1.7,24,0,0,1,2,1,0,2.4,6,2.3,1.8,24,1,0,0.7,2.2,1,0.2]]
showdetails = []
yc = model.predict(XP)
print("-45 real score")
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