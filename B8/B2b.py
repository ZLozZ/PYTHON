import matplotlib.pyplot as plt
import numpy as np
from numpy import arange
from numpy import exp
from numpy import sqrt
from numpy import cos
from numpy import sin
from numpy import e
from numpy import pi
from numpy import meshgrid

feature_x = np.linspace(-10, 10, 100)
feature_y = np.linspace(-10, 10, 100)
[x, y] = np.meshgrid(feature_x, feature_y)
fig, ax = plt.subplots()

Z = -abs(sin(x)*cos(y)*exp(abs(1-((sqrt(x*x + y*y))/pi))))
ax.contourf(x, y, Z,levels=np.linspace(-20, 0.9, 45))
ax.set_title('Hölder table function')
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()