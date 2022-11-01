#cau 3
def partition(mang, l, h):
  dem3 = 0
  pivot = mang[h]
  i = l - 1
  for j in range(l, h):
    if mang[j] >= pivot:
      i = i + 1
      (mang[i], mang[j]) = (mang[j], mang[i])
      dem3 = dem3 + 2
    dem3 = dem3 + 1
  (mang[i + 1], mang[h]) = (mang[h], mang[i + 1])
  dem3 = dem3 + 1
  return i + 1, dem3
  
def quicksort(mang, l, h, dem3):
  if l < h:
    pi, dem3 = partition(mang, l, h)

    quicksort(mang, l, pi - 1, dem3)
  
    quicksort(mang, pi + 1, h, dem3)
  return mang, dem3

dem3 = 0   
n = int(input("Nhap so phan tu cua mang : "))
mang = [float(input(">>")) for i in range(n)]
print(f'mang da nhap: {mang}')
mang, dem3 = quicksort(mang, 0, len(mang) - 1, dem3)
print(f'So lon nhat cua mang la',mang[0])
print('so phep tinh la:', dem3)