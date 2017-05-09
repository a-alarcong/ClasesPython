class Vehiculo:
    #Método de inicialización
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


coche = Vehiculo("Azul","Audi",4,9)
coche.mostrardatos()


moto = Vehiculo("Rojo","Honda",2,12)
moto.mostrardatos()