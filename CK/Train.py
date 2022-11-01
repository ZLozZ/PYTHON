import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt
import tensorflow as tf

#chuẩn bị data
data = pd.read_csv('Result.csv')
X = data.iloc[:,:5].values
Y = data.iloc[:,5:].values

#chuẩn bị mô hình AI
model = Sequential()
model.add(Dense(1000, input_shape = (5,), activation='tanh'))
model.add(Dense(1500, activation ='tanh'))
model.add(Dense(2, activation = "linear"))

#thông tin mô hình
print(model.summary())

#chỉ tiêu đánh giá MSE (mean squared error), giải thuật huấn luyện "Adam"
model.compile(loss='mse', optimizer='Adam')

#train 10000 lần, 100 dữ liệu được đưa vào trong 1 lần train
model.fit(X, Y, epochs=10000, batch_size=100) 

model.save('Train.abc')