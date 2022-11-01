
def check_Quicksort(arr, min, max):
    x = arr[max]
    i = min
    global dem
    for j in range(min, max):
        if arr[j] < x:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
            dem += 3
    arr[i], arr[max] = arr[max], arr[i]
    return i

def n_Min(arr, min, max, n):
	if (n > 0 and n <= max - min + 1):
		index = check_Quicksort(arr, min, max)
		if (index - min == n - 1):
			return arr[index]
		if (index - min > n - 1):
			return n_Min(arr, min, index - 1, n)
		return n_Min(arr, index + 1, max, n - index + min - 1)

def duplicate(arr):
    ds = []
    for i in arr:
        if i not in ds:
            ds.append(i)
    return ds

global dem
dem = 0
arr = input("Nhap chuoi so: ").split()
arr = [float(i) for i in arr]
arr = duplicate(arr)
l = len(arr)
n = int(input("Nhap phan tu: "))
nMin = n_Min(arr, 0, l-1, n)
print("Phần tử bé thứ {} là: {}".format(n, nMin))
print("Số phép tính sử dụng của chương trình là: {}".format(dem))