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

# c3.radio = -2
print(c3.radio)



def decorador(funcion_a_decorar):
    def funcion_definida_dentro_del_decorador(*args, **kwargs):
        print("decorador: aqui podriamos introducir las instrucciones del decorador")
        funcion_a_decorar(args[0] + 1, args[1] + 1)
        print("seguimos en el decorador")

    return funcion_definida_dentro_del_decorador

@decorador
def a_decorar(x, y):
    print(x + y)

a_decorar(1, 2)


"""
Vamos a aplicarlo

"""
def avisar(f):
    def inner(*args, **kwargs):
        f(*args, **kwargs)
        print("Se ha ejecutado %s" % f.__name__)
    return inner


def abrir_puerta():
    print("Abrir puerta")


def cerrar_puerta():
    print("Cerrar puerta")


abrir_puerta()
cerrar_puerta()

abrir_puerta2 = avisar(abrir_puerta)
cerrar_puerta2 = avisar(cerrar_puerta)
abrir_puerta2()
cerrar_puerta2()


@avisar
def abrir_puerta3():
    print("Abrir puerta")

def cerrar_puerta3():
    print("Cerrar puerta")

abrir_puerta3()
cerrar_puerta3()