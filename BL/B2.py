print('Nhap ten:')
fl = open("tenSinhVien.txt", "w")
running = True
while(running):
    name = str(input())
    if name == 'NO' or name == 'N':
        running = False
    else:
        fl.write(name + '\n')
fl.close()
