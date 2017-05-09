import numpy as np
import matplotlib.pyplot as plt


class RepresentadorPuntos(object):
    def __init__(self, punto):
        self.fig_init()
        self.pointPlotter(punto)

    def fig_init(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)

    def pointPlotter(self, punto):
        self.ax.plot(punto.x, punto.y, "x")

class Punto(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


pt1 = Punto(1, 2)
pt2 = Punto(2, 3)
miRepresentacion = RepresentadorPuntos(pt1)
miRepresentacion = RepresentadorPuntos(pt2)


plt.show()