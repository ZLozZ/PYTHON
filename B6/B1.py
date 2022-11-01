
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
print(matrix1)
print(matrix2)
while(1):
    print("Bạn muốn làm gì? \n1.Để chọn phép công \n2.Để chọn phép trừ \n3.Để chọn phép nhân \n4. Để chọn phép chia\n5.Thoát")
    n = int(input("Mời bạn nhập: "))
    if n == 1:
        print("Cộng 2 ma trận: ")
        print(np.add(matrix1, matrix2))
    if n == 2:
        print("Trừ 2 ma trận: ")
        print(np.subtract(matrix1, matrix2))
    if n == 3:
        print("Tích 2 ma trận: ")
        print(np.dot(matrix1, matrix2))
    if n == 4:
        print("Chia 2 ma trận: ")
        print(np.matmul (b,np.linalg.inv(a1)))
    if n == 5:
        break
