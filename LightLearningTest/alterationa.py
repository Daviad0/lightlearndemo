import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

df = pd.read_csv('alterationa1.csv')
model = LogisticRegression()
model.max_iter = 12000
def fitthemodel():
    XT = df[['BlueAPCP_a', 'BlueAPC', 'BlueTPCP_a', 'BlueTPC', 'BlueCPC_c', 'BlueEIEP_a', 'RedAPCP_a', 'RedAPC', 'RedTPCP_a', 'RedTPC', 'RedCPC_c', 'RedEIEP_a']].values
    yt = df['BlueFinalDiff'].values
    model.fit(XT, yt)


#Training Data

XP = [[0,0,0,0,0,0,0,0,0,0,0,0]]
while True:
    fitthemodel()
    XP[0][0] = float(input("BlueAPCP_a: "))
    XP[0][1] = float(input("BlueAPC: "))
    XP[0][2] = float(input("BlueTPCP_a: "))
    XP[0][3] = float(input("BlueTPC: "))
    XP[0][4] = float(input("BlueCPC_c: "))
    XP[0][5] = float(input("BlueEIEP_a: "))
    XP[0][6] = float(input("RedAPCP_a: "))
    XP[0][7] = float(input("RedAPC: "))
    XP[0][8] = float(input("RedTPCP_a: "))
    XP[0][9] = float(input("RedTPC: "))
    XP[0][10] = float(input("RedCPC_c: "))
    XP[0][11] = float(input("RedEIEP_a: "))
    y_pred = model.predict(XP)
    if(y_pred > 0):
        print("Blue Wins by " + str(y_pred) +" points\n\n")
    elif(y_pred < 0):
        print("Red Wins by " + str(0-y_pred) +" points\n\n")
    else:
        print("Tie!")
    actualwinner = float(input("Who actually won by how much? (+ for blue, - for red): "))
    csvfile = open("alterationa1.csv", "a")
    csvfile.write("\n" + str(XP[0][0]) + "," + str(XP[0][1]) + "," + str(XP[0][2]) + "," + str(XP[0][3]) + "," + str(XP[0][4]) + "," + str(XP[0][5]) + "," + str(XP[0][6]) + "," + str(XP[0][7]) + "," + str(XP[0][8]) + "," + str(XP[0][9]) + "," + str(XP[0][10]) + "," + str(XP[0][11]) + "," + str(actualwinner))
    csvfile.close()
    print("\n\n")


#yc = [0,1,0]

#coolscorevariable = model.score(XP, yc)
#print(y_pred)

#print("Score: " + str(coolscorevariable))