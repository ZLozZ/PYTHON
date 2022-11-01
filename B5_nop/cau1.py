a =[]
b=[]
c=[]
d=[]
k=[]
n = int(input("Nhập số lượng danh sách:"))
with open('cau1.txt','w') as f:
    for i in range (n):
    
        name = input("Nhập họ và tên:")
        a.append(name)
        f.write(a[i])
        f.write(",")
        #
        address = input("Nhập địa chỉ:")
        b.append( address)
        f.write(b[i])
        f.write(",")
        #
        email = input("Nhập email:")
        c.append(email)
        f.write(c[i])
        f.write(",")
        #
        email = input("Nhập số điện thoại:")
        d.append(email)
        f.write(d[i])
        f.write(",")
        f.write(";")