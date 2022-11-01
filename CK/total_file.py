import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

name_col= ['DATE', 'PRICE_LAST', 'PRICE_HIGH', 'PRICE_LOW', 'PRICE_OPEN', 'TRADING_VOLUME']
data = pd.read_csv('DOGEUSDT-1m-2022-10-22.csv', names=name_col)
df = pd.DataFrame(data)
data1 = pd.read_csv('DOGEUSDT-1m-2022-10-21.csv', names=name_col)
df1 = pd.DataFrame(data1)
data2 = pd.read_csv('DOGEUSDT-1m-2022-10-20.csv', names=name_col)
df2 = pd.DataFrame(data2)
data3 = pd.read_csv('DOGEUSDT-1m-2022-10-19.csv', names=name_col)
df3 = pd.DataFrame(data3)
data4 = pd.read_csv('DOGEUSDT-1m-2022-10-18.csv', names=name_col)
df4 = pd.DataFrame(data4)
data5 = pd.read_csv('DOGEUSDT-1m-2022-10-17.csv', names=name_col)
df5= pd.DataFrame(data5)
data6 = pd.read_csv('DOGEUSDT-1m-2022-10-16.csv', names=name_col)
df6 = pd.DataFrame(data6)
df = df.append(df1, ignore_index=True)
df = df.append(df2, ignore_index=True)
df = df.append(df3, ignore_index=True)
df = df.append(df4, ignore_index=True)
df = df.append(df5, ignore_index=True)
df = df.append(df6, ignore_index=True)
df.to_csv('Result.csv',index=0)