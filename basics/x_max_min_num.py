# This program to identify the Max number of the list.

a = [23,5,2,43,21,52,6,78,91,53,65]
a_len = len(a)
b = 0

print('Here is the Given List ')
for i in a:
    b += 1
    if a_len == b:
        print(i, end='\n')
    else:
        print(i, end = ' ,') 

# Identifying the maximum number in the given list
b = max(a)

print("Maximum number of the above list %d" %b)

c = min(a)
print("Minimum number of the above list %d" %c)

a.sort()
print ("Sorting the given numbers in Acsending order " )

i = 0
for y in a:
    i += 1
    if i == a_len:
        print(y, end='\n')
    else:
        print(y, end=' ,')
# Sorting the numbers in Descending order

print ("Sorting the given numbers in Descending order " )
a.sort(reverse = True)
i = 0
for y in a:
    i += 1
    if(i == a_len):
        print(y, end=' \n')
    else:
        print(y, end=' ,')

