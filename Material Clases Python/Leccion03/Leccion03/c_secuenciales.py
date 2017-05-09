"""
Dentro de esos, se pueden considerar secuenciales
2 - Strings
4 - List
5 - Tuples


(tb se puede iterar en las llaves/valores de los diccionarios y en los sets)
"""

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


