"""
https://github.com/AeroPython/Curso_AeroPython/blob/master/notebooks_completos/040-SymPy-Intro.ipynb

https://github.com/AeroPython/Curso_AeroPython/blob/master/notebooks_completos/040-SymPy-Mecanica.ipynb
"""
from sympy import *
import sympy

init_printing()
# init_session()

x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)

print(2*x)

print(sympy.Integral(sqrt(1/x), x))
print(latex(Integral(sqrt(1/x), x)))
print(pretty(Integral(sqrt(1/x), x), use_unicode=False))

print(latex(integrate(sqrt(1/x), x)))


expr = cos(x)**2 + sin(x)**2
print(expr)







print(simplify(expr))

print(expr.subs(cos(x), y))

"""

"""