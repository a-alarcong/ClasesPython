import numpy as np

a = np.sqrt(2)
print(a)

print(np.pi, np.e)

miarray = np.array([1, 2, 3])
miarray.astype(np.float16)
print(type(miarray[0]), miarray)


N = 100
M = 100

a = np.empty(N*M).reshape(N, M)
b = np.random.rand(N*M).reshape(N, M)
c = np.random.rand(N*M).reshape(N, M)

import time
start = time.time()
for i in range(N):
    for j in range(M):
        a[i,j] = b[i,j] + c[i,j]

print("El bucle tardo", time.time() - start)

start = time.time()
a = b + c
print("La suma tardo", time.time() - start)

miarray2 = np.array([[0, 1, 2],[3, 4, 5]])
print(type(miarray2), miarray2)

print(miarray2[:,0])


# Otras formas de generar arrays
miarray = np.empty((2,2))
miarray = np.identity(2)
miarray = np.eye(2,3)
print(miarray)


print(np.linspace(0, 7.3, 5))
print(np.logspace(0, 7.3, 5))

miarray = np.empty((2,2))
miarray2 = np.zeros((2,2))
miarray3 = np.zeros((2,2)) + np.float16(0.000002)*np.random.rand(2,2)

#print(np.all(miarray==miarray3))

#print(miarray==miarray2)

print("*******************")
print(np.isclose(miarray2, miarray3,atol=.0000001))
