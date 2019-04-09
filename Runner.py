import RankCalculator

schoolslink = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQfU-xYwtTc9nlW_tpsEmk-TMlUqsvzLooC8m3tcFnS7ig3lvWkA_b_2BxzUNGik8zq6IV-Lg9BwGSV/pub?output=csv"
regattaLink = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQfeyC1LeMtdi0qIz-GWxke3jPQ1jJzp72YNi_I9YXF1f73HXUBRTG7AqePHI_L5X54HVwAofxueTiO/pub?output=csv"
ranks = RankCalculator.calculateRanks(regattaLink, schoolslink)

for i in ranks:
    print(i[0])

for i in ranks:
    print(i[1])
