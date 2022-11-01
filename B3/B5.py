#Tạo một set chứa thông tin 10 loại trái cây bất kỳ. Tạo một dictionary gồm tên 10 loại trái cây
#trên và giá từng loại. Viết chương trình tính số tiền phải trả khi người dùng mua trái cây với
#số lượng và loại bất kỳ.

set = {"Tao", "Vai", "Dua", "Nho", "Xoai", "Nhan", "Thom", "Oi", "Na", "Cam"}

thisdict = {
    "Tao" : 1000,
    "Vai" : 2000,
    "Nho" : 3000,
    "Dua" : 3500,
    "Xoai": 4000,
    "Nhan": 4500,
    "Thom": 5000,
    "Oi" : 5500,
    "Na" : 6000,
    "Cam" : 6500
}


Money = []
print("Nhập 'stop' để thanh toán ")
while True: 
  Fruit = input("Nhập loại quả muốn mua: ")
  S = int(input("Nhập số lượng: "))
  if Fruit == 'stop':
    break
  f = thisdict.get(Fruit) * S
  print("Số tiền: " + str(f))
  Money.append(f)

HoaDon = 0
for i in Money:
  HoaDon += i
print("Số tiền cần thanh toán: "+ str(HoaDon))