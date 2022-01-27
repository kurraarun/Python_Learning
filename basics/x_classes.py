# This excercise to learn Classes and Objects 

class abc:
    x = 5

a = abc ()
print('Printing value from Class through Object ')
print('Here the value of x is ' , a.x)

class my_class:

# The __init__() function is called automatically every time the class is being used to create a new object.

    def __init__(self, fname, lname , age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def my_details(self):
        print("Hello My Name " +self.fname + " " + self.lname  )   
        print("Hello age is " , self.age )
c1 = my_class("Kunal",'Kumar', 34)
c1.my_details()


# We can create sub class under the class


