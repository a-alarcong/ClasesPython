"""
https://github.com/AeroPython/Curso_AeroPython/blob/master/notebooks_completos/034-SciPy-EcuacionesNoLineales.ipynb

https://docs.scipy.org/doc/scipy-0.18.1/reference/optimize.html

"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize


def F1(x):
    return np.log(x) - x*np.sin(x)


x = np.linspace(0, 10, num=100)

plt.figure(1)
plt.plot(x, F1(x), 'k', lw=2, label="$F(x)$")
plt.plot(x, np.log(x), label="$\log{x}$")
plt.plot(x, np.sin(x), label="$\sin{x}$")
plt.plot(x, np.zeros_like(x), 'k--')

solucion = optimize.brentq(F1, 0, 10)
solucion2 = optimize.fsolve(F1, 10)

plt.plot(solucion, F1(solucion), 'o', color='black')
plt.plot(solucion2, F1(solucion2), 'x', color='red')


plt.legend(loc=4)

"""
Las funciones pueden ser multivariable
"""


def F2(x):
    x1 = x[0]
    x2 = x[1]
    f1 = x[0]*np.cos(x[1]) - 4
    f2 = np.log(x[0]) - x[0]*np.sin(x[0])
    return [f1 , f2]

solucion3 = optimize.fsolve(F2, [1, 0])
print(solucion3)

x1 = x[0:len(x)-1]
x2 = x[1:len(x)]

cambiosdesigno = np.sign( F1(x1)* F1(x2))
plt.figure(2)
plt.plot(x1, cambiosdesigno)


indices = np.where(cambiosdesigno==-1)
print(indices[0], x1[indices[0]])
print(indices[0], x2[indices[0]])

print(np.sign(0))

print(np.log(0)/np.log(0))

plt.show()