"""
https://github.com/AeroPython/Curso_AeroPython/tree/master/notebooks_completos
"""

"""
Funciones especiales con Scipy
https://github.com/AeroPython/Curso_AeroPython/blob/master/notebooks_completos/030-SciPy-FuncionesEspeciales.ipynb
"""
import numpy as np
from scipy import special
import matplotlib.pyplot as plt

x = np.linspace(2, 9, 100)

for ii in range(5):
    plt.plot(x, special.jn(ii, x))
plt.grid(True)




"""
https://github.com/AeroPython/Curso_AeroPython/blob/master/notebooks_completos/031-SciPy-CalculoIntegrales.ipynb
"""
from scipy import integrate


def fun(x):
    return x * np.sin(x)

"""
Vamos a aplicar el concepto de funcion lambda

OJO,... no es una funcion lambda, es una variable que apunta a otra funcion
"""
mi_int = integrate.trapz
value = mi_int(fun(x), x)
print("El resultado es: ", value)


mi_int = integrate.simps
value = mi_int(fun(x), x)
print("El resultado es: ", value)

"""
Es decir, puedo escribir codigo consistente, que me permita cambiar en las opciones al principio que integrador usar

Si quiero usar una lambda:
"""


value = mi_int(x * np.sin(x), x)
print("El resultado es: ", value)



"""
Estadistica
https://github.com/AeroPython/Curso_AeroPython/blob/master/notebooks_completos/032-Scipy-Estadistica.ipynb



Interpolacion y ajuste de datos
https://github.com/AeroPython/Curso_AeroPython/blob/master/notebooks_completos/033-SciPy-InterpolacionAjuste.ipynb



Resolver ecuaciones
https://github.com/AeroPython/Curso_AeroPython/blob/master/notebooks_completos/034-SciPy-EcuacionesNoLineales.ipynb



Sistemas de EDOS
https://github.com/AeroPython/Curso_AeroPython/blob/master/notebooks_completos/035-SciPy-EcuacionesDiferencialesOrdinarias.ipynb
"""
#########

plt.show()