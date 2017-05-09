"""
Mas tutoriales, informacion de numpy, scipy, matplotlib,...

http://pybonacci.org/tag/aeropython/

http://pybonacci.org/2015/10/15/curso-de-python-en-la-etsiae-4a-edicion/#more-3491
https://github.com/AeroPython/Curso_AeroPython

"""

from __future__ import print_function, division
import numpy as np

"""
Numpy da acceso a una serie de librerias matematicas

TODO: comprobar como mejorar la precision
"""

print("%.20f" %(1/3,))
print("%.20f" %(np.float64(np.float64(1)/np.float64(3)),))


print("sqrt(2)=%s, cos(90)=%s" %(np.sqrt(2), np.cos(90),))
print("OJO, RADIANES\n")

print("Pi=%.20f, e=%.20f" %(np.pi, np.e,))

"""
Tambien me permite trabajar con arrays
Esto habilitara vectorizar funciones, y evitar bucles (no siempre) con operaciones algebraicas

"""

# Un array se inicializa como una lista

miarray = np.array([1, 2, 3])
print(type(miarray[0]), miarray)
miarray = np.float64(miarray)
print(type(miarray[0]), miarray)


#Importo el modulo time para hacer un pequeño profile de dos funciones
import time
N = M = 100 #Si, puedo inicializar dos variables iguales asi

a = np.empty(N*M).reshape(N, M)
print("\nArray 'vacio:\n'", a[0:2,0:2])
b = np.random.rand(N*M).reshape(N, M)
c = np.random.rand(N*M).reshape(N, M)

#suma de dos matrices elemento a elemento mediante bucle
start = time.time()
for i in range(N):
    for j in range(M):
        a[i,j] = b[i,j] + c[i,j]
print("\n")
print("El bucle tardo %.3e" %(time.time() - start,))

start = time.time()
a = b + c
print("La suma matricial tardo %.3e" %(time.time() - start,))


"""Si quiero un bucle con numeros consecutivos,...
Evito bucles
"""

print()
arr1 = np.arange(10)
print(type(arr1), arr1)
arr2 = np.arange(10, 3, -1)
#arr2 = np.arange(3, 10, -1)
print(type(arr2), arr2)

print()
print("Espaciado lineal:", np.linspace(0, 7.3, 5))
print("Espaciado logaritmico:", np.logspace(0, 100, 3))


"""Importacion de datos
https://github.com/AeroPython/Curso_AeroPython/blob/master/notebooks_completos/012-NumPy-Importacion.ipynb
"""