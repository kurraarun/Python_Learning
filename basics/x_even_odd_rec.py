

print()

x = int(input('Please Enter number to find Even or odd : '))

if x % 2 == 0:
    print('This number %d is EVEN number' % x)
else:
    print('This number %d is ODD num' %x)

print("Finding recursive way")

def find_even_odd(n):
    if n < 2:
        return (n % 2 == 0)
    return(find_even_odd(n-2))

y = int(x)
ab = find_even_odd(y)

if (find_even_odd(y) == True):
    print('Its Even Number')
else:
    print('its odd')   
