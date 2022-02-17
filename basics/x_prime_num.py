

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