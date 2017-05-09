#a asd
import Leccion3.a_moduloBasico

print(Leccion3.a_moduloBasico.sqrt, Leccion3.a_moduloBasico.sqrt(4))

import math
print(math.sqrt, math.sqrt(4))


"""
 importar solo una funcion del modulo
"""
from math import sqrt, sin

print(sqrt(4))

from Leccion3.a_moduloBasico import sqrt
print(sqrt(4))

"""
math = 5
from math import math.sqrt
"""

# Para importar todas las funciones
from math import *
cos(4)

import math as mt
mt.cos(45)