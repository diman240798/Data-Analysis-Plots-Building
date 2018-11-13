class Team:
    name = ""
    games = 0
    victories = 0
    victoriesOver = 0
    victoriesBullit = 0
    fails = 0
    failsOver = 0
    failsBullit = 0
    dateScore = {}


    def __str__(self) -> str:
        return self.name

def whoWon(string):
    score1, score2 = string.split(':')
    a = int(score1) - int(score2) > 0
    return a


def checkWinnerBullit(string, team1, team2, date):
    split = string.split(":")
    if (split[0] == '' or len(split) < 2):
        return

    checkWinnerUsual(string, team1, team2, date)

    result1 = int(split[0])
    result2 = int(split[1])

    if (result1 > result2):
        curScore = team1.dateScore.get(date, 0)
        team1.dateScore[date] = curScore + result1

        team1.victoriesBullit = team1.victoriesBullit + 1
        team2.failsBullit = team2.failsBullit + 1
    else:
        curScore = team2.dateScore.get(date, 0)
        team2.dateScore[date] = curScore + result2

        team2.victoriesBullit = team2.victoriesBullit + 1
        team1.failsBullit = team1.failsBullit + 1


def checkWinnerOver(string, team1, team2, date):
    split = string.split(":")
    if (split[0] == '' or len(split) < 2):
        return

    checkWinnerUsual(string, team1, team2, date)

    result1 = int(split[0])
    result2 = int(split[1])

    if (result1 > result2):
        curScore = team1.dateScore.get(date, 0)
        team1.dateScore[date] = curScore + result1

        team1.victoriesOver = team1.victoriesOver + 1
        team2.failsOver = team2.failsOver + 1
    else:
        curScore = team2.dateScore.get(date, 0)
        team2.dateScore[date] = curScore + result2

        team2.victoriesOver = team2.victoriesOver + 1
        team1.failsOver = team1.failsOver + 1


def checkWinnerUsual(string, team1, team2, date):
    split = string.split(":")
    if (split[0] == '' or len(split) < 2):
        return

    result1 = int(split[0])
    result2 = int(split[1])

    if (result1 > result2):
        curScore = team1.dateScore.get(date, 0)
        team1.dateScore[date] = curScore + result1

        team1.victories = team1.victories + 1
        team2.fails = team2.fails + 1
    else:
        score = team2.dateScore
        curScore = score.get(date, 0)
        team2.dateScore[date] = curScore + result2

        team2.victories = team2.victories + 1
        team1.fails = team1.fails + 1
