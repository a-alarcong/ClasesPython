"""
https://github.com/AeroPython/Curso_AeroPython/blob/master/notebooks_completos/014-NumPy-AlgerbraLineal.ipynb

"""
import numpy as np

M = np.array([
    [1, 2],
    [3, 4]
])

v = np.array([1, -1])


u = np.dot(M, v)
print ("M.v=", u)

print("Determinante:")
print(np.linalg.det(M))

print("Inversa:")
print(np.linalg.inv(M))

print("Autovectores:")
print(type(np.linalg.eig(M)), np.linalg.eig(M))

print("\nDescomprimo la tupla de salida con otra tupla")
(autovalor, autovector) = np.linalg.eig(M)
print("autovalor:", autovalor)
print("autovector:", autovector)