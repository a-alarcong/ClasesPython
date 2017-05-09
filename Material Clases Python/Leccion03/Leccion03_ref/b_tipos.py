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

"""
Dentro de esos, se pueden considerar secuenciales
2 - Strings
4 - List
5 - Tuples


(tb se puede iterar en las llaves/valores de los diccionarios y en los sets)

"""

"""
https://docs.python.org/3/tutorial/introduction.html#numbers
"""
# 1 - Datos numericos
miVar = 2
miVar2 = 2.

print(type(miVar), miVar)
print(type(miVar2), miVar2)

suma = 1 + miVar
resta = 1 - miVar
multiplicacion = 2 * miVar
division = 1/float(2)
divisionentera = 1.0 // 2.0
modulodivision = 1.0 % 2.0
print(divisionentera)
print(modulodivision)

# 2 - Strings
myString = "my string"
myString2 = 'my other string'

print(type(myString), myString)
print(myString2)
print("esto es un %s" %("string",))

# 3 - Booleans
varTrue = True
varFalse = False
print(type(varTrue), varTrue)

# 4 - List
myList = [1, 2, 3]
myList = list([1, 2, 3])
myList = [1, True, "string"]
myList2 = [1, myList]
print(type(myList), myList)
print(type(myList2), myList2)

# 5 - tuplas
myTuple = 1, 2, 3
myTuple2 = (1, 2, 3)
myTuple = tuple([1, 2, 'string'])
myTuple = (1,)
print(type(myTuple), myTuple)
print(type(myTuple2), myTuple2)

# Datos mutables vs inmutables
myTupla = (1, 2, 3)
milista = [1, 2, 3]
print(id(myTupla), type(myTupla), myTupla)
print(id(milista), type(milista), milista)

#myTupla[0] = 'hola'
myTupla = 'hola',
milista[0] = 'hola'
print(id(myTupla), type(myTupla), myTupla)
print(id(milista), type(milista), milista)
milista = ['hola']
print(id(milista), type(milista), milista)

# 6 - sets
lista  = [1, 1, 'hola', 0, 'hola', 'hola']
miSet  = set(lista)
miSet2 = {1, 1, "1"}


print(type(lista), lista)
print(type(miSet), miSet)
print(type(miSet2), miSet2)

# 7 - Diccionarios
miDiccionario = {'llave': 'valor', 1: 'unstring', 'unaclave': milista }
print(type(miDiccionario), miDiccionario)


#######
# Acceder a elementos de la colecion
# Diccionario
print(miDiccionario['unaclave'])

milista = [1, 2, 3, 4, 5]
posicion = [0, 1, 2, 3, 4]
posicion = [-5,-4,-3,-2,-1]

print(milista[0])
print(milista[1:3])
print(milista[1:])
print(milista[-1:])
print(milista[-1:-3:-1])
print(milista[-2::-2])
