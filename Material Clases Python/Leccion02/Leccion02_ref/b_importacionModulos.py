"""
Se puede importar un modulo/paquete entero con la sentencia import

Para acceder a una función o clase del modulo, accedo con un punto
En el fondo, es un objeto mas

"""
import math
print(math.sqrt, math.sqrt(2))


"""
si el nombre es muy largo podemos asignarle otra etiqueta, como si fuese una variable mas
"""
import numpy as np
print(np.sqrt, np.sqrt(2))


"""
Ahora solo quiero una funcion especifica del modulo
"""
from numpy import sqrt
print(sqrt(2))

from numpy import sqrt as hector
print(hector(2))

"""
O podemos importar todo lo que tenga el paquete
"""
from Leccion3.a_moduloBasico import *
print(sqrt(2))