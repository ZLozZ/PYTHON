import csv

try:

    with open('N.csv', mode='r') as N_file:
        N_reader = csv.reader(N_file)
        for row in N_reader:
            print(row)
except FileNotFoundError:
    print('không tìm thấy file N.csv, bỏ file N.csv vào cùng thư mục của chương trình')