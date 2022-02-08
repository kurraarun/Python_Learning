

# This Exercise to practice Recursion functions
import sys
print()
print(' This Exercise to practice Recursion Functions ')

print()
print('Welcome to Recursion function ')

def reverse(a):
    print(a)
    if a == 0 :
        return
    else:
        reverse(a-1)
print('Printing the Lines in Reverse order ')
reverse(9)
print()

print("Simple Recursion function to find the Factorial of given Number")
print()

def factorial(a):
    if a == 1:
        return 1
    return a * factorial(a-1)

print("Please Enter the number to find Factorial of :  " )
y = sys.stdin.readline()
try:
    z = int(y)
    print('Factorial of the given number is  ')
    x = factorial(z)
    print(x)
except:
    print('Entered Value is not an Integer to find Factorial ')

print('Fibonacci Series')
def fibonac(a):
    if a <= 1:
        return a
    else:
        return fibonac(a-1) + fibonac(a-2) 

print("Please Enter the number to Print Fibonacci of :  " )
x1 = sys.stdin.readline()   
print()
try:
    z1 = int(x1)
    for i in range(z1):
        print(fibonac(i))
except:
    print('Entered Value is not an Integer to Print Fibonacci ')
 