"""
Datos simples
1 - Numeric
2 - Strings / caracteres
3 - Booleans

Colecciones de datos
4 - List
5 - Tuple
6 - Set
7 - Dictionary
-------
8 - Clases
9 - ficheros
"""

# 1 - Datos numericos
miVar = 2
miVar2 = 2.

print(type(miVar), miVar)
print(type(miVar2), miVar2)

print(1 / 2)
print(1.0 // 2.0)

# 2 - Strings
myString = "my string"
myString2 = 'my other string'

mistring = """a
\n sdf
"""
mistring = r"\n a"

print(type(myString), myString) # comentario en linea
print(myString2)
print("valor 1" + str(miVar))
if miVar:
    print(mistring)

# 4 - List
miLista  = list() #una lista vacia
miLista2 = list([1, "uno", "1"])
print(id(miLista2), type(miLista2), miLista2)

miLista2 = list((1, "uno", "2"))
miLista3 = [1, "uno", "3","5"]
miLista4 = [1, "uno", "3","5"]

"""
print(id(miLista), type(miLista), miLista)
print(id(miLista2), type(miLista2), miLista2)
print(id(miLista3), type(miLista3), miLista3)
"""""

print(id(miLista4), type(miLista4), miLista4)

miLista4.append("el quinto elemento")
print(id(miLista4), type(miLista4), miLista4)

miLista5 = miLista4
mielem = miLista5.pop()
print(mielem)
print(id(miLista4), type(miLista4), miLista4)

import copy

miLista6 = copy.copy(miLista4)
miLista6.extend([1,2,3])
print(id(miLista4), type(miLista4), miLista4)
print(id(miLista6), type(miLista6), miLista6)
miLista6.append([1,2,3])
print(id(miLista6), type(miLista6), miLista6)

# 5 - Tuple
mitupla = (1, 2, 3)
mitupla = tuple((1, 2, 3))
mitupla = tuple([1, 2, 3])

print(id(mitupla),type(mitupla), mitupla)

mitupla = 1,
mitupla = 1, 2
print(id(mitupla),type(mitupla), mitupla)

# 6 - Set
miset = {1, 1, 1, 1, 2, "1"}
print(id(miset),type(miset), miset)

# 7 - Dictionary
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