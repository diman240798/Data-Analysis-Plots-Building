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
        l.append(str(self.games))
        l.append(str(self.victories))
        l.append(str(self.victoriesBullit))
        l.append(str(self.victoriesOver))
        l.append(str(self.fails))
        l.append(str(self.failsBullit))
        l.append(str(self.failsOver) + '\n')
        return ','.join(l)

