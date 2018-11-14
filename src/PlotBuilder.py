import json
import matplotlib.pyplot as plt
import src.Config as Config


def plotByTeamName(name):
    with open(Config.resultFolder + '/graphsData.json', 'r') as f:
        line = f.readline()
        all = json.loads(line)
        for x in all:
            object = x['name']
            for x in object.keys():
                if (x == name):
                    dateScoredWrapped = object[x]
                    dateScore = dateScoredWrapped['dateScore']
                    fig = plt.figure(num=None, figsize=(80, 10), dpi=80, facecolor='w', edgecolor='k')
                    plt.title(name, fontsize=70, fontweight=3, color='blue', loc='center')
                    plt.xlabel('Score', fontsize=40, color='red')
                    plt.ylabel('Date', fontsize=40, color='violet')
                    plt.plot(dateScore.keys(), dateScore.values(), linewidth=10.0)
                    plt.savefig(Config.resultFolder + '/plot/' + name +'.png')
                    plt.show()
                    return
    print("No team with such name")

