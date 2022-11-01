with open("file.txt", 'r', encoding='UTF-8') as f:
    info = f.readlines()
    for i in info:
        i = i.rstrip()
        i = i.rstrip(', ')
        print(i)