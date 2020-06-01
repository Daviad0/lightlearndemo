import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

df = pd.read_csv('test3.csv')
model = LogisticRegression()
def fitthemodel():
    XT = df[['BlueA', 'BlueT', 'BlueE', 'RedA', 'RedT', 'RedE']].values
    yt = df['BlueWin'].values
    model.fit(XT, yt)


#Training Data

XP = [[0,0,0,0,0,0]]
while True:
    fitthemodel()
    XP[0][0] = float(input("Blue Autonomous Score: "))
    XP[0][1] = float(input("Blue Teleop Score: "))
    XP[0][2] = float(input("Blue Endgame Score: "))
    XP[0][3] = float(input("Red Autonomous Score: "))
    XP[0][4] = float(input("Red Teleop Score: "))
    XP[0][5] = float(input("Red Endgame Score: "))
    y_pred = model.predict(XP)
    if(y_pred == 1):
        print("Blue Wins\n\n")
    else:
        print("Red Wins\n\n")
    actualwinner = input("Who actually won (1 or 0 based on algorithm, 2 to not include): ")
    if(actualwinner != "2"):
        csvfile = open("test3.csv", "a")
        csvfile.write("\n" + str(XP[0][0]) + "," + str(XP[0][1]) + "," + str(XP[0][2]) + "," + str(XP[0][3]) + "," + str(XP[0][4]) + "," + str(XP[0][5]) + "," + actualwinner)
        csvfile.close()
    print("\n\n")
    


yc = [0,1,0]

coolscorevariable = model.score(XP, yc)
print(y_pred)

print("Score: " + str(coolscorevariable))