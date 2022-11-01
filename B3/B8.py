import random
def ratio(n):
    k = float(input("Nhập k trong khoảng từ 0->1: "))
    list2 = []
    sum = 0
    for i in range(0, n):
        pt = k**i
        list2.append(round(pt, 10))
        sum += list2[i]
    sum_p = 0
    if sum != 1:
        sum = 1/sum
    for i in range(0, n):
        list2[i] = list2[i]*sum
        sum_p += list2[i]

    return list2, sum_p
    
def random_element(list2, list1, a):
    b = 0
    for i in range(0, len(list2)):
        if a > b and a <= b+list2[i]:
            result =  list1[i]
        b += list2[i]
    return result
        

n = int(input("Nhập số phần tử cần tạo: "))
list1 = []
m = n
while n > 0:
    list1.append(round(random.uniform(0, 100), 2))
    n -= 1
print(list1)
list2, sum = ratio(m)
print("Tỉ lệ từng phần tử là: ",list2)
print("Tổng phần tử của list2: ",sum)
a = random.uniform(0, 1)
print("Tỉ lệ random: ",a)
result = random_element(list2, list1, a)
print("Phần tử lấy theo tỉ lệ là: ", result)