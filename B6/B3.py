
import numpy as np

class matran:
    def __init__(self, matrix):
        self.matrix = np.array(matrix)

    def inverse_matrix(self):
        self.result1 = np.linalg.inv(self.matrix)
    
    def matrix_determinant(self):
        self.result2 = np.linalg.det(self.matrix)


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
Mt = matran(nhap(row, colum))
Mt.inverse_matrix()
Mt.matrix_determinant()
print(Mt.result2)
    
    
    
