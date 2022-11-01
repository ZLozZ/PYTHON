try:
    with open (cau1.txt,"r",encoding="utf-8") as file:
        ds = file.readline().rstrip(';')

    ds = ds.split(';')
    Menu = ["Hovaten","Diachi", "email", "SDT"]
    ketqua1 = []

    for i in ds:
        ketqua1.append(i.rstrip(','))

    ketqua2 = []
    for i in ketqua1:
        ketqua2.append(i.split(','))
    final = []
    for i in ketqua2:
        final.append(dict(zip(Menu, i)))

    for i in final:
        for key, value in i.items():
            print("{}:{}".format(key, value), end = " ")
        print()
except NameError:
    print("Lỗi tên file!")