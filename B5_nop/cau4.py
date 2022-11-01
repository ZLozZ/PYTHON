import csv

so = []
with open("N.csv", 'r') as N_file:
    N_reader = csv.reader(N_file)
    for row in N_reader:
        for i in row:
            so.append(float(i))

def tangdan(mang, l, h):
  pivot = mang[h]
  i = l - 1
  for j in range(l, h):
    if mang[j] <= pivot:
      i = i + 1
      (mang[i], mang[j]) = (mang[j], mang[i])
  (mang[i + 1], mang[h]) = (mang[h], mang[i + 1])
  return i + 1
  
def quicksort1(mang, l, h):
  if l < h:
    pi = tangdan(mang, l, h)

    quicksort1(mang, l, pi - 1)
  
    quicksort1(mang, pi + 1, h)
  return mang

so1 = quicksort1(so, 0, len(so)-1)
with open("tang.csv", 'w') as tang:
    writer = csv.writer(tang)
    writer.writerow(so1)

def giamdan(mang, l, h):
  pivot = mang[h]
  i = l - 1
  for j in range(l, h):
    if mang[j] >= pivot:
      i = i + 1
      (mang[i], mang[j]) = (mang[j], mang[i])
  (mang[i + 1], mang[h]) = (mang[h], mang[i + 1])
  return i + 1
  
def quicksort2(mang, l, h):
  if l < h:
    pi = giamdan(mang, l, h)

    quicksort2(mang, l, pi - 1)
  
    quicksort2(mang, pi + 1, h)
  return mang

so2 = quicksort2(so, 0, len(so)-1)
with open("giam.csv", 'w') as giam:
    writer = csv.writer(giam)
    writer.writerow(so2)