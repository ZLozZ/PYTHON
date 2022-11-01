from tensorflow.keras.models import load_model
import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt

model = load_model('Train.abc')

#chuẩn bị Data
data = pd.read_csv('Result.csv')
X = data.iloc[:,:5].values
Y = data.iloc[:,5:].values

Y_guess = model.predict(X)

fig, ax = plt.subplots()
print(Y_guess)
ax.plot(Y_guess[:, 1],label='Dogcoin_guess')

ax.plot(Y[:, 1], label='Dogcoin')
ax.legend()
ax.set_title("DOG_COIN")
ax.set_ylabel('USDT')
ax.set_xlabel('Minute')
plt.show()