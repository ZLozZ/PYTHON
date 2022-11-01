import csv
import random
N = int(input("N="))
MIN = int(input("MIN="))
MAX = int(input("MAX="))
thislist = []
for i in range (N):
  thislist.append(random.uniform(MIN,MAX))
print(thislist)
with open('N.csv',mode='w') as N_file:
    N_write = csv.writer(N_file, quoting=csv.QUOTE_ALL)
    N_write.writerow(thislist)