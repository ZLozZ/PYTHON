# cau  1 c buoi 8 
import matplotlib.pyplot as plt
import numpy as np

# cong thuc tinh toan 
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

# tim giao điem 
idx=np.argwhere(np.diff(np.sign(y - y2 )) != 0).reshape(-1) + 0

for i in range(len(idx)):
    plt.plot((x[idx[i]]+x[idx[i]+1])/2.,(y[idx[i]]+y[idx[i]+1]+y2[idx[i]]+y2[idx[i]+1])/4., 'bs')

# hien thi toa do x,y
plt.text(-2.66,-10.4, "x=-2.66,y=-10.4", color='magenta',horizontalalignment='right',verticalalignment='top') 
plt.text(-0.94,2.3, "x=-0.94,y=2.3", color='magenta',horizontalalignment='right',verticalalignment='baseline') 
plt.text(1.19,-1.5, "x=1.19,y=-1.5", color='magenta') 
plt.text(3.41,29.5, "x=3.41,y=29.5", color='magenta') 

# in ra man hinh 

plt.show()


