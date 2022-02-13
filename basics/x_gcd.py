# To find the GCD of Given numbers
print()
a = int(input("Please Enter the first number to find the GCD : "))

b = int(input("Please Enter the Second number to find the GCD : "))


def gcd_num(x,y):
    if ( y == 0 ):
        return(x)
    return (gcd_num(y,x%y))
GCD = gcd_num(a,b)
print("GCD of given Numbers is : ",GCD)