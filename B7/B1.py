import numpy as np
import random
import pandas as pd

def Create_series():
    ds = []
    for i in range(0, 35):
        ds.append(random.randint(1, 9))
    ds = np.array(ds)
    S = pd.Series(ds)
    return S

def head_tail(n):
    print("5 dòng dữ liệu đầu tiên:")
    print(n.head(5))
    print("5 dòng dữ liệu cuối cùng:")
    print(n.tail(5))

series_ptu = Create_series()
print("Serial vừa tạo:")
print(series_ptu)
head_tail(series_ptu)
print("In danh sách các phần tử của series theo dạng array:")
print(series_ptu.values)
print("In ra màn hình thông tin thống kê chung:")
print(series_ptu.describe())
print("In ra màn hình tổng của các phần tử có trong series:")
print(series_ptu.sum())
print("In ra màn hình phần tử có tần suất xuất hiện nhiều nhất trong series:")
print(series_ptu.mode())


    
