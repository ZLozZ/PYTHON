#Nhập từ bàn phím và lưu dữ liệu vào từng list với các trường như sau: Mã số Sinh Viên, Họ
#và Tên, Ngày Tháng Năm Sinh, Tên Lớp, Điểm Thường Kỳ 1,2,3, Điểm Thi Giữa Kỳ, Điểm
#Thi Cuối Kỳ, Tính điểm trung bình tổng kết, kết quả đậu rớt.

while(True):
  n = int(input("Nhập số SV: "))
  if(n>0): break
listSV=[]
for i in range(0, n, 1):
  print("Nhập thông tin sv thứ "+ str(i+1))
  mssv = input("Nhập mã sv: ")
  name = input("Nhập họ và tên: ")
  Date = input("Nhập ngày/tháng/năm sinh: ")
  Class = input("Nhập tên lớp: ")
  TK1 = float(input("Nhập điểm tk1: "))
  TK2 = float(input("Nhập điểm tk2: "))
  TK3 = float(input("Nhập điểm tk3: "))
  GK = float(input("Nhập điểm gk: "))
  CK = float(input("Nhập điểm ck: "))
  TB = (TK1 + TK2 + TK3) / 3 * 0.2 + GK * 0.3 + CK * 0.5
  if CK < 3 or TB < 4 or GK == 0:
    KQ = 'thi lại'
  else:
    KQ = 'Thi đỗ'
  a = {"mã số sv":mssv, "Họ và tên": name, "Ngày tháng năm": Date, "Tên lớp": Class, 
  "Thường kì 1": TK1, "Thường kì 2": TK2, "Thường kì 3":TK3, "giữa kì":GK, "Cuối kì":CK, "Trung bình":TB, "Kết quả":KQ }
  listSV.append(a)
print(listSV)
