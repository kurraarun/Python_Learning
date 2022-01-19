x=1
if x == 1:
    print("x is one")
x = 8
print(x)
x = 7.4
print(x)
x = float(8)
print(x)
x = 'string1'
print(x)
x = "string2"
print(x)
x="My son's Birthday"
print(x)
x=1
y=2
z = x + y
print(z)
X = 5
print(x)
print(X)
x = "arun"
y = "kurra"
z = x + " " + y
print(z)
x,y = 2,4
print(x,y)
print(x)
print(y)


mystring = None
myfloat = None
myint = None
print(mystring)
print(myfloat)
print(myint)

mystring = "hello"
myfloat = 10.0
myint = 20
if mystring == "hello":
    print("String : %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float : %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Int : %d" % myint)
mylist = []
mylist.append(100)
mylist.append(200)
mylist.append(300)
print(mylist[0])
print(mylist[1])
print(mylist[2])
for x in mylist:
    print(x)

mylist = [5,6,7,8]
print(mylist[1])
numbers1 = []
srings1 = []
names = ["arun","kumar","kurra"]
print("my second name is  " + names[1])
myseond = None
myseond = names[1]
print("my second name %s" %myseond)

numb= 4 + 2 * 3 / 4.0
print(numb)
x = 'hello '
print(x * 7)
x = [1,2,3,4]
y = [5,6,7,8]
print(x + y)
print(x * 3)

a = object()
b = object()

a_list = [a] * 10
b_list = [b] * 10
ab_list = a_list + b_list
print("list contains %d " % len(a_list))
print(len(b_list))


a = "Arun"
b=40
print("Hello %s! your age is %d" %(a,b))
a = [1,'arun',2,'kumar',45.232]
print("Hello %s" %a)

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."
a_string = 'hello'
print(a_string + " " + data[0] +" " + data[1] + ". Your current balance is %.2f" %data[2] )

print(format_string  % data)

a ="Hello World!"

print(a.startswith('Hello'))
print(a.startswith('hello'))
print(a.endswith('World'))
a="Aruna Kumar Kurra"
print(a.split(" "))

a="Arun"
age =41
a_string = ("Aruna",41)
if a == "Arun" and age == 41:
    print("Your name is %s and you are also %s years old." %a_string )

a=12
b=23
if (a == 12 and b == 24):
    print('hai')
print('Its in out of If condition')

x = 2
y = 2
if x == 2:
    print('x having value as 2  ')

print( x == 2)

print ( x is 4)


x = [1,2,3,4,5,6]
for i in x:
    print(i)
for i in range(10):
    print(i)
print("new range")
for i in range(1,13):
    print(i)
print('different range')
for i in range(1,25,4):
    print(i)

count = 0
while count < 5: 
    print(count)
    count += 1
print('new conditions')
c = 0
while True: 
    print(c)
    c += 1
    if c == 5:
        break 
print('new conditions for Continue ')
for x in range(10):
    #print(x)
    if x % 2 == 0:
        #print(x)    
        continue
    print(x)    
numbers = [951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527]  
for i in numbers:
    if i == 237:
        break  
    elif i % 2 == 0:
        print(i)
def my_first():
    print("My First Function")
def my_func_arg(a):
    for i in a:
        print(i)
my_first()
x = "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"
y= "Kurra"
my_func_arg(x)
x = [25,6,1,7,32,9,19,51,8]
print(max(x))
print(min(x))
x.sort()
y = x
print('Sorting new')
for i in y:
    print(i)



def list_benefits():
    a = ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]
    return a

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    abc = "%s  is a benefit of functions!" %benefit
    return abc

test = list_benefits()
#print("%s" %test[0])
for i in test:
    #print("%s is a benefit of functions!" %i)
    aa = build_sentence(i)
    print(aa)

class myfirstclass:
    a ='hai'
    def myfunction(hello):
        print("My function under class")
abc = myfirstclass()
print("%s Arun" %abc.a)

abc.myfunction()
