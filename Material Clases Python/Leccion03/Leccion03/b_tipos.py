"""
Datos simples
1 - Numeric
2 - Strings / caracteres
3 - Booleans

Colecciones de datos
4 - List
5 - Tuples
6 - sets
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
# asd

mistring = """a
\n sdf
"""
mistring = r"\n a"

print(type(myString), myString) # comentario en linea
print(myString2)
print("valor 1" + str(miVar))
if miVar:
    print(mistring)

