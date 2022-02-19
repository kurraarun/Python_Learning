

# 

n=int(input("Please Enter value to find the list of Prime numbers in that range :  "))

ab = range(2,n+1)

print(ab)

#abc = set( range(2,n+1))

#print(abc)

num_list= set(range(2,n+1))
print(num_list)

print()
print("Here is the List of Prime numbers till ",n)
while num_list:
    min_num = min(num_list)
    print(min_num, end ="\t")
    num_list = num_list - set(range(min_num,n+1,min_num))
#    print(num_list)
print()


print('Prime numbers in another way ')

i=1
while i<=n:
    k=0
    j=1
    while j <=i:
        if i%j==0:
            k = k+1    
        j = j+1
    if k <=2 and i != 1:
        print(i ,end = "\t")
    i = i +1






