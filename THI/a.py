from Trai_cay import Nhap_ten, value, sale, mount
from Loichao import loichao, Nhapten, tambiet

def nhap():
    name_t = []
    value_t= []
    sale_off_t = []
    mount_t = []
    while 1:
        name_pt = Nhap_ten.nhap_ten()
        value_pt = value.nhap()
        sale_of = sale.nhap()
        mount_pt = mount.nhap();
        name_t.append(name_pt)
        value_t.append(value_pt)
        sale_off_t.append(sale_of)
        mount_t.append(mount_pt)
        print("Bạn có muốn nhập nữa không:\n Nhấn 1 để nhập tiếp \n Nhấn 0 để thoát")
    return name_t, value_t, sale_off_t, mount_t

name_u = Nhapten.name_user()
loichao.hello(name_u)
n = int(input("Nếu bạn muốn nhập đầu vào thì nhấn 1, để tìm kiếm nhấn 2: "))
if n == 1:
    while 1:
        name_t, value_t, sale_off_t, mount_t = nhap()
        i = int(input("Bạn có muốn nhập tiếp không nếu không thì nhấn không còn lại thì nhấn 1: "))
        if i == 0:
            break
if n == 2:
    while 1:
        k = 

tambiet.bye(name_u)