

# Finding Factorial by recursive method

print()
a =int(input("Please enter the single Digit number to find the Factorial : " ))

def facto(n):
    if n <= 1:
        return 1
    else:
        return(n * facto(n-1))
print()
print('Factorial of {} is %d'.format(a) % facto(a))
print()
