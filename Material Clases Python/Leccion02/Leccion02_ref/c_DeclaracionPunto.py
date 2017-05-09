import math

class Punto(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, otro):
        x_delta = self.x - otro.x
        y_delta = self.y - otro.y
        return math.sqrt(x_delta ** 2 + y_delta ** 2)

"""
Uso de un metodo de la clase superior
"""
class Circulo(Punto):
    """
    Porque las globales de clase no son buena idea salvo ocasiones particulares
    """
    x = 0
    y = 0
    radio = 0
    def __init__(self, x, y, radio):
        super(Circulo, self).__init__(x, y)
        self.raido = radio


c1 = Punto(4, 1.5)
c2 = Punto(3, 3.1)
print(c1.distancia(c2) == Punto.distancia(c1, c2))

c3 = Circulo(1,2,3)
print(c3.radio)