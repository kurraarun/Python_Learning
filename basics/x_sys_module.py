# This excerise to learn about Sys module

import sys
print()
print('Here the command sys.version is to print the version of the system ')
print()
a = '########Helllo World##########'
print(a)
print(a.rstrip('#'))   
print(a.lstrip('#'))
print(a.strip('#'))
print()

print('This Exmample to take input from user and print it ')

print('please Enter any text or number ')

ab = sys.stdin.readline()
print("Here the Entered Value is ",ab)
print(type(ab))
print()
print("PLease enter value as we are using Input Method ")
bc = input()
print('Your Entered Value is ', bc)
print(type(bc))

sys.stdout.write('Another exaample for  for STDOUT function \n')
print(sys.version)
print()

print('Please enter any character in Capital Letters')
for i in sys.stdin:
    if 'Q' == i.rstrip():
         break
    print("Entered Value is :  ", i)
print('exited from loop')
print()

sys.stdout.write('Example for STDOUT function \n')


def print_to_stderr(*a):
 
    # Here a is the array holding the objects
    # passed as the argument of the function
    print(*a, file = sys.stderr)
 
print_to_stderr("Hello This is for STD ERROR example ")
# print(abc)
print()

age = 19
if age < 18:
    sys.exit('You are not eligible to vote')    
else:
    print('You are eligible to Vote')
    print('You can also contest in elections')
print('Welcome to sys.exit function ')

print(sys.path)