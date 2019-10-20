import pandas
import termcolor
from termcolor import colored, cprint

def getRegattaResultsAndNumTeams(regattaLink, regattaType):
    resultsTable = ""
    try:
        resultsTable = pandas.read_html(regattaLink, header=0, index_col=0)
    except:
        cprint(colored("REGATTA LINK IS BROKEN: " + regattaLink), 'red')
        return
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
