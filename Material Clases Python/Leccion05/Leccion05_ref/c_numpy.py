import numpy as np

# Otras alternaticas de generar arrays

print("Array de varias dimensiones,.... lista de listas de ...")
miarray2 = np.array([[0, 1, 2], [3, 4, 5]])
print(type(miarray2),"\n", miarray2)

"""
Puedo indexar como una lista de una lista,...
O como si fuese una matrix (matlab)
"""

print("\nIndexacion")
print("Cuidado,... que estoy pidiendo cosas distintas")
print(miarray2[:][0])
print(miarray2[:, 0])
print(miarray2[:, 1:3])


"""
Tambien puedo inicializarlo con ciertos valoes,...
"casi identidad": eye, identity
Ceros, vacia

Ojo,... vacia no es vacia,... es casi vacia
"""

print("\n")

miarray1 = np.empty((2,2))
miarray2 = np.identity(2)
miarray3 = np.eye(2,3)
print("Vacia:\n", miarray1)
print("Vacia: %.3e\n" %(miarray1[0,0],))
print("Identidad:\n", miarray2)
print("Diagonal de unos:\n", miarray3)


"""
Puedo hacer comparaciones de matrices, evitando bucles,

Os dejo buscar como hacer intersecciones, uniones, diferencias de conjuntos de elementos,...
"""

miarray = np.empty((2,2))
miarray2 = np.zeros((2,2))
miarray3 = np.zeros((2,2)) + np.float16(2e-7)*np.random.rand(2,2)


#print(np.det(miarray))

print(np.all(miarray == miarray3))
print(np.all(miarray2 == miarray3))
print(miarray == miarray2)

print("*******************")
print(np.isclose(miarray2, miarray3, atol=1e-7))

print(np.divide(1,1e-6))