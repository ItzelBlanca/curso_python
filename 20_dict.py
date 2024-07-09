person = {
    'name':'Itzel',
    'last_name':'Ruiz',
    'langs':['python','javascript'],
    'age':26 
}

print(person)
#Actualizar / Modificar
person['name'] = 'Blanca'
person['age'] -= 10
person['langs'].append('rust')
print(person)
#Eliminar
del person['last_name']
person.pop('age')#Cuando se trabaja con diccionarios en el pop se tiene que especificar que llave se quiere eliminar 
print(person)

print('items')
print(person.items())#Muestra atributos y valores en tuplas

print('keys')
print(person.keys()) #Muestra los atributos no se fija en los valores

print('values')
print(person.values())#Mustra solo los valores