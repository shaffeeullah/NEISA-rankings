import pandas as pd

def read_sheet(link):
    df = pd.read_csv(link, encoding = 'utf8')
    return df
