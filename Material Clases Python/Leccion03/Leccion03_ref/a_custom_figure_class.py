"""
You can pass a custom Figure constructor to figure if you want to derive from the default Figure.
  This simple example creates a figure with a figure title
"""
from matplotlib.pyplot import figure, show
from matplotlib.figure import Figure


class Punto(object):
    def __init__(self, x, y):
        """
        Inicializador de la clase punto
        :param x: Coordenada x
        :param y: Coordenada y
        """
        self.x = x
        self.y = y

    def distancia(self, otro):
        """
        Definicion de la distancia entre dos puntos
        :param otro:
        :return:
        """
        x_delta = self.x - otro.x
        y_delta = self.y - otro.y
        return math.sqrt(x_delta ** 2 + y_delta ** 2)


class RepresentadorPuntos(Figure):
    def __init__(self, punto):
        """
        Clase propia para representar instancias de la clase punto
        """
        self.fig_init()
        self.pointPlotter(punto)

    def fig_init(self):
        self.fig = figure()
        self.ax = self.fig.add_subplot(111)
        show(block=False)

    def pointPlotter(self, punto):
        self.ax.plot(punto.x, punto.y, 'o', color='black')




pt1 = Punto(0, 1)
fig1 = RepresentadorPuntos(pt1)

pt2 = Punto(1, 2)
fig2 = RepresentadorPuntos(pt2)


"""
Esta linea es necesara para que se represente la grafica
"""
show()