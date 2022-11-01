import random

n = int(input("Nhập số phần tử cần tạo: "))
Min, Max = map(int, input("Nhập khoảng cần tạo: ").split())
ds = []
while n > 0:
    Element = random.uniform(Min, Max)
    if Element not in ds:
        ds.append(round(Element, 2))
        n-=1
print(ds[random.randint(0, len(ds))])