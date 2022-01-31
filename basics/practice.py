# Practicing the Python

print('Hello welcome to Python')

print("Hello welcome to Python world")


if 5 > 12:
    print('5 greater than 12 ')
elif 5 == 5:
    print('5 equal to 12 ')
else :
    print('5 less than to 12')
''' Hello this is comments
section. here we can write any
comments which python wont execute the'''
print('End of comments section ')

x = 1

x = 'hai'
x= int(3)
x= float(3.3433)

print(x)

y = 1
print(type(y))
z= 'hello'
print(type(z))

a = 1
print(a)
_a = 2

print(_a)
_a_ = 3

print(_a_)

a_b = 3

print(a_b)

a,b,c,d,e = 'hello'

print(a)
print(b)
print(c)
print(d)
print(e)


a,b,c = ('Hello' , 'World','Python')
print(a)
print(b)
print(c)

a = 'Awesome '
print('Python is', a)

print('Python is'+ a)

x = 5
y = "John"
print(x , y)


x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x) 


abc ='Fantastic'

def myfunc():
    abc = 'Awesome'
    print('Python is ' + abc )
print('Python is ' + abc )

x = range(6)
print(x)

x = 5

print(type(x))

x = 5j

print(type(x))
print()
import random

print(random.randrange(1, 10)) 


for i in 'hello':
   print(i)
a =len('hello')
print(a)

a = [34,22,1343,2343,3,6,65]
for i in a:
    print(i)
    i += 1

a = 'hello'
for i in range(len(a)):
    print(i)
a = 'hello'
for i in range(len(a)):
    print(a[i])
print()
print('helo')
b = 'hello world!'

print(b[2:7])
print()

b = 'hello world!'
print(b[:7])
print()

b = 'hello world!'
print(b[2:])

print(b[-4:-2])

a = "Hello, World!"
print(a.upper())
print(a.lower())

print()
try:
    print('Hello this is try and exception ')
    print(abcd)
except NameError:
    print('This is Nameerror Exception')
except:
    print('Here we are in exception')