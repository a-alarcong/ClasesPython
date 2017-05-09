"""
Otra tecnica para evitar bucles, (y habrá alguna mas que me haya dejado

Es vectorizar la funcion (numpy) o utilizar las funciones map, reduce, filter,... (alguna estaba deprecada ya)
"""

milista = list(range(0, 11))

tupla = (1, 2, 3)
mifun = lambda x: x**2

valores = map(lambda x: x**2, milista)


print(type(valores), valores)
print("Me genera un iterable,... pero tengo que iterar para sacarlo")
print("Con una list / ... comprenhension sera mas facil")
for elem in valores:
    print(elem,end=", ")
print("\n")


# filter()
print("Filter:", filter(lambda x: x % 3 == 0, milista))

print("Map:", map(lambda x: x * 2 + 10, milista))

# Aplicar de forma recursiva la misma operacion, deprecado, hay que hacer una importacion
from functools import reduce
print("Reduce:", reduce(lambda x, y: x + y, milista))



import numpy as np
mifun_vec = np.vectorize(mifun)
valores2 = mifun_vec(milista)
print(type(valores2), valores2)