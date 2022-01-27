
# Iterators

my_tuple = ('Apple','Banana','Orange','Grapes','Cherry')

my_iterator = iter(my_tuple)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

my_string = 'Hello'

my_str_iterator = iter(my_string)

print(next(my_str_iterator))
print(next(my_str_iterator))
print(next(my_str_iterator))


# To understand the scope of the variable
print('I am here in outer block  ')
x = 300
def func1():
    x = 200
    print('I am here in local block x is  ' ,x)
print()
func1()
print('I am here at outer block  x is ' , x)
print()

# to define the variables anywhere and making them as global

def func1():
    global x 
    x = 200
    print('I am here in local block, But variable is Global  x is  ' ,x)
print()
func1()
print('I am here at outer block  x is ' , x)

