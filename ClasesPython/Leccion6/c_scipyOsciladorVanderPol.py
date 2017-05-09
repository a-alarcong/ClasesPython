"""
https://en.wikipedia.org/wiki/Van_der_Pol_oscillator

https://github.com/AeroPython/Curso_AeroPython/blob/master/notebooks_completos/035-SciPy-EcuacionesDiferencialesOrdinarias.ipynb
"""
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

"""
Oscilador de Van der Pol

d2x/dt2 - mu(1-x**2)dx/dt + x = 0

"""
# vec = [x, y]
mu = .1

#el tiempo tiene que ser explicito
def oscilador(vec, mu, t):
    A = np.array([[0, 1], [-1, mu*(1 - vec[0]**2)]])
    B = np.array([0, 0])
    return np.dot(A, vec) + B

y0 = [0, 1]
t = np.linspace(0, 3, 100)
plt.figure()
for mu in np.linspace(0, 1, 3):
    sol = integrate.odeint(lambda x, t: oscilador(x, mu, t), y0, t)

    plt.plot(t, sol[:, 0])


"Puedo no bloquear si quiero guardar la figura"
plt.show(block=False)


plt.show(block=True)