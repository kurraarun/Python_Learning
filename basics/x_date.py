

# This Excerice to practice date

dt = input('Please Enter the date in format DD/mm/yyyy  : ')

dd,mm,yy = dt.split('/')
dd = int(dd)
mm = int(mm)
yy = int(yy)

print('dd : ',dd)

print('mm : ',mm)

print('yy : ',yy)

if (mm > 12 or mm == 0 or dd == 0 or dd >31):
    print("Date is Invalid")
elif (mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12):
    mx_dd = 31
elif (mm == 4 or mm == 6 or mm == 9 or mm == 11):
    mx_dd = 30
elif(( yy%4 == 0 and yy%100 !=0 ) or (yy%400 ==0)) :
    mx_dd = 29 
else:
    mx_dd = 28
if dd == mx_dd and mm == 12:
    dd = 1
    mm = 1
    yy = yy + 1
    print('In cremental date is ',dd,mm,yy)
elif dd == mx_dd and mm <12:
    dd = 1
    mm +=1
    print('In cremental date is ',dd,mm,yy)
elif dd < mx_dd and mm < 12 and mm !=2:
    dd += 1
    mm +=1
    print('In cremental date is ',dd,mm,yy)
else:
    print('not valid')
