# This excersize is to understand about the functions in Python

def minnum(y):
    min = y[0] 
    for i in y:
        if i < min:
            min = i
    return(min)
print()
x =  [43,52,64,65,34,21,32,23,21,54,65,89]
print()
print('Original list ' ,x)
abc = minnum(x)
print("Smallest Number in the given List is : ",abc)


# By this way we can pass any number of arguments

def student_name(**std):
    print("Student First Name " + std["fname"])
    print("Student Last Name " + std["lname"])

student_name(fname="Kishore" , lname="kumar")

