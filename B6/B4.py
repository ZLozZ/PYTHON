import numpy as np
import random
import csv

class Oj:
    def __init__(self, matrix):
        self.matrix = np.array(matrix)

    def read_file(self, matrix):
        with open("matrix.csv", 'w') as f1:
            writer = csv.writer(f1)
            writer.writerow(matrix)

    def load_file(self):
        with open("matrix.csv", 'r') as f2:
            reader = np.array(f2.read())
        return reader

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
min = int(input("Nhập số min: "))
max = int(input("Nhập số max: "))
matrix = create_matrix(row, colum, min, max)
Mt = Oj(matrix)
Mt.read_file(Mt.matrix)
print(Mt.load_file())
print(type(Mt.load_file()))
