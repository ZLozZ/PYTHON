from my_Package import module1, module2, module3


print("============FUNTION============")
print("1. Để tính phương trình bậc 2")
print("2. Để sắp xếp tăng dần")
print("3. Để sắp xếp giảm dần")
print("4. Để thoát chương trình")
while True:
    i = int(input("Bạn muốn chọn chức năng: "))

    if i == 1:
        a, b, c = map(float, input("Nhập hệ số: ").split())
        module1.giai_pt2(a, b, c)
    if i == 2:
        n = int(input("Nhập số phần tử của mảng : "))
        mang = [float(input(">>")) for i in range(n)]
        print(f'Mảng đã nhập: {mang}')
        mang = module2.increase(mang, 0, len(mang) - 1)
        print(f'Mảng sắp xếp theo thứ tự tăng dần: {mang}')
    if i == 3:
        n = int(input("Nhập số phần tử của mảng : "))
        mang = [float(input(">>")) for i in range(n)]
        print(f'Mảng đã nhập: {mang}')
        mang = module3.reduce(mang, 0, len(mang) - 1)
        print(f'Mảng sắp xếp theo thứ tự giảm dần: {mang}')
    if i == 4:
        break
