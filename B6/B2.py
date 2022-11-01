import numpy as np

with open('matrix1.txt', 'r') as f:
    content = f.read()

content = np.array(content)
print(content)