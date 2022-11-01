# cau  1 b buoi 8 
import matplotlib.pyplot as plt
import numpy as np

# cong thuc tinh 
x = np.linspace(-4,4)
y = x**4 - (10)*(x**2) +10 

x2 = np.linspace(-4,4)
y2 = x**3 - 3*x 

# setting truc x va truc y 
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# hien thi chu thich
ax.plot(x, y, 'r', label='y')
leg = ax.legend();
ax.plot(x2, y2, 'g', label='y2')
leg2 = ax.legend();

# plot the function
plt.plot(x,y, 'r')
plt.plot(x2,y2, 'g')
# show the plot
plt.show()