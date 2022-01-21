# This excercise for different operations on strings

string1 = 'Hello'

string2 = ' '

string3 = 'Moto'

string4 = string1 + string2 + string3

print(string4)

print(string1 + string2 + string3)

print('Hello' + ' ' + 'Moto')

print()
# Single Variable saving multiple lines 

a = """Hello this Example 
for Printing 
Multiple Lines under One variable"""

print(a)

print('''Python is powerful language 
and its simple 
and its open source language ''')

b = 'PYTHON'

p,q,r,x,y,z = b

print (p)
print(q)
print(r)
print(x)
print(y)
print(z)

concat_st = p+q+r+x+y+z

print(concat_st)


a = ['abc' ,'xyz','pqr','stg']

print( a[0])

print('hello \t tablespace')
print()

# Function to identify the starting or ending string

a ="Hello World!"
print(a.startswith('hello'))
print(a.endswith('World!'))
print()

# Split the string and assign to different variable

a="Arun Kumar Kurra"
print(a.split(" "))

b = a.split(" ")
print(b)

a ="Helloaworldaworldisabigaenough"

print(a.split("a"))



# Swap the each letter in the given string from Lower case to Upper and Upper case to Lower
str1 = 'hello world'
print(str1.swapcase())

str2 = 'HELLO WORLD'
print(str2.swapcase())

str3 = 'Hello World'
print(str3.swapcase())

str2 = 'HELLO WORLD'
print(str2.isupper())

str1 = 'hello world'
print(str1.islower())