import math
import Leccion3.c_DeclaracionPunto

class Circulo(Leccion3.c_DeclaracionPunto.Punto):
    def __init__(self, x, y, radio):
        super().__init__(x, y)
        self.radio = radio

    @property
    def area(self):
        self._area = math.pi*self.radio**2
        return self._area
    @area.setter
    def area(self, area):
        self.radio = math.sqrt(area/math.pi)

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, radio):
        if radio < 0:
            self._radio = 0
            print("El radio era negativo")
        else:
            self._radio = radio

c1 = Circulo(2,3,-5)
print(c1.area)

c1.radio = 3
print(c1.area)

c1.area = 0.53
print(c1.area, c1.radio)