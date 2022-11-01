import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('Result.csv')
df = pd.DataFrame(data)
Name_Iphone= np.array(data['Ten Iphone'].astype(str))
data_tgdd=np.array(data['Gia Thegioididong'].astype(str))
data_fpt=np.array(data['Gia FPT'].astype(str))
data_viettel=np.array(data['Gia ViettleStore'].astype(str))

plt.plot(Name_Iphone,data_tgdd,color = 'b', ls = '--', marker = 's')
plt.plot(Name_Iphone,data_fpt,color = 'r', ls = '--', marker = 's')
plt.plot(Name_Iphone,data_viettel,color = 'k', ls = '-', marker = 's')
plt.legend(['TheGioiDiDong','FPT','ViettelStore'])
plt.show()
