import Leccion2.a_moduloBasico

print(Leccion2.a_moduloBasico.sqrt, Leccion2.a_moduloBasico.sqrt(4))

import math
print(math.sqrt, math.sqrt(4))


"""
 importar solo una funcion del modulo
"""
from math import sqrt, sin

print(sqrt(4))

from Leccion2.a_moduloBasico import sqrt
print(sqrt(4))

"""
math = 5
from math import math.sqrt
"""

from math import *  # Para importar todas las funciones
cos(4)

import math as mt
mt.cos(45)