x = int(input("Enter the number :"))
a=[]
for i in range(0, x):
    for j in range(0,x):
        if i == j:
            print(1,sep= " ",end = " ")
        else:
            print(0,sep= " ",end = " ")
    print() 

for i in range (x,0,-1):
    print( i * '*')

for i in range (x,0,-1):
    print( (x-i) * ' ' +i * '*')


