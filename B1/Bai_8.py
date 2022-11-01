a = "L"
factorial = 1
b = a
if a < 0:
    print("Vui long nhap so duong")
else:
    while a >= 0:
        if a == 0:
            factorial *= 1
        else:
            factorial *= a
        a -= 1
    print("%d! = %d" %(b, factorial))


