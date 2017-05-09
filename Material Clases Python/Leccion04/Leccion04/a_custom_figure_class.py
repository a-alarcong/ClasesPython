from matplotlib import pyplot as plt
from matplotlib.pyplot import figure, show
from matplotlib.figure import Figure


class Punto(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class RepresentadorPuntos(Figure):
    def __init__(self, listaPuntos):
        """
        Clase propia para representar instancias
         de la clase Punto
        """
        self.fig_init()

        if isinstance(listaPuntos, list):
            self.plot_pointlist(listaPuntos)
        elif isinstance(listaPuntos, Punto):
            self.pointPlotter(listaPuntos)
        else:
            print("no se pintarlo")

    def fig_init(self):
        self.fig = plt.figure()
        self.ax = list(["", ""])
        self.ax[0] = self.fig.add_subplot(211)
        #self.ax.append(self.fig.add_subplot(2,2, 3))
        self.ax[1] = self.fig.add_subplot(2,3, 4)

        # Puede ser util
        # para guardar sin bloquear el hilo
        show(block=False)

    def pointPlotter(self, punto):
        self.ax[0].plot(punto.x, punto.y, 'o', color='black')

    def plot_pointlist(self, listaPuntos):
        for elemento in listaPuntos:
            self.pointPlotter(elemento)

pt1 = Punto(0,0)
pt2 = Punto(1,2)

listaPuntos = list([pt1, pt2])
listaPuntos.append(Punto(2,3))
fig1 = RepresentadorPuntos(listaPuntos)

pt3 = Punto(0,0)
fig2 = RepresentadorPuntos(pt3)

fig3 = RepresentadorPuntos("sdfasdf")

#Show es necesario en matplotlib
plt.show()