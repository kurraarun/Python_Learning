# Pythong Practicing

print()

x = int(input("How many digits you want to enter for Array : "))

a= []

for i in range(0,x):
    element= int(input("enter first element : " ))
    a.append(element)
print(a)
print("Sum is : ", sum(a))

print("Average is : ", sum(a)/x)
