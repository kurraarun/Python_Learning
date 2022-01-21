# This session is to deal with List of objects
a = []
print(a)
print('Its an empty List')
print(len(a))
print()

# append the values to existing list
a.append('cricket')
a.append('Football')
a.append('basketball')
a.append('Rugby')
a.append('Volleball')
a.append('Golf')
print(len(a))
print(a)
print()
# modifying the list with other values
a[2] = 'AmericanBasketball'
print(a)

# assigning the list values to other variables
x = a[2]
print(x)

# Inserting the items to the list

colors = ['red','green','blue','orange']

colors.insert(2,'yellow')
print(colors)

colors.insert(4,'pink')
print(colors)

colors.insert(6,'grey')
print(colors)

colors.insert(9,'Voilet')
print(colors)
print()

# Deleting the items from the list
colors.remove ('red')
print(colors)

print('removing one last item in the list')
colors.pop()
print(colors)

colors.pop(4)
print(colors)

del colors[1]
print(colors)

#print('Deleting all the values from the list')
#del colors

print('Clearing the list ')

colors.clear()
print(colors)
print()

# Copy the list into another 
colors = ['red','green','blue','orange']
fair_colors = colors 
print(colors)
print(fair_colors)

# Joining two lists
veggies =['potato','Brinjal','Bottleguard']

veg_color =  veggies + colors 

print(veg_color)

nums = [1,3,4,5,7]

veg_colors_nums = veg_color + nums
print(veg_colors_nums)
print()

# Reversing the list
print('Reverse the list')
veg_colors_nums.reverse()
print(veg_colors_nums)




















