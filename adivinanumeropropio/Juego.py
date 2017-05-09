__author__ = 'Álvaro'

import random

incognita = random.randint(1, 10)
#print(incognita)

for i in range(1, 4):
    print("intento", i)
    usuario = input("Introduce un valor entero entre 1 y 10")
    if int(usuario) == incognita:
        print("Acertaste!")
    else:
        print("Otra vez será")