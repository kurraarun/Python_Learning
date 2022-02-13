

# This excercise to practice LCM of given numbers
print()
a = int(input("Please enter the First number to find the LCM  : "))

b = int(input("Please enter the Second number to find the LCM  : "))

def lcm(x,y):
    lcm.mul = lcm.mul + y
    if ( lcm.mul % x == 0) and ( lcm.mul % y == 0 ):
        return lcm.mul
    else:
        lcm(x,y)
    return lcm.mul
lcm.mul = 0

if (a > b):
    val=lcm(b,a)
else:
    val= lcm(a,b)
print()
print("LCM Of NUmber {} and {} is {} ".format(a,b,val))

