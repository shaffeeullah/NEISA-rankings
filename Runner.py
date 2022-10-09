import rank_calculator
import csv

schoolslink = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR4d8JvuxteLJ7NqAvZhjYzRggjV_ptKUQCNNsQAVrblK9r2h3CFovSODtSpg7Jp7_xt0lFdLjxUedQ/pub?output=csv"
coedRegattaLink = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSwVtHxq6LONV5TiX73WF1xaCDk93xnsFz7Vh6VisLJFJIg6MpvsVNDCoOe-XcBc6h1cu1SC6_HYPVM/pub?output=csv"
womensRegattaLink = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRrN9Sdev0TpLnAzuUgPQFwEa_VXcmsXX9CKoR3Y5p4fFydyh8WwdM1Xx-yaOWobLlNYPYWUMjGql1w/pub?output=csv"

coed_rankings_output_file = "rankings.csv"
coed_component_scores_file = "component_scores.csv"

womens_rankings_output_file = "womensrankings.csv"
womens_component_scores_file = "womens_component_scores.csv"

################## COED ######################
ranks, school_objects = rank_calculator.calculate_ranks(coedRegattaLink, schoolslink)

f = open(coed_rankings_output_file, "w")
f.truncate()
f.close()

with open(coed_rankings_output_file, 'w') as result:
    writer = csv.writer(result, delimiter=",")
    writer.writerow(('School', 'Score'))
    for row in ranks:
        row = (row[0], str(row[1]))
        writer.writerow(row)


f = open(coed_component_scores_file, "w")
f.truncate()
f.close()

with open(coed_component_scores_file, 'w') as result:
    writer = csv.writer(result, delimiter=",")
    writer.writerow(('School', 'Counted Scores Regular Regattas', 'Championship Score'))
    for school in school_objects:
        obje = school_objects[school]
        row = (obje.name, obje.counted_points, obje.s_regatta_score)
        writer.writerow(row)
######################################################


################### WOMENS ###########################
ranks, school_objects = rank_calculator.calculate_ranks(womensRegattaLink, schoolslink)

f = open(womens_rankings_output_file, "w")
f.truncate()
f.close()

with open(womens_rankings_output_file, 'w') as result:
    writer = csv.writer(result, delimiter=",")
    writer.writerow(('School', 'Score'))
    for row in ranks:
        row = (row[0], str(row[1]))
        writer.writerow(row)


f = open(womens_component_scores_file, "w")
f.truncate()
f.close()

with open(womens_component_scores_file, 'w') as result:
    writer = csv.writer(result, delimiter=",")
    writer.writerow(('School', 'Counted Scores Regular Regattas', 'Championship Score'))
    for school in school_objects:
        obje = school_objects[school]
        row = (obje.name, obje.counted_points, obje.s_regatta_score)
        writer.writerow(row)
