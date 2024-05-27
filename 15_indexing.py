text = "Ella sabe python"
#Imprime el caracter que se encuentre en la posicion establecida
print(text[0])
print(text[1])
#print(text[999]) si le das una posicion que no existe marca error
size = len(text)
print("size => ",size)
print(text[size - 1])
print(text[-1])

#slicing Sacar siertas partes del texto
print(text[0:5])
print(text[10:16])
#Si no le envias nada en automatico iniciara en cero
print(text[:10])
print(text[5:-1])
print(text[5:])
print(text[:])
#Saltos
print(text[10:16:1])
print(text[10:16:2])
print(text[::2])