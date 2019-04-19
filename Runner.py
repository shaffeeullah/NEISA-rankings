import RankCalculator
import csv

schoolslink = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQfU-xYwtTc9nlW_tpsEmk-TMlUqsvzLooC8m3tcFnS7ig3lvWkA_b_2BxzUNGik8zq6IV-Lg9BwGSV/pub?output=csv"
coedRegattaLink = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQfeyC1LeMtdi0qIz-GWxke3jPQ1jJzp72YNi_I9YXF1f73HXUBRTG7AqePHI_L5X54HVwAofxueTiO/pub?output=csv"
womensRegattaLink = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQfeyC1LeMtdi0qIz-GWxke3jPQ1jJzp72YNi_I9YXF1f73HXUBRTG7AqePHI_L5X54HVwAofxueTiO/pub?output=csv"

coedRankingsOutputFile = "rankings.csv"
coedComponentScoresFile = "component scores.csv"

womensRankingOutputFile = "womensrankings.csv"
womensComponentScoresFile = "womens component scores.csv"

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
