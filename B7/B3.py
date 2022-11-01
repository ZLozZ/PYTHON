from cProfile import label
import pandas as pd
import matplotlib 

def Box(df):
    df[['TK1', 'TK2', 'TK3', 'GK', 'CK']].plot.box()
    matplotlib.pyplot.show()

def Histogram(df):
    df[['TK1']].plot.hist()
    matplotlib.pyplot.show()
    df[['TK2']].plot.hist()
    matplotlib.pyplot.show()
    df[['TK3']].plot.hist()
    matplotlib.pyplot.show()
    df[['GK']].plot.hist()
    matplotlib.pyplot.show()
    df[['CK']].plot.hist()
    matplotlib.pyplot.show()

df = pd.read_csv('Book2.csv')
Box(df)
Histogram(df)
print("Điểm trung bình thường kì 1 lớp")
print(df['TK1'].sum()/len(df))
print("Điểm trung bình thường kì 2 lớp")
print(df['TK2'].sum()/len(df))
print("Điểm trung bình thường kì 3 lớp")
print(df['TK3'].sum()/len(df))
print("Điểm trung bình giữa kì lớp")
print(round(df['GK'].sum()/len(df), 1))
print("Điểm trung bình cuối kì lớp")
print(df['CK'].sum()/len(df))

