
dicts = {}
mount = 0
ds = []
while True:
    for i in range(0, 1):
        info = []
        name = input("Họ và tên: ")
        info.append(name)
        address = input("Địa chỉ: ")
        info.append(address)
        mail = input("Địa chỉ mail: ")
        info.append(mail)
        number_phone = input("Số điện thoại: ")
        info.append(number_phone)
    for i in range(0,mount):
        for j in info:
            ds[i].append(j)
    print("Bạn muốn nhập nữa không\n 1. Có\n 2. Không")
    i = int(input("Nhập yêu cầu: "))
    if i == 2:
            break
    mount+=1

with open('file.txt', 'w', encoding='UTF-8') as f:
    for i in range(0, mount+1):
        for j in ds[i]:
            f.write(j)
        f.write('\n')
    
        
            
