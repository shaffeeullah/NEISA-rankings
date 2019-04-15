import pandas

def getRegattaResultsAndNumTeams(regattaLink):
    resultsTable = pandas.read_html(regattaLink, header=0, index_col=0)
    results = resultsTable[0].School
    num_teams = len(set(results))
    return (results, num_teams)
