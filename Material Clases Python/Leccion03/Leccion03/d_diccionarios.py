
midict = {1:"valor", "1":"otrovalor","llave":list([1, 2, 3]) }

print(type(midict), midict)
print(midict[1])
print(midict["llave"])

miPuntero = midict["llave"]
miPuntero.append(1)
print(midict["llave"])

print(midict.keys())
print(midict.items())

for llave in midict.keys():
    print(llave, midict[llave])

for llave, valor in midict.items():
    print(llave, valor)


milista1 = [1, 2, 3]
milista2 = [3, 4, 5, 6]
milista3 = [7, 8, 9, 10, 11]

#zip para empaquetar varias listas e iterar de golpe
for i, j, k in zip(milista2, milista1, milista3):
    print(i, j, k)


for _ in range(0,3,2):
    print(milista3[_])
