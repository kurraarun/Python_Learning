

# This example to practice recursive function 


n = int(input(" Please Enter the number of digits for list :  "))
a = []

def sum_arr(arrb, y):
#    print(arrb)  
    if y == 0:
        return 0
    else:
        return arrb[y-1]+sum_arr(arrb,y-1) 
  
for i in range(0,n):
    elemt = int(input("Enter Element {}  : ".format(i)))  
    a.append(elemt)

print(a)
total=sum_arr(a,n)
print("Sum of array elements is : ",total)