# cau 1 a buoi 8 
import matplotlib.pyplot as plt
import numpy as np

# cong thuc tinh 
x = np.linspace(-4,4,50)
y = (x**4) - 10*(x**2)+10 

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

# plot the function
plt.plot(x,y, 'r')

# show the plot
plt.show()