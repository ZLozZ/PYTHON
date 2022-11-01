
#giai thuat euclid
def ucln(a, b):
    if (b == 0):
        return a;
    return ucln(b, a % b)
 
def bcnn(a, b):
    return int((a * b) / ucln(a, b))
 
number1, number2 = map(int,input("Nhập 2 số cần tìm UCLN, BCNN: ").split())
UCLN = ucln(number1, number2)
BCNN = bcnn(number1, number2)
print("Ước số chung lớn nhất của {} và {} là: {}".format(number1, number2, UCLN))
print("Bội số chung nhỏ nhất của {} và {} là: {}".format(number1, number2, BCNN))