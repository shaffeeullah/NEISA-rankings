import pandas as pd

def readSheet(link):
    df = pd.read_csv(link, encoding = 'utf8')
    return df
