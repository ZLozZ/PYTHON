import pandas as pd
import random

def TBTK(n):
    TB = []
    for i in range(0, len(n)):
        TB.append(round((n.loc[i, 'TK1'] + n.loc[i, 'TK2'] + n.loc[i, 'TK3'])/3, 1))
    n['TBTK'] = pd.Series(TB)

def create_scores(df):
    diem = []
    for i in range(0, len(df)):
        diem.append(round(random.uniform(1, 10), 1))
    return diem

def add_colums(n):
    n['GK'] = pd.Series(create_scores(n))
    n['CK'] = pd.Series(create_scores(n))

def Save_file(n):
    n.to_csv('Book2.csv', index = False)

def Create_TBM(n):
    TB = []
    for i in range(0, len(n)):
        if n.loc[i, 'GK'] >= 1 and n.loc[i, 'CK'] >= 3:
            TB.append(round(n.loc[i, 'TBTK']*0.2 + n.loc[i, 'GK']*0.3 + n.loc[i, 'CK']*0.5, 1))
        else:
            TB.append(0.0)
    n['TBM'] = pd.Series(TB)

df = pd.read_csv('Book1.csv')
TBTK(df)
add_colums(df)
Save_file(df)
Create_TBM(df)
print(df)