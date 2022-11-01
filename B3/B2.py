#2. Sử dụng kiểu Tuple viết chương trình có dữ liệu điểm trung bình môn học của học sinh Nguyễn
#Văn A như sau: “Nguyễn Văn A, Toán 7.4 Lý 6.5 Hoá 7.0”. Hiển thị màn hình hướng dẫn
#nhập liệu search thông qua nhập tên học sinh. Ví dụ nhập Nguyễn Văn A thì nghĩa là hiển thị
#xuất ra tên và điểm trung bình môn học.
ten=("Kim Văn A","Kim Văn B","Kim Văn C")
diemtoan=(9,8.75,5)
diemly=(6.5,10,9)
diemhoa=(8,7,10)
while 1:
    s= int(input("Điểm từng môn nhấn số 1, Điểm trung bình nhấn số 2, Kết thúc nhấn số 3: "))
    if s == 1:
        x = input("Nhập tên học sinh: ")
        for i in range(3):
            if x == ten[i]:
                print("Tên học sinh: %s, Điểm Toán: %.2f, Điểm Lý: %.2f, Điểm Hóa: %.2f"%(ten[i],diemtoan[i],diemly[i],diemhoa[i]))
    if s == 2:
        for i in range(3):
            s=(diemtoan[i]+diemly[i]+diemhoa[i])/3
            x = input("Nhập tên học sinh: ")
            if x == ten[i]:
                print("Tên học sinh: %s, Điểm Trung bình: %.2f"%(ten[i],s))
    if s == 3:
        break
