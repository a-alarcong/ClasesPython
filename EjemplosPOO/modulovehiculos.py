class Coche:
    color = ""        #NO ES NECESARIO PONER LOS ATRIBUTOS AQUÍ
    modelo = ""
    ruedas = 0
    velocidades = 0


    def __init__(self, col, mod, rued, vel):
        self.color = col
        self.modelo = mod
        self.ruedas = rued
        self.velocidades = vel


    def mostrardatos(self):
       print("Color: ", self.color)
       print("Modelo: ", self.modelo)
       print("Ruedas: ", self.ruedas)
       print("Velocidades: ", self.velocidades)


class Moto:
    color = ""
    modelo = ""
    ruedas = 0
    velocidades = 0


    def __init__(self, col, mod, rued, vel):
        self.color = col
        self.modelo = mod
        self.ruedas = rued
        self.velocidades = vel


    def mostrardatos(self):
       print("Color: ", self.color)
       print("Modelo: ", self.modelo)
       print("Ruedas: ", self.ruedas)
       print("Velocidades: ", self.velocidades)


class Camion:
    color = ""
    modelo = ""
    ruedas = 0
    velocidades = 0


    def __init__(self, col, mod, rued, vel):
        self.color = col
        self.modelo = mod
        self.ruedas = rued
        self.velocidades = vel


    def mostrardatos(self):
       print("Color: ", self.color)
       print("Modelo: ", self.modelo)
       print("Ruedas: ", self.ruedas)
       print("Velocidades: ", self.velocidades)