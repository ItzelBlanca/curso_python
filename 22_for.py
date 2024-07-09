'''
for element in range(1, 21): #range crea un numero de iteraciones asta un numero dado 
    print(element)
    
'''
my_list = [23, 45, 67, 89, 43]
for element in my_list:
    print(element)
    
my_tuple = ('blanca', 'itzel', 'andrea')
for element in my_tuple:
    print(element)

#Diccionario
product = {
    'name':'camisa',
    'price':100,
    'stock':89
}
for key in product:
    print(key, '=>',product[key])
    
for key, value in product.items():
    print(key, '=>', value)
    
people = [#Diccionarios dentro de listas
    {
        'name':'itzel',
        'age':26
    },
    {
      'name':'blanca',
      'age':23  
    },
    {
        'name':'leandro',
        'age':30
    }
    ]

for person in people:
    print('name => ',person['name'])