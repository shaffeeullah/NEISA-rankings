import pandas as pd
import numpy as np
import google_sheets
import techscore_reader
import csv

class School:
    def __init__(self, name):
        self.name = name
        self.points = []
        self.s_regatta_score = (0, None)
        self.counted_points = [] #if this is empty then all the points are counted

    def add_points(self,x,regatta_name):
        self.points.append((round(x, 2), regatta_name))
        self.points = sorted(self.points, key=lambda x: x[0], reverse=True)

    def get_points_total(self):
        if len(self.points) > 3:
            self.counted_points = [self.points[0], self.points[1], self.points[2], self.points[3]]
        else:
            self.counted_points = self.points

        return sum([pair[0] for pair in self.counted_points]) + self.s_regatta_score[0]

def calculate_rank(type, total_teams, score):
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
    elif type == "WB" or type == "A-":
        first = 7.0
    elif type == "SC":
        first = 10.0
        last = 5.0
    elif type == "SC_alt":
        first = 7

    droprate = .005 * first
    amounttodrop = (18-total_teams)*droprate
    first = first - amounttodrop
    rankvalue = -1.0 * (first-last) / (total_teams-1) * (score-1) + first
    if (abs(rankvalue) < .003): rankvalue = 0.0
    return rankvalue

def enter_scores(school_objects, data, type, total_teams, regatta_name):
    data = list(data)
    for scoreind in range(len(data)):
        team = data[scoreind]
        score = calculate_rank(type, total_teams, scoreind+1)
        if team in school_objects:
            school_objects[team].add_points(score, regatta_name)

def enter_s_scores(school_objects, data, type, total_teams, regatta_name):
    data = list(data)
    if type == "SC_A":
        type = "SC"
    elif type == "SC_B":
        type = "B"
        if (total_teams < 18):
            total_teams = 18
    elif type == "WSC_A": #TODO: why was it WSC_A in the first place? why not just WSC?
        type = "WSC"
    else:
        print("enter_s_scores doesnt understand the regatta type")

    for scoreind in range(len(data)):
        team = data[scoreind]
        score = calculate_rank(type, total_teams, scoreind+1)
        if team in school_objects:
            if school_objects[team].s_regatta_score[0] == 0:
                school_objects[team].s_regatta_score = (round(score, 2), regatta_name)
            else:
                print("hmm you tried to add two s scores to the same school object")

def get_rank(school_objects):
    tuplist = []
    for school_name in school_objects:
        school = school_objects[school_name]
        tuplist.append((school.name, school.get_points_total()))
    tuplist.sort(key=lambda x: x[1], reverse = True)
    return tuplist

def add_school_objects(schools_link):
    schools = google_sheets.read_sheet(schools_link).Schools
    school_objects = {}
    for school in schools:
        school_objects[school] = School(school)
    return school_objects

def calculate_ranks(regatta_link, schools_link):
    df = google_sheets.read_sheet(regatta_link)
    school_objects = add_school_objects(schools_link)
    for index, regatta in df.iterrows():
        regatta_type = regatta.Type
        regatta_finishes, total_teams = techscore_reader.get_regatta_results_and_num_teams(regatta.Link, regatta_type)
        lateDrops = regatta.LateDrops
        if not pd.isnull(lateDrops):
            total_teams += lateDrops
        regatta_name = (regatta.Link.split("/"))[-2]
        if regatta_type in ("SC_A", "WSC_A", "SC_B"):
            enter_s_scores(school_objects, regatta_finishes, regatta_type, total_teams, regatta_name)
            continue

        if (regatta_type == "A") and (total_teams < 18):
            total_teams = 18

        if (regatta_type == "B") and (total_teams < 16):
            total_teams = 16

        if regatta_type == "special_A": #sidesteps the total team minimum
            regatta_type = "A"

        #TODO: where is the WSC one the line below coming from?
        regattaTypes = ["A", "special_A", "A-", "WSC", "B", "C", "WA", "WB", "SC", "SC_alt"]
        if regatta_type not in regattaTypes:
            print("Regatta type " + regatta_type + " is incorrect for " + regatta.Link)
            print("Possible regatta type options for this regatta are: " + str(regattaTypes))
            continue

        enter_scores(school_objects, regatta_finishes, regatta_type, total_teams, regatta_name)

    return (get_rank(school_objects), school_objects)


def calculate_score_table(total_teams_maximum, total_teams_minimum, regatta_type):
    total_teams = total_teams_maximum
    while total_teams >= total_teams_minimum:
        print("for teams:", total_teams)
        for i in range(1, total_teams+1):
            print(calculate_rank(regatta_type, total_teams, i))
        total_teams = total_teams - 1
