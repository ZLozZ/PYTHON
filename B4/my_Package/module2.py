def partition1(mang, l, h):
  pivot = mang[h]
  i = l - 1
  for j in range(l, h):
    if mang[j] <= pivot:
      i = i + 1
      (mang[i], mang[j]) = (mang[j], mang[i])

  (mang[i + 1], mang[h]) = (mang[h], mang[i + 1])
  return i + 1
  
def increase(mang, l, h):
  if l < h:
    pi = partition1(mang, l, h)
    increase(mang, l, pi - 1)
    increase(mang, pi + 1, h)
  return mang
