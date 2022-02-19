

def count_set_bits(n):
    count = 0
    while n:
        print('hello : ',n)
        n &= n - 1
        print(n)
        count += 1
    return count
 
 
n = int(input('Enter n: '))
print('Number of set bits:', count_set_bits(n))