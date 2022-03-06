import sys

# Practicing Recursive Fibonacci series 
print("Practicing Fibonacci series")

print("Please enter single Digit number to get Fibonacci series ")
var1=sys.stdin.readline()



print()

def fibonac(var2):
    if var2 <= 1:
        return var2
    else:
        return fibonac(var2-1) + fibonac(var2-2)


try:
    
    print('Entered value is ', var1)
    var2 = int(var1)
    if var2 < 1:
        print('Please enter positive integer')
    elif var2 == 1:
        x=0
        print(x)
        
    elif var2 == 2:
        x=0 
        y=1
        print(x)
        print(y)
    elif var2 > 2:
        x=fibonac(0)
        y=fibonac(1)
        z=0
        print(x)
        print(y)
        for i in range(2,var2):
            z=x+y
            x=y
            y =z
            print(z)
    else:
        print('None')    
except:
    print('Entered value is not Integer')


