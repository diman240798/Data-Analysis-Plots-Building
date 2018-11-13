class Team:
    def __init__(self):
        self.games = 0
        self.victories = 0
        self.victoriesOver = 0
        self.victoriesBullit = 0
        self.fails = 0
        self.failsOver = 0
        self.failsBullit = 0
        self.scoreSum = 0
        self.dateScoreSum = {}

    def __str__(self, name) -> str:
        l = list()
        l.append(name)
        l.append(str(self.victories))
        l.append(str(self.victoriesBullit))
        l.append(str(self.victoriesOver))
        l.append(str(self.fails))
        l.append(str(self.failsBullit))
        l.append(str(self.failsOver) + '\n')
        return ','.join(l)


def checkWinnerBullit(string, team1, team2, date):
    split = string.split(":")
    if (split[0] == '' or len(split) < 2):
        return

    checkWinnerUsual(string, team1, team2, date)

    result1 = int(split[0])
    result2 = int(split[1])

    if (result1 > result2):

        team1.victoriesBullit += 1
        team2.failsBullit += 1
    else:
        team2.victoriesBullit += 1
        team1.failsBullit += 1


def checkWinnerOver(string, team1, team2, date):
    split = string.split(":")
    if (split[0] == '' or len(split) < 2):
        return

    checkWinnerUsual(string, team1, team2, date)

    result1 = int(split[0])
    result2 = int(split[1])

    if (result1 > result2):

        team1.victoriesOver += 1
        team2.failsOver += 1
    else:
        team2.victoriesOver += 1
        team1.failsOver += 1


def checkWinnerUsual(string, team1, team2, date):
    split = string.split(":")
    if (split[0] == '' or len(split) < 2):
        return

    result1 = int(split[0])
    result2 = int(split[1])

    team1.games += 1
    team2.games += 1
    if (result1 > result2):
        curScore = team1.scoreSum
        team1.dateScoreSum[date] = curScore + result1

        team1.victories += 1
        team2.fails += 1
    else:
        curScore = team2.scoreSum
        team2.dateScoreSum[date] = curScore + result2

        team2.victories += 1
        team1.fails += 1
