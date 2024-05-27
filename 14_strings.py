text = "Ella sabe programar en python"
# in Verificar si un subtexto se encuenra dentro de sus sub variables 
'''
print('JavaScript' in text)
print('python' in text)
if "python" in text:
    print("Elegiste bien")
else:
    print("Tambien elegiste bien")
#len nos dice el numero de caracteres los espacios tambien son contados
'''
size = len(text)
print(size)

print(text)
#Todo lo pasa a mayusculas
print(text.upper())
#Todo lo pasa a minuscula
print(text.lower())
#Cuenta el numero de apariciones en especifico
print(text.count("a"))
#Transforma todas las letras que esten en mayuscula en minuscula y las minusculas en mayusculas
print(text.swapcase())
#Sirve de manera de consulta nos responde de manerara boleana
print(text.startswith("Ella"))
print(text.endswith("Rust"))
#Remplazar
print(text.replace("python", "Go"))

text_2 = "este es un titulo"
print(text_2)
#Pone la primera letra en mayuscula
print(text_2.capitalize())
#Lo combierte a titulo
print(text_2.title())
#Nos dice si el texto es un dgito
print(text_2.isdigit())
print("398".isdigit())
