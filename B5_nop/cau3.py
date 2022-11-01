import csv

with open('N.csv', mode='r') as N_file:
    N_reader = csv.reader(N_file)
    for row in N_reader:
        print(row)

