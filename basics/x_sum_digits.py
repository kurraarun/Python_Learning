# This excercise to practice Python Recursion

a = []    # 2,4,5

b = int(input("Please enter the number to find the sum of Digits by Recursive way : "))

def sum_digit(x):
    if x == 0:
        return 1
    digit = x%10
    a.append(digit)

    sum_digit( x //10)


sum_digit(b)
print(sum(a))