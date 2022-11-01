def TRIANGLE():
    n = int(input("Nhập độ dài: "))
    if(n < 0):
        print("Vui long nhap so tu nhien!")
    else:
        for i in range(n):
            khoangtrang = " "*((n-i)*2-1)
            print(khoangtrang, end = '')
            for j in range(2*i + 1):
                print("*", end =' ')
            print()
                