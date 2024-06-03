#crud create, Read, Update y Delete

numbers = [1, 2, 3, 4, 5]
print(numbers[1])
numbers[-1] = 10
print(numbers)
#append sirve para agregar un nuevo elemento
numbers.append(700)
print(numbers)
#inseta en la posicion 0
numbers.insert(0,'hola')
print(numbers)

numbers.insert(3, 'change')
print(numbers)
#Se van a fucionar los elementos que hay en numbers y los que hay en tasks
tasks = ['todo 1', 'todo 2', 'todo 3']
new_list = numbers + tasks
print(new_list)
#Preguntar en que posicion esta algun elemento
index = new_list.index('todo 2')
new_list[index] = 'todo changed'
print(new_list)
#Remover algun elemento
new_list.remove('todo 1')
print(new_list)
#elimina elementos
new_list.pop()
print(new_list)

new_list.pop(0)
print(new_list)
#voltea todo el list
new_list.reverse()
print(new_list)
#ordena el arreglo
numbers_a = [1, 4, 6, 3]
numbers_a.sort()
print(numbers_a)

strings = ['re', 'ab', 'ed']
strings.sort()
print(strings)

#new_list.sort() no se puede ordenar si tiene elementos mezclados

