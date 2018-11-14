import json
import os
from pandas import read_csv
from src.Team import Team
from src.Team import checkWinnerBullit
from src.Team import checkWinnerOver
from src.Team import checkWinnerUsual
import src.Config as Config


def examineCSVbyName(name):
    df1 = read_csv(name)

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

    with open(Config.resultFolder + '/examined.csv', 'w+') as f:
        f.write('Имя,Игры,Победы,ПобедыБуллит,ПобедыОвер,Поражения,ПораженияБуллит,ПораженияОвер\n')
        for k in teams.keys():
            f.write(teams[k].__str__(k))

    with open(Config.resultFolder + '/graphsData.json', 'w+') as f:
        f.write('[')
        for k in teams.keys():
            dateScore = {'dateScore': teams[k].dateScoreSum}
            unnamed = {k: dateScore}
            named = {'name': unnamed}
            f.write(json.dumps(named, ensure_ascii=False) + ',')
        f.seek(f.tell() - 1, os.SEEK_SET)
        f.write(']')
