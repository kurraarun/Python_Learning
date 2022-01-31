# This excercise to practice one liners in Python

print()
for i in range(10): print(i)
print()

a = [33,12,25,27,61,80]
for i in a:
    print(i)

x = [i+2 for i in a]
print(x)

y = [i*2 for i in x]
print(y)

print()
z = [i**2 for i in range(10)]
print(z)
print()

aa = [i**2 for i in range(10) if i%2 == 1]
print(aa)

print([(i,j) for i in range (3) for j in range(3)])
print()

i=4
print(i**2 if i<5 else 0)
