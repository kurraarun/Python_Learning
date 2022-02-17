# This excercise to print the number into reverse order

a = int(input("Please enter the number to print in Reverse order : "))
b = a
rev = 0
print()
while a > 0 :
    c = a%10
    rev = rev *10 + c
    a = a//10
print("The Reverse order of %d is  %d " %(b ,rev))
print()
if b == rev:
    print('The Entered Number is Palindrome')
else:
    print('The Entered Number is not Palindrome')
