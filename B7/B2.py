from operator import index
import pandas as pd
import random

def TBTK(n):
    TB = []
    for i in range(0, len(n)):
        TB.append(round((n.loc[i, 'TK1'] + n.loc[i, 'TK2'] + n.loc[i, 'TK3'])/3, 1))
    n['TBTK'] = pd.Series(TB)

def Create_TBM(n):
    TB = []
    for i in range(0, len(n)):
        if n.loc[i, 'GK'] >= 1 and n.loc[i, 'CK'] >= 3:
            TB.append(round(n.loc[i, 'TBTK']*0.2 + n.loc[i, 'GK']*0.3 + n.loc[i, 'CK']*0.5, 1))
        else:
            TB.append(0.0)
    n['TBM'] = pd.Series(TB)

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

def add_colums_PF(n):
    GC = []
    for i in range(0, len(n)):
        if n.loc[i, 'TBM'] >= 4:
            GC.append("PASS")
        else:
            GC.append("FALL")
    n['GhiChu'] = pd.Series(GC) 

def find_Max(n):
    k = pd.read_csv('Pass.csv')
    diem  = k['TBM'].max()
    print(k[['STT', 'TBM']].loc[k['TBM']==diem])
    

df = pd.read_csv('Book1.csv')
print("5 Dòng đầu tiên")
print(df.head(5))
TBTK(df)
add_colums(df)
Create_TBM(df)
add_colums_PF(df)
Save_file(df)
print("                           DANH SÁCH CÁC BẠN ĐẬU")
ps = df.loc[df['TBM'] >= 4]
ps.to_csv('Pass.csv', index = False)
print(ps)
print("                           DANH SÁCH CÁC BẠN RỚT")
fl = df.loc[df['TBM'] < 4]
fl.to_csv('Fall.csv', index = False)
print(fl)
print("                       THÔNG TIN BẠN CÓ ĐIỂM CAO NHẤT")
find_Max(ps)