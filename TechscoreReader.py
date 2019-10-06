import pandas

def getRegattaResultsAndNumTeams(regattaLink, regattaType):
    resultsTable = pandas.read_html(regattaLink, header=0, index_col=0)
    teams = list(resultsTable[0].Team)
    result = list(resultsTable[0].School)
    finishes = []
    for ind in range(len(teams)):
        team = teams[ind]
        if(regattaType == "special_A"):
            if (result[ind] not in finishes):
                finishes.append(result[ind])
        elif (any(i.isdigit() for i in team) and ("1" in team) or (not any(i.isdigit() for i in team))):
            finishes.append(result[ind])

    return (finishes, len(finishes))
