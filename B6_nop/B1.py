import numpy as np
a = np.array ([[1,2,3],[1,2,3],[3,2,1]])
b = np.array ([[5,6,7],[5,2,7],[7,6,8]])
c= a+b
d= a-b
e= np.matmul (a,b)
q = np.matmul (a,np.linalg.inv(b))
print (c)
print (d)
print (e)
print (q)
