import pandas

def getRegattaResultsAndNumTeams(regattaLink):
    resultsTable = pandas.read_html(regattaLink, header=0, index_col=0)
    # print(resultsTable[0].Team)
    results = resultsTable[0].School
    num_teams = len(set(results))
    return (results, num_teams)
