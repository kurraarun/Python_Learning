# This excercize on Dictionaries which is used to store value pairs

a_dict = {"Name " : "Kalam" ,
	   "Proffession" : "Scientist",
            "Year" : "2001",
		"Year" : "1999"}

print(a_dict)


a_cars = {'Type ' : 'Sedan ',
          'Make ' : 'Ford ',
	  'Model ' : 'Ikon ',
          'Year' : '2006',
          'Colors' : ['red','Blue' ,'black'] ,
          'Diesel'  : False}

print(a_cars)

print(type(a_cars))

x = a_cars["Year"]
print(x)

y = a_cars.keys()
print(y)
a_cars['seats'] = 5
print(y)

z = a_cars.values()
print(z)
print()
# Adding items to Dictonary 

a_cars ['Gears'] ='Manual'
print(a_cars)

a_cars.update({'No_gears' : 4})
print(a_cars)

#  Nested Dictionaries
print()
car1 ={'Make' : 'Maruthi', 'Year': 1970}
print(car1)

car2 = { 'Make' :'Hyundai','Year': 2000}
print(car2)
my_cars = {'My car1':car1,
            'My Car2': car2 }

print(my_cars)