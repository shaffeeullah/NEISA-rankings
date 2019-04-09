import pandas as pd

# you have to publish to web
def readSheet(link):
    # r = requests.get(link)
    # data = r.content
    df = pd.read_csv(link, encoding = 'utf8')
    # df = pd.read_csv(BytesIO(data), index_col=0,parse_dates=['Type'])
    # regattas = pandas.read_csv(link)
    return df
#
# print(readSheet("https://docs.google.com/spreadsheets/d/e/2PACX-1vQfeyC1LeMtdi0qIz-GWxke3jPQ1jJzp72YNi_I9YXF1f73HXUBRTG7AqePHI_L5X54HVwAofxueTiO/pub?output=csv"))
#
#
# schoolslink = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQfU-xYwtTc9nlW_tpsEmk-TMlUqsvzLooC8m3tcFnS7ig3lvWkA_b_2BxzUNGik8zq6IV-Lg9BwGSV/pub?output=csv"
# print(readSheet(schoolslink))
