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

    for i in range(var2):
        print(fibonac(i))

except:
    print('Entered value is not Integer')


