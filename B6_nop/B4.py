from email import header
import numpy as np
import pandas as pd
import random

class Oj:
    def __init__(self, matrix):
        self.X = np.array(matrix)

    def save_file(self, head):
        np.savetxt('np.csv', self.X, fmt='%.2f', delimiter=',', header=head)

    def load_file(self):
        self.X = np.array(pd.read_csv('np.csv'))

    def update(self, alpha, K):
        self.X = self.X - alpha*K

def create_matrix(m, n, min, max):
    matrix = []
    for i in range(0, m):
        ptu = []
        for j in range(0, n):
            ptu.append(random.uniform(min, max))
        matrix.append(ptu)
    return matrix

row = int(input("Nhập số hàng: "))
colum = int(input("Nhập số cột: "))
header = ''
for i in range(0, colum):
    if i == (colum-1):
        header+=(str(i))
    else:
        header+=(str(i)+', ')
        
min = int(input("Nhập số min: "))
max = int(input("Nhập số max: "))
matrix = create_matrix(row, colum, min, max)
K = np.array(create_matrix(row, colum, min, max))
alpha = float(input("Nhập alpha: "))
Mt = Oj(matrix)
print(K)
Mt.save_file(header)
Mt.load_file()
print("Trước update: ")
print(Mt.X)
Mt.update(alpha, K)
print("Sau update: ")
print(Mt.X)