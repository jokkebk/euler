import datetime, math

num = 0

for year in range(1901, 2001):
    for month in range(1, 13):
        day = datetime.date(year, month, 1)
        if day.weekday() == 6:
            print("%s was %d" % (str(day), day.weekday()))
            num += 1

print(num)
