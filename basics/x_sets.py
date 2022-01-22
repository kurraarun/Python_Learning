# This excercise for Sets 
print()
print('''Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary.
all with different qualities and usage. ''')

print()

print("Sets are Unordered, which means we can't sure which order they will display . we can't refer them by index as well")

a_set = {'Cricket','Squash','Kabbadi','Hockey'}
print()
print(a_set)

b_set = {'Cricket' , 28 , 'Kabaddi' , 32.11, 'Hockey' , True}

print(b_set)
print(type(b_set))
print()

# Another way of defining set 

c_set = set (( 'Billiards' , 54,'Carroms' ,45.3 ))

print(c_set)

# we can combine different sets

fruit_set = {'apple','banana','guava'}
print(fruit_set)

veggies_set = {'Beans','Tomato','Bottle guard'}
print(veggies_set)
print()
fruit_set.update(veggies_set)
print(fruit_set)


# Remove and Discard functions can be use to remove any item from the set

fruit_set.remove('apple')

print(fruit_set)
fruit_set.discard('banana')
print(fruit_set)

# There are different methods which we can join two sets

s1 ={'a','b','c'}

s2 = {1,2,3,4}

s3 =s1.union(s2)
print(s3)
print()

s1 ={'x','y','z', 3, 6}

s2 = {1,'g',3,'y',5}

s3 = s1.intersection(s2)
print(s3)
print()

s1 ={'x','y','z', 3, 6}
s2 = {1,'g',3,'y',5}

s3 = s1.symmetric_difference(s2)
print(s3)

s3.add('d')

print(s3)

 