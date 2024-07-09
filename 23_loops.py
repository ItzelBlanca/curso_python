matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ] #Es una lista que tiene listas

print(matriz[0][1])

for row in matriz:
    print(row)
    for column in row:
        print(column)