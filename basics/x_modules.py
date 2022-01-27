# This session is for Modules 

import x_function   # this is another file we are importing to here

x_function.student_name(fname="Kishore" , lname="kumar")
print()

# Importing the standard functions as well
import datetime    

x = datetime.datetime.now()
print(x) 
print(x.year)
print(x.strftime("%A")) 
print(x.month)
print(x.day)
print(x.strftime("%B")) 

print(x.strftime("%c"))

import math

x = math.ceil(1.4)
y = math.floor(1.4)

print('1.4 ceil value is ' ,x)

print('1.4 floor value is ' ,y)

x = math.sqrt(64)

print('Sq root of 64  is ',x) 


import re

txt = "The war may began in Taiwan"
x = re.search("^The.*Taiwan$", txt) 
print(x)

y = re.findall("an",txt)
print(y)


try:
    print(c)
except:
    print("Welcome to Excepion handler")