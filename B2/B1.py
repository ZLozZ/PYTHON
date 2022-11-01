#cau 1
def partition(mang, l, h):
  dem1 = 0
  pivot = mang[h]
  i = l - 1
  for j in range(l, h):
    if mang[j] <= pivot:
      i = i + 1
      (mang[i], mang[j]) = (mang[j], mang[i])
      dem1 = dem1 + 2
    dem1 = dem1 + 1
  (mang[i + 1], mang[h]) = (mang[h], mang[i + 1])
  dem1 = dem1 + 1
  return i + 1, dem1
  
def quicksort(mang, l, h, dem1):
  if l < h:
    pi, dem1 = partition(mang, l, h)

    quicksort(mang, l, pi - 1, dem1)
  
    quicksort(mang, pi + 1, h, dem1)
  return mang, dem1

dem1 = 0
n = int(input("Nhap so phan tu cua mang : "))
mang = [float(input(">>")) for i in range(n)]
print(f'mang da nhap: {mang}')
mang, dem1 = quicksort(mang, 0, len(mang) - 1, dem1)
print(f'Mang xep theo thu tu tang dan: {mang}')
print('so phep tinh la:', dem1)