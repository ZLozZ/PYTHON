import numpy as np
import csv
a = np.array ([[1,2,3],[1,2,3],[3,2,1]])
b = np.array ([[5,6,7],[5,2,7],[7,6,8]])
np.savetxt('m1.csv', a, fmt='%.2f', delimiter=',', header='1,  2,  3')
np.savetxt('m2.csv', b, fmt='%.2f', delimiter=',', header='1,  2,  3')
c = a + b
d = a - b
e= np.matmul (a,b)
q = np.matmul (a,np.linalg.inv(b))
print(c)
print(d)
print(e)
print(q)
f = open('kq.csv','w')
g = csv.writer(f)
g.writerows(c)
g.writerows(d)
g.writerows(e)
g.writerows(q)
