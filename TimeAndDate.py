import datetime as dt
year, month, day = input().split()
days = int(input())
newdate = dt.date(int(year),int(month),int(day))
newdate1 = dt.timedelta(days)
newdate1 += newdate
print(newdate1.year, newdate1.month, newdate1.day)
#print(newdate1.strftime('%Y %m %d'))