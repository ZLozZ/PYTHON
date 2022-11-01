def LeapYear(year):
    if year%400 == 0:
        return True
    if year % 100 != 0 and year % 4 == 0:
        return True
    return 0

today = [1, 12, 2020]
next_day = [12, 12, 2020]
date = [31,28,31,30,31,30,31,31,30,31,30,31]
dateOfYear = 0
dateOfMonth = 0

for year in range(today[2], next_day[2]):
    if LeapYear(year):
        dateOfYear += 366
    else:
        dateOfYear += 365

if LeapYear(next_day[2]):
    date[1] = 29
if today[1] > next_day[1]:
    for i in range (next_day[1],today[1]):
        dateOfMonth -= date[i-1]
else:
    for i in range(today[1], next_day[1]):
        dateOfMonth += date[i-1]
date = next_day[0] - today[0] + 1
sumDate = date + dateOfMonth + dateOfYear
print(sumDate)



    