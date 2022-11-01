import numpy as np

def nhap(m, n):
    matrix = []
    for i in range(0, row):
        ptu = []
        for j in range(0, colum):
            l  = int(input("Nhập phần tử hàng {} cột {}: ".format(i, j)))
            ptu.append(l)
        matrix.append(ptu)
    return matrix

row = int(input("Nhập số hàng: "))
colum = int(input("Nhập số cột: "))
matrix1 = np.array(nhap(row, colum))
matrix2 = np.array(nhap(row, colum))
content1 = str(matrix1)
content2 = str(matrix2)
with open('matrix1.txt', 'w') as f1:
    f1.write(content1)

with open('matrix2.txt', 'w') as f2:
    f2.write(content2)
