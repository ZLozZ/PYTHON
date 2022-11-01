import csv

number = input("Nhập chuỗi số: ").split()
number = [float(i) for i in number]
print(number)

with open("file.csv", 'w') as f:
    writer = csv.writer(f)
    writer.writerow(number)
    
with open("file.csv", 'r') as f:
    creader = csv.reader(f)
    print("Chuỗi vừa nhập vào file: ", end = "")
    for row in creader:
        for i in row:
            print(i, end = ' ')

