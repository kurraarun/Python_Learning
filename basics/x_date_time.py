

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta    # this use for timebase mathematics

print(date.today())


x = date.today()

print('Todays date is : ', x)

#print(dir(date))

print(x.day)

print(x.month)

print(x.year)

print("Today's Week Day is  :  ", x.weekday())

print(datetime.now())

y = datetime.time(datetime.now())

print(y)

z = datetime.now()

print(z.strftime("The current Year is : %Y"))

print(z.strftime(" Today day is  :  %a  Dt :  , %d  Month is  %B , year is %y"))
print()

print(z.strftime("Local Date and time :  %c"))

print(z.strftime("Local Date  :  %x"))

print(z.strftime("Local time :  %X"))

print()

print(z.strftime("Current time : %I:%M:%S  %p"))

print(z.strftime("24 Hour time : %H:%M"))

print(timedelta(days=365, hours=5, minutes=1))

now = datetime.now()

print("today is: " + str(now))

print("One year from now it will be : " + str(now + timedelta(days = 365)))

print("One month from now it will be : " + str(now + timedelta(days = 30)))

print("IN 2 days and 3 weeks , it will be "+ str(now + timedelta(days = 2, weeks =3)))

t = datetime.now() - timedelta(weeks=1)

s = t.strftime("%A %B %d , %Y")

print("One Week ago it was : ",s)


today = date.today()
afd = date(today.year,4,1)

if afd < today:
   print("April Fool's day already went by %d days ago"%((today-afd).days))
   
   afd = afd.replace(year = today.year+1)

time_to_afd = afd - today

print("Its just ", time_to_afd.days, "days untile April Fools day")


