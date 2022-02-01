import pandas
import termcolor
from termcolor import colored, cprint

def get_regatta_results_and_num_teams(regatta_link, regatta_type):
    results_table = ""
    try:
        results_table = pandas.read_html(regatta_link, header=0, index_col=0)
    except:
        cprint(colored("REGATTA LINK IS BROKEN: " + regatta_link), 'red')
        return
    teams = list(results_table[0].Team)
    result = list(results_table[0].School)
    finishes = []
    for ind in range(len(teams)):
        team = teams[ind]
        if(regatta_type == "special_A"):
            if (result[ind] not in finishes):
                finishes.append(result[ind])
        elif (any(i.isdigit() for i in team) and ("1" in team) or (not any(i.isdigit() for i in team))):
            finishes.append(result[ind])

    return (finishes, len(finishes))
