# This lesson for Loops

x = 20
y= 30

if x > y:
    print('X is greater than Y')
if x < y:
    print('x is Less than y')
else:
    print('both are equal')

while x < y:
    print(x)
    x = x+1


# To find the biggest number in given list

x = [23,4,26,76,34,21,87,99,3,74]
y = x[0]
print('Given List is : ',x)
for i in range(len(x)):
    if x[i] > y:
        y = x[i]
print('Bigger number is : ',y)
print()

# To find the smallest number in given list

y = x[0]
print('Given List is : ',x)
for i in range(len(x)):
    if x[i] < y:
        y = x[i]
print('Smallest number is : ',y)
print()



a= [23,4,26,76,34,21,87,99,3,74]
print(a)
print('Above one is original list')
print()
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] > a[j]:
           temp = a[i]
           a[i] = a[j]
           a[j] = temp
    print(a)
print("Ascending order of list")
print(a)  