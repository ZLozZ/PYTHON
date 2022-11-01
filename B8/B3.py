import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-4,4,0.1)
y = x**3 - 3*x
y1 = np.sin(x)

d= np.random.rand(100)
t = np.random.rand(100)

G = gridspec.GridSpec(2, 3)
axes_1 = plt.subplot(G[0, 0])
axes_1.plot(x,y,color = 'b', ls = '--', marker = 's')
plt.text(0.5, 0.5, '', ha='center', va='center', size=24, alpha=.5)
axes_2 = plt.subplot(G[0, 1])
axes_2.plot(x, y,color = 'r', ls = '--', marker = 's')
plt.text(0.5, 0.5, '', ha='center', va='center', size=24, alpha=.5)
axes_3 = plt.subplot(G[0, 2])
axes_3.plot(x, np.sin(x))
plt.text(0.5, 0.5, '', ha='center', va='center', size=24, alpha=.5)
axes_4 = plt.subplot(G[1, :])
axes_4.scatter(x, y)
plt.text(0.5, 0.5, '', ha='center', va='center', size=24, alpha=.5)
plt.show()

fig = plt.figure(figsize=(6, 4))
G = gridspec.GridSpec(4, 2)
axes_1 = plt.subplot(G[0, 0])
axes_1.plot(x, y)
plt.text(0.5, 0.5, '', ha='center', va='center', size=24, alpha=.5)
axes_2 = plt.subplot(G[0, 1])
axes_2.plot(x, y1, color = 'c')
plt.text(0.5, 0.5, '', ha='center', va='center', size=24, alpha=.5)
axes_3 = plt.subplot(G[1, 0])
days = list(range(1,9))
celsius_values = [25.6, 24.1, 26.7, 28.3, 27.5, 30.5, 32.8, 33.1]
axes_3.plot(days, celsius_values)
plt.text(0.5, 0.5, '', ha='center', va='center', size=24, alpha=.5)
axes_4 = plt.subplot(G[2, 0])
axes_4.plot([4,3,2,1])
plt.text(0.5, 0.5, '', ha='center', va='center', size=24, alpha=.5)
axes_5 = plt.axes([0.55, 0.30, 0.35, 0.38])
axes_5.plot(x, y1, color = 'g')
plt.text(0.5, 0.5, '', ha='center', va='center', size=24, alpha=.5)
axes_6 = plt.subplot(G[3, 0:])
axes_6.plot(x, y1, color = 'y')
plt.text(0.5, 0.5, '', ha='center', va='center', size=24, alpha=.5)
plt.show()

