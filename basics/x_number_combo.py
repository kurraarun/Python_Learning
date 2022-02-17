# This practice to display different combinations

a=int(input('Please enter the first single digit number : '))

b=int(input('Please enter the Second single digit  number : '))
c=int(input('Please enter the Third  single digit number : '))

x=[]
x.append(a)
x.append(b)
x.append(c)
print(x)
#print(len(x))
for i in range(0,len(x)):
    for j in range(0,len(x)):
        for k in range(0,len(x)):
            if (i!=j and j!=k and i!=k):
                print(x[i],x[j],x[k])
#            else:
#                print(i,j,k)

for i in range(0,len(x)):
    for j in range(0,len(x)):
        for k in range(0,len(x)):
            if (i!=j and j!=k and i!=k):
                print(x[i],x[j],x[k])

##################################################

print()
print("This is different combo ")
print()

xz = int(input("Enter the number :"))

for i in range(1, xz +1):
    a=[]
    for j in range(1,i+1):
        print(j,sep= " ", end = " ")
        if j < i:
            print("+",sep=" ", end= " ")
        a.append(j) 
    print("=",sep=" ",end = " ")
    
    print(sum(a)) 
print()




for i in range(0, xz-1):
    for j in range(0,xz-1):
        if i == j:
            print(1,sep= " ",end = " ")
        else:
            print(0,sep= " ",end = " ")
    print() 