
# Python having 4 different data types which holds the collection of data 
print()
print('Here is the list from List type variable')
dif_dat_type = ["List",'Tuple',"Set","Dictionary"]
print( dif_dat_type)
print()

print('Here is the list from Tuple type variable')
tuple_dtp = ('List','Tuple' ,'Set','Dictionary' )
print(tuple_dtp)

#anthoer way of defining tuple data type
atuple = tuple(('apple','orange','mango','kiwi'))
print(atuple)

print()

#This is practicing the tuples 

a=len(tuple_dtp)
print(a)

tuple_dtp = ('List','Set', 'Tuple','Dictionary')
print(tuple_dtp)

print()
print('this one is not tuple')
a_tuple = ('harry')
print(a_tuple)

print()
a_tuple = ('harry',)
print(a_tuple)
print(type(a_tuple))

#assigning multiple data type values

a_multi_tuple = ('Harry',23,True,'Potter',65,'Amazon','world','wonderful')
print(a_multi_tuple)

# Pritning the tuple values in different position based on index
print(a_multi_tuple[3])
print(a_multi_tuple[-2])
print()

print(a_multi_tuple[2:6])

# Once a tuple is created, we can't change its values. Tuples are unchangeable.
# But there is a workaround. convert the tuple into a list and change the list and convert the list back into a tuple.
print()
print(atuple) # ('apple', 'orange', 'mango', 'kiwi')

abc = list(atuple)
abc[1] = 'banana'
print(abc) 
atuple = tuple(abc)
print(atuple)

print("we can append the values to Tuple by convert them into list and append the values and convert them again into Tuple")

print(""" In Python we can extract values from List into Variable , 
This called as Un packing """)

a,b,c,d = atuple

print(a)
print(b)
print(c)
print(d)
print()

a,b,*c = atuple

print(a)
print(b)
print(c)

