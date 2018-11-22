import json
import os

from pandas import read_csv

import src.Config as Config
from model.Team import Team


def examineCSVbyName(fileName):
    df1 = read_csv(fileName)

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

        count = lambda x, y, z, n: int(x[n]) + int(y[n]) + int(z[n])
        firstScore = count(per1, per2, per3, 0)
        secondScore = count(per1, per2, per3, 2)

        if (firstScore == secondScore):

            count = lambda x, n: int(x[n])

            firstScore = count(over, 0)
            secondScore = count(over, 2)

            if (firstScore == secondScore):

                firstScore = count(bullit, 0)
                secondScore = count(bullit, 2)

                if (firstScore > secondScore):
                    team1.victoriesBullit += 1
                    team2.failsBullit += 1
                elif (secondScore > firstScore):
                    team2.victoriesBullit += 1
                    team1.failsBullit += 1

            elif (firstScore > secondScore):
                team1.victoriesOver += 1
                team2.failsOver += 1
            else:
                team2.victoriesOver += 1
                team1.failsOver += 1

        if (firstScore > secondScore):
            team1.scoreSum += 3
            team1.victories += 1
            team2.fails += 1
        elif (secondScore > firstScore):
            team2.scoreSum += 3
            team2.victories += 1
            team1.fails += 1

        team1.games += 1
        team2.games += 1

        team1.dateScoreSum[date] = team1.scoreSum
        team2.dateScoreSum[date] = team2.scoreSum

        teams[team1Name] = team1
        teams[team2Name] = team2

    with open(Config.resultFolder + '/examined.csv', 'w+') as f:
        f.write('Имя,Игры,Победы,ПобедыБуллит,ПобедыОвер,Поражения,ПораженияБуллит,ПораженияОвер\n')
        for k in teams.keys():
            f.write(teams[k].__str__(k))


    from data.Divisions import getBOBROV
    from data.Divisions import getTARASOV
    from data.Divisions import getHARLAMOV
    from data.Divisions import getCHERNISHEV

    fileNames = ['BOBROV', 'TARASOV', 'HARLAMOV', 'CHERNISHEV']
    divisions = [getBOBROV(), getTARASOV(), getHARLAMOV(), getCHERNISHEV()]
    resultFolder = Config.resultFolder + '/divisions/'

    createSortedCSV(divisions, fileNames, resultFolder)

    from data.Conferences import getWest
    from data.Conferences import getEast

    fileNames = ['WEST', 'EAST']
    conferences = [getWest(), getEast()]
    resultFolder = Config.resultFolder + '/conferences/'

    createSortedCSV(conferences, fileNames, resultFolder)


    with open(Config.resultFolder + '/graphsData.json', 'w+') as f:
        f.write('[')
        for k in teams.keys():
            dateScore = {'dateScore': teams[k].dateScoreSum}
            unnamed = {k: dateScore}
            named = {'name': unnamed}
            f.write(json.dumps(named, ensure_ascii=False) + ',')
        f.seek(f.tell() - 1, os.SEEK_SET)
        f.write(']')

def createSortedCSV(listOfteamNames, fileNames, resultFolder):
    import csv
    for x in range(0, len(fileNames)):
        fileName = fileNames[x]
        teamNames = listOfteamNames[x]
        filePath = resultFolder + fileName + '.csv'
        t = open(filePath, 'w+')
        t.close()
        with open(filePath, 'a') as f:
            with open(Config.resultFolder + '/examined.csv', 'r') as all_data:
                reader = csv.reader(all_data)
                csvHeader = next(reader)
                f.write(','.join(csvHeader))
                for row in reader:
                    for teamName in teamNames:
                        if (teamName in row):
                            f.write('\n' + ','.join(row))
