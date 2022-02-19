n=int(input("Enter any number: "))
a=list(map(int,str(n) ) ) 
print(a)

b=list(map(lambda x:x**3,a))

print(b)

c= list(map(lambda x,y : x + y , a, b))

print(c)


   