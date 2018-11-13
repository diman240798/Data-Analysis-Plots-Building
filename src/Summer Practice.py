import matplotlib.pyplot as plt
from pandas import read_csv
from src.Team import Team
from src.Team import checkWinnerBullit
from src.Team import checkWinnerOver
from src.Team import checkWinnerUsual

df1 = read_csv("khl_2017_18.csv")

sTeam1 = df1.Команда_1
sTeam2 = df1.Команда_2
sOver = df1.Овертайм
sPer1 = df1.Период_1
sPer2 = df1.Период_2
sPer3 = df1.Период_3
sBullit = df1.Буллиты
sDate = df1.Дата

teams = {}

for x in range(0, len(sTeam1)):
    team1Name = sTeam1[x]
    team2Name = sTeam2[x]
    over = sOver[x]
    bullit = sBullit[x]
    per1 = sPer1[x]
    per2 = sPer2[x]
    per3 = sPer3[x]
    date = sDate[x]

    team1 = teams.get(team1Name, Team())
    team2 = teams.get(team2Name, Team())
    checkWinnerBullit(bullit, team1, team2, date)
    checkWinnerOver(over, team1, team2, date)
    checkWinnerUsual(per1, team1, team2, date)
    checkWinnerUsual(per2, team1, team2, date)
    checkWinnerUsual(per3, team1, team2, date)
    teams[team1Name] = team1
    teams[team2Name] = team2

a = 5

fig = plt.figure(num=None, figsize=(50, 10), dpi=80, facecolor='w', edgecolor='k')
# ax1 = plt.subplot2grid((1, 5), (0, 0), colspan=1000, rowspan=1000)

teams_get = teams.get('СКА')
score = teams_get.dateScore
keys = list(score.keys())[:20]
values = list(score.values())[:20]


plt.plot(score.keys(), score.values())

plt.show()
a = 6
