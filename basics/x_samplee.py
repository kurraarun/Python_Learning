from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta  
import calendar


now=datetime.now()
print(now.strftime("%d-%b-%Y %H:%M:%S"))


print(now.strftime("%c"))


print(now.strftime("%d"))


print(now.strftime("%M"))


print(now.strftime("%Y"))


today=date.today()
# Option A:
tomorrow=today+timedelta(days=1)

print(tomorrow)
# Option B:
tomorrow11  =date(today.year,today.month,today.day+1)
print(tomorrow11)