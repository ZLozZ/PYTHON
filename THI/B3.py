def nhap():
    name = []
    value = []
    sale_off = []
    mount = []
    while 1:
        name_pt = input("Nhập tên trái cây: ")
        value_pt = float(input("Nhập giá trái cây: "))
        sale_of = float(input("Nhập phần trăm sale: "))
        mount_pt = int(input("Nhập số lượng trong kho: "))
        name.append(name_pt)
        value.append(value_pt)
        sale_off.append(sale_of)
        mount.append(mount_pt)
        print("Bạn có muốn nhập nữa không:\n Nhấn 1 để nhập tiếp \n Nhấn 0 để thoát")
    return name, value, sale_off, mount


name, value, sale_off, mount = nhap()
"""while 1:
    s=int(input("Chọn chức năng: "))
    if s == 1:
        x = input("Nhập loại trái cây: ")
        for i in range (10):
            if x == traicay[i]:
                print("Tên trái cây: %s, Gía tiền: %s"%(traicay[i],giatien[i]))
                n = ("Trái Đào","Trái Cam","Trái Soài","Trái Mận","Trái Chanh","Trái Cóc","Trái Ổi","Trái Quýt","Trái Nho","Trái Táo")
                m = ("20.000/kg", "30.000/kg", "33.000/kg", "24.000/kg", "10.000/kg", "15.000/kg", "25.000/kg", "34.000/kg", "27.000/kg", "40.000/kg", )
                y = list(n)
                g = list(m)
    if s == 2:
        x= input("Nhập loại trái cây cần đổi giá: ")
        e= input("Giá cập nhật: ")
        for i in range(10):
            if x == n[i]:
                g[i] = e
    if s == 3:
        x = input("Nhập loại trái cây: ")
        for i in range (10):
            if x == traicay[i]:
                print("Tên trái cây: %s, Gía tiền: %s"%(traicay[i],g[i]))
    if s == 4:
        break"""