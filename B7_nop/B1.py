import matplotlib
import pandas as pd
import numpy as np

nd_array_1 = np.array([1, 2, 6, 3, 4, 5])
s1 = pd.Series(nd_array_1)
s1.plot.hist()
matplotlib.pyplot.show()