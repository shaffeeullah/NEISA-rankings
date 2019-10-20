import RankCalculator
import csv

schoolslink = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR4d8JvuxteLJ7NqAvZhjYzRggjV_ptKUQCNNsQAVrblK9r2h3CFovSODtSpg7Jp7_xt0lFdLjxUedQ/pub?output=csv"
coedRegattaLink = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRYuBfRn534EQy6tXw957Ree0IPLUxyaFri25OQtd_0n5SyG3J-5ELfpUPgwUKGxT_qfDmzrmtds8Y2/pub?output=csv"
womensRegattaLink = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRrN9Sdev0TpLnAzuUgPQFwEa_VXcmsXX9CKoR3Y5p4fFydyh8WwdM1Xx-yaOWobLlNYPYWUMjGql1w/pub?output=csv"

coedRankingsOutputFile = "rankings.csv"
coedComponentScoresFile = "component_scores.csv"

womensRankingOutputFile = "womensrankings.csv"
womensComponentScoresFile = "womens_component_scores.csv"

################## COED ######################
ranks, schoolobjects = RankCalculator.calculateRanks(coedRegattaLink, schoolslink)

f = open(coedRankingsOutputFile, "w")
f.truncate()
f.close()

with open(coedRankingsOutputFile, 'w') as result:
    writer = csv.writer(result, delimiter=",")
    writer.writerow(('School', 'Score'))
    for row in ranks:
        row = (row[0], str(row[1]))
        writer.writerow(row)


f = open(coedComponentScoresFile, "w")
f.truncate()
f.close()

with open(coedComponentScoresFile, 'w') as result:
    writer = csv.writer(result, delimiter=",")
    writer.writerow(('School', 'Counted Scores Regular Regattas', 'Championship Score'))
    for school in schoolobjects:
        obje = schoolobjects[school]
        row = (obje.name, obje.countedPoints, obje.SRegattaScore)
        writer.writerow(row)
######################################################


################### WOMENS ###########################
ranks, schoolobjects = RankCalculator.calculateRanks(womensRegattaLink, schoolslink)

f = open(womensRankingOutputFile, "w")
f.truncate()
f.close()

with open(womensRankingOutputFile, 'w') as result:
    writer = csv.writer(result, delimiter=",")
    writer.writerow(('School', 'Score'))
    for row in ranks:
        row = (row[0], str(row[1]))
        writer.writerow(row)


f = open(womensComponentScoresFile, "w")
f.truncate()
f.close()

with open(womensComponentScoresFile, 'w') as result:
    writer = csv.writer(result, delimiter=",")
    writer.writerow(('School', 'Counted Scores Regular Regattas', 'Championship Score'))
    for school in schoolobjects:
        obje = schoolobjects[school]
        row = (obje.name, obje.countedPoints, obje.SRegattaScore)
        writer.writerow(row)
