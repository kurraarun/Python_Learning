# This excercise for Exception Handling
try:
    print()
    print(x)
except:
    print('Exception was handled')

print()
# Else is to use if there is no exception the else block also runs

try:
    x = 10
    print("X value is  ",x)
except:
    print('There is no exception to raise')
else:
    print('No Exception so executed from Else block')
print()

#finally block will execute irrespective of whether any error raised in Try block or not

try:
    x = 10
    print("X value is  ",x)
    print("y value is  ",y)
except:
    print('There is an exception to raise')
finally:
    print('Though there is an exception, its executing from Finally Block')
print()


try:
    f = open("hello.txt")
    try:
        f.write("Hello Moto")
    except:
        print('This is executing as the file hello.txt is available, But unable to write the content into it ')  # this executes if the file available and not able to write
    finally:
        f.close()
except:
    print('This executes if the file hello.txt is not avaialble in the system ')  # this executes if the file itself not available to write

print()

# Raise exception manually 

x = -1

#if x < 0:
#    raise Exception("Exception raised by manually ")
#    raise TypeError("Error")
#print('after raised exception manually')

# This excercise to learn how can we pass run time values

username = input("Enter username:")
print("Username is: " + username)

print()
# Here discussing how to open a file

f = open("hello.txt", "rt")
print(f.read())


