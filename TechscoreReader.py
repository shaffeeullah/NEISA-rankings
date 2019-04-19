import pandas

def getRegattaResultsAndNumTeams(regattaLink):
    resultsTable = pandas.read_html(regattaLink, header=0, index_col=0)
    teams = list(resultsTable[0].Team)
    result = list(resultsTable[0].School)
    finishes = []
    for ind in range(len(teams)):
        team = teams[ind]
        if (any(i.isdigit() for i in team) and ("1" in team) or (not any(i.isdigit() for i in team))):
            finishes.append(result[ind])

    return (finishes, len(finishes))


# regattaLink = "https://scores.collegesailing.org/f18/hatch-brown/"
# getRegattaResultsAndNumTeams(regattaLink)
