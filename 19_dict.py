my_dict = {}
print(type(my_dict))

my_dict = {
    'name': 'Itzel',
    'last_name':'Ruiz Garcia',
    'age':26
}

print(my_dict)
print(len(my_dict))

print(my_dict['age'])
print(my_dict['last_name'])
print(my_dict.get('age'))#Con get si no encuentra el dato no dettiene la operación

print('name' in my_dict)#Comprovamos si la palabra avion se encuentra en my_dict
print('otroqueno' in my_dict)