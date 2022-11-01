import numpy as np

class matran:
    def __init__(self, matrix):
        self.matrix = matrix
    
    def inverse_matrix(self):
        self.result1 = np.linalg.inv(self.matrix)
    
    def matrix_determinant(self):
        self.result1 = np.linalg.det(self.matrix)

def nhap(m, n):
    matrix = []
    for i in range(0, row):
        ptu = []
        for j in range(0, colum):
            l  = float(input("Nhập phần tử hàng {} cột {}: ".format(i, j)))
            ptu.append(l)
        matrix.append(ptu)
    return matrix

row = int(input("Nhập số hàng: "))
colum = int(input("Nhập số cột: "))
Mt = matran(np.array(nhap(row, colum)))
x = Mt.matrix_determinant()
print(Mt.result1)
if Mt.result1 != 0:
    Mt.inverse_matrix()
    print(Mt.result1)
else:
    print("Định thức là 0 nên không có tồn tại nghịch đảo")

    
