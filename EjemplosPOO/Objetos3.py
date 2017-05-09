import time

class Vehiculo:
    def mostrardatos(self):
       print("Color: ", self.color)
       print("Modelo: ", self.modelo)
       print("Ruedas: ", self.ruedas)
       print("Velocidades: ", self.velocidades)


    def arrancar(self):
        print ("El vehiculo ha arrancado")


    def apagar(self):
        print ("El vehiculo se ha apagado")


    def acelerar(self, velocidad):
        print("El vehiculo ha empezado a acelerar")
        for i in range (0,velocidad,2):
            print ("Velocidad del vehiculo: ", i, " km/h")
            time.sleep(0.5) #Tiempo entre cada iteración
        print ("El vehiculo ha alcanzado una velocidad de ", velocidad, " km/h")


    def frenar(self, velocidad, velfrenada):
        print("El vehiculo ha empezado a frenar")
        for i in range (velocidad,velfrenada,-2):
            print("Velocidad del vehiculo: ", i, " km/h")
            time.sleep(0.2)
        print ("El vehiculo ha frenado hasta alcanzar una velocidad de ", velfrenada, " km/h")


coche = Vehiculo()
coche.color = "Azul"
coche.modelo = "Audi"
coche.ruedas = 4
coche.velocidades = 9
coche.mostrardatos()
coche.arrancar()
coche.acelerar(40)
coche.frenar(40,10)
coche.apagar()