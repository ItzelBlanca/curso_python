name = "Itzel"
last_name = "Ruiz Garcia"
my_age = "26"
print(name)
print(last_name)
print(my_age)

full_name = name + " " + last_name + " y tengo " + my_age
print(full_name)

quote = "I'am itzel"
print(quote)

quote2 = 'she said "Hello"'
print(quote2)

#Format
template = "Hola, mi nombre es " +name +" y mi apellido es " + last_name + " y tengo " + my_age + " años"
print('v1',template)

template = "Hola, mi nombre es {} y mi apellido es {} y tengo {} años".format(name,last_name,my_age)
print('v2',template)

template = f"Hola, mi nombre es {name} y mi apellido es {last_name} y tengo {my_age} años"
print('v3',template)