#cau 2
def partition(mang, l, h):
  dem2 = 0
  pivot = mang[h]
  i = l - 1
  for j in range(l, h):
    if mang[j] >= pivot:
      i = i + 1
      (mang[i], mang[j]) = (mang[j], mang[i])
      dem2 = dem2 + 2
    dem2 = dem2 + 1
  (mang[i + 1], mang[h]) = (mang[h], mang[i + 1])
  dem2 = dem2 + 1
  return i + 1, dem2
  
def quicksort(mang, l, h, dem2):
  if l < h:
    pi, dem2 = partition(mang, l, h)

    quicksort(mang, l, pi - 1, dem2)
  
    quicksort(mang, pi + 1, h, dem2)
  return mang, dem2
  
dem2 = 0    
n = int(input("Nhap so phan tu cua mang : "))
mang = [float(input(">>")) for i in range(n)]
print(f'mang da nhap: {mang}')
mang, dem2 = quicksort(mang, 0, len(mang) - 1, dem2)
print(f'Mang xep theo thu tu giam dan: {mang}')
print('so phep tinh la:', dem2)
