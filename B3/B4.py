#4. Tạo ra dữ liệu sẵn có về 10 loại trái cây và giá tiền tương ứng dùng cấu trúc Tuples. Cho phép
# nhập liệu tên trái cây search ra giá tiền. Sau đó cập nhật lại giá tiền của 5 loại trái cây trong
# tuple đó. Search lại lần nữa các loại trái cây và xuất ra màn hình
traicay=("Trái Đào","Trái Cam","Trái Soài","Trái Mận","Trái Chanh","Trái Cóc","Trái Ổi","Trái Quýt","Trái Nho","Trái Táo")
giatien=("20.000/kg", "30.000/kg", "33.000/kg", "24.000/kg", "10.000/kg", "15.000/kg", "25.000/kg", "34.000/kg", "27.000/kg", "40.000/kg", )
while 1:
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
        break