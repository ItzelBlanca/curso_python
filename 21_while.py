'''
while True: #While es mientras la condicion se cumlpa se ejecutara
    print('se ejecuto')

counter = 0
while counter < 10:
    counter += 1
    print(counter)


counter = 0

while counter < 20:
    counter += 1
    if counter == 15:
        break #Se rompe de una manera forzada
    print(counter)
'''
counter = 0

while counter < 20:
    counter += 1
    if counter < 15:
        continue #Salta a la siguiente iteracion hasta que se cumpla la condicion 
    print(counter)