import csv

def partition1(mang, l, h):
  pivot = mang[h]
  i = l - 1
  for j in range(l, h):
    if mang[j] <= pivot:
      i = i + 1
      (mang[i], mang[j]) = (mang[j], mang[i])
  (mang[i + 1], mang[h]) = (mang[h], mang[i + 1])
  return i + 1

def partition2(mang, l, h):
  pivot = mang[h]
  i = l - 1
  for j in range(l, h):
    if mang[j] >= pivot:
      i = i + 1
      (mang[i], mang[j]) = (mang[j], mang[i])
  (mang[i + 1], mang[h]) = (mang[h], mang[i + 1])
  return i + 1
  
def quicksort_increase(mang, l, h):
  if l < h:
    pi = partition1(mang, l, h)

    quicksort_increase(mang, l, pi - 1)
  
    quicksort_increase(mang, pi + 1, h)
  return mang

def quicksort_reduce(mang, l, h):
  if l < h:
    pi = partition2(mang, l, h)

    quicksort_reduce(mang, l, pi - 1)
  
    quicksort_reduce(mang, pi + 1, h)
  return mang

number = []
with open("file.csv", 'r') as f:
    creader = csv.reader(f)
    for row in creader:
        for i in row:
            number.append(float(i))

number1 = quicksort_increase(number, 0, len(number)-1)
with open("tang.csv", 'w') as t:
    writer = csv.writer(t)
    writer.writerow(number1)

number2 = quicksort_reduce(number, 0, len(number)-1)
with open("giam.csv", 'w') as g:
    writer = csv.writer(g)
    writer.writerow(number2)

