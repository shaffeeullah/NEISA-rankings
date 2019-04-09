import pandas as pd
import numpy as np
import GoogleSheets
import TechscoreReader

class School:
    def __init__(self, name):
        self.name = name
        self.points = []
        self.SRegattaScore = 0
        self.countedPoints = [] #if this is empty then all the points are counted

    def addPoints(self,x):
        self.points.append(x)
        self.points = sorted(self.points, reverse=True)

    def getPointsTotal(self):
        if len(self.points) > 3:
            self.countedPoints = [self.points[0], self.points[1], self.points[2], self.points[3], self.SRegattaScore]
            return self.points[0] + self.points[1] + self.points[2] + self.points[3] + self.SRegattaScore
        else:
            total = 0
            for i in self.points:
                total += i
            return total + self.SRegattaScore

def calculateRankS(type, totalTeams, score):
    if (score == 0):
        return 0
    first = None
    last = None
    if type == "S":
        first = 10
        last = 5
    rankvalue = -1.0*(first-last) / (totalTeams-1) * (score-1) + first
    return rankvalue


def calculateRank(type, totalTeams, score):
    if score == 0:
        return 0
    first = None
    last = 0
    if type == "A":
        first = 8.5
    elif type == "B":
        first = 5.01
    elif type == "C":
        first = 4.16
    elif type == "WSC":
        first = 10.0
    elif type == "WA":
        first = 8.5
    elif type == "WB":
        first = 7.0
    elif type == "SC":
        first = 10.0
        last = 5.0
    elif type == "SC_alt":
        first = 4.8

    droprate = .005 * first
    amounttodrop = (18-totalTeams)*droprate
    first = first - amounttodrop
    rankvalue = -1.0 * (first-last) / (totalTeams-1) * (score-1) + first
    if (abs(rankvalue) < .003): rankvalue = 0.0
    return rankvalue

def enterScores(schoolobjects, data, type, totalTeams):
    data = list(data)
    seen = set()
    offset = 0
    for scoreind in range(len(data)):
        team = data[scoreind]
        if team in seen:
            offset += 1
            continue
        seen.add(team)
        score = calculateRank(type, totalTeams, scoreind+1-offset)
        if score < 0: print(score, scoreind, scoreind+1-offset, totalTeams, team, data)
        if totalTeams == 0:
            print("There are 0 total teams for a regatta of type ", type)
        if team in schoolobjects:
            schoolobjects[team].addPoints(score)

def enterSScores(schoolobjects, data, type, totalTeams):
    data = list(data)
    if type == "SC_A":
        type = "SC"
    elif type == "SC_B":
        type = "B"
    elif type == "WSC_A":
        type = "WSC"
    else:
        "AHHH you did something stupid"

    for scoreind in range(len(data)):
        team = data[scoreind]
        score = calculateRank(type, totalTeams, scoreind+1)
        if team in schoolobjects:
            if schoolobjects[team].SRegattaScore == 0:
                schoolobjects[team].SRegattaScore = score
            else:
                print("hmm you tried to add two s scores to the same school object")

def getRank(schoolobjects):
    tuplist = []
    for schoolname in schoolobjects:
        school = schoolobjects[schoolname]
        tuplist.append((school.name, school.getPointsTotal()))
    tuplist.sort(key=lambda x: x[1], reverse = True)
    return tuplist

def addSchoolObjects(schoolsLink):
    schools = GoogleSheets.readSheet(schoolsLink).Schools
    schoolobjects = {}
    for school in schools:
        schoolobjects[school] = School(school)
    return schoolobjects

def calculateRanks(regattaLink, schoolsLink):
    df = GoogleSheets.readSheet(regattaLink)
    # print(df)
    schoolobjects = addSchoolObjects(schoolsLink)
    for index, regatta in df.iterrows():
        regattaType = regatta.Type
        print(regatta.Link)
        regattaFinishes, totalTeams = TechscoreReader.getRegattaResultsAndNumTeams(regatta.Link)
        # print("new regatta", regattaType, regattaFinishes)
        if (regattaType == "SC_A"):
            enterSScores(schoolobjects, regattaFinishes, "SC_A", totalTeams)

        elif (regattaType == "WSC_A"):
            enterSScores(schoolobjects, regattaFinishes, "WSC_A", totalTeams)

        elif (regattaType == "SC_B"):
            enterSScores(schoolobjects, regattaFinishes, "SC_B", totalTeams)

        elif (regattaType == "A"): #TODO: this still bumps single handeds up to 18 boats
            if (totalTeams < 18):
                totalTeams = 18
            enterScores(schoolobjects, regattaFinishes, "A", totalTeams)

        elif (regattaType == "WSC"):
            enterScores(schoolobjects, regattaFinishes, "WSC", totalTeams)

        elif (regattaType == "B"):
            enterScores(schoolobjects, regattaFinishes, "B", totalTeams)

        elif (regattaType == "C"):
            enterScores(schoolobjects, regattaFinishes, "C", totalTeams)

        elif (regattaType == "WA"):
            enterScores(schoolobjects, regattaFinishes, "WA", totalTeams)

        elif (regattaType == "WB"):
            enterScores(schoolobjects, regattaFinishes, "WB", totalTeams)

        elif (regattaType == "SC"):
            enterScores(schoolobjects, regattaFinishes, "SC", totalTeams)

        elif (regattaType == "SC_alt"):
            enterScores(schoolobjects, regattaFinishes, "SC_alt", totalTeams)
        else:
            print("something is wrong ")

    toreturn = getRank(schoolobjects)

    for school in schoolobjects:
        #print(obje.points)
        obje = schoolobjects[school]
        print(obje.name, obje.countedPoints)

    return toreturn


# ranks = calculateRanks("WomensNow.csv")
# ranks = calculateRanks("CoedNow.csv")


######UNCOMMENT BELOW TO FIGURE OUT RANKS
# for i in ranks:
#     print(i[0])
#
# for i in ranks:
#     print(i[1])


#
# totalteams = 18
# while totalteams >= 18:
#     print("for teams:", totalteams)
#     for i in range(totalteams+1):
#         print(calculateRank("SC_alt", totalteams, i))
#     totalteams = totalteams - 1
