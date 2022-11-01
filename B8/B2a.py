import matplotlib.pyplot as plt
import numpy as np
from numpy import exp
from numpy import sqrt
from numpy import cos
from numpy import e
from numpy import pi

feature_x = np.linspace(-5.0, 5, 100)
feature_y = np.linspace(-5.0, 5, 100)
[x, y] = np.meshgrid(feature_x, feature_y)
fig, ax = plt.subplots(1, 1)

Z = -20.0 * exp(-0.2 * sqrt(0.5 * (x**2 + y**2)))-exp(0.5 * (cos(2 * pi * x)+cos(2 * pi * y))) + e + 20
ax.contourf(x, y, Z)
ax.set_title('Ackley function')
ax.set_xlabel('x')
ax.set_ylabel('y')
  
plt.show()

