"""
You can pass a custom Figure constructor to figure if you want to derive from the default Figure.
  This simple example creates a figure with a figure title
"""
from matplotlib.pyplot import figure, show
from matplotlib.figure import Figure


class MyFigure(Figure):
    def __init__(self, *args, **kwargs):
        """
        custom kwarg figtitle is a figure title
        """
        figtitle = kwargs.pop('figtitle', 'hi mom')
        Figure.__init__(self, *args, **kwargs)
        self.text(0.5, 0.95, figtitle, ha='center')

fig = figure(FigureClass=MyFigure, figtitle='my title')
ax = fig.add_subplot(111)
ax.plot([1, 2, 3], [2, 2, 3])


class RepresentadorPuntos(Figure):
    def __init__(self, listaPuntos):
        """
        custom kwarg figtitle is a figure title
        """
        self.fig = figure()
        self.ax = self.fig.add_subplot(111)
        self.ax.plot(pt1.x, pt1.y, 'o', color='black')


from Leccion3_ref.c_DeclaracionPunto import Punto

pt1 = Punto(0, 1)
fig2 = RepresentadorPuntos(pt1)

show()