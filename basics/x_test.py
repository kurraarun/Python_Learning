x = int(input("Enter the number :"))
a=[]
for i in range(0, x-1):
    for j in range(0,x-1):
        if i == j:
            print(1,sep= " ",end = " ")
        else:
            print(0,sep= " ",end = " ")
    print() 
