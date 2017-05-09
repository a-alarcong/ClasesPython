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
    def __init__(self, x, y, radio):
        super(Circulo, self).__init__(x, y)
        self.radio = radio

    @property
    def area(self):
        return math.pi * self.radio ** 2

    @area.setter
    def area(self, area):
        self.radio = math.sqrt(area / math.pi)

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, radio):
        if radio < 0:
            raise ValueError("'radio' deber ser no negativo")
        self._radio = radio


c1 = Punto(4, 1.5)
c2 = Punto(3, 3.1)
print(c1.distancia(c2) == Punto.distancia(c1, c2))

c3 = Circulo(1, 2, 4)
print(c3.radio)

c3.radio = -2
print(c3.radio)