# Definimos clase y sus atributos
class Vehiculo:
# Creando metodos; Sintaxis
# def nombremetodo(self)
#         acciones
    def mostrardatos(self):
       print("Color: ", self.color)
       print("Modelo: ", self.modelo)
       print("Ruedas: ", self.ruedas)
       print("Velocidades: ", self.velocidades)


# Asignación de valores a los atributos
coche = Vehiculo()
coche.color = "Azul"
coche.modelo = "Audi"
coche.ruedas = 4
coche.velocidades = 9
coche.mostrardatos()


moto = Vehiculo()
moto.color = "Rojo"
moto.modelo = "Honda"
moto.ruedas = 2
moto.velocidades = 12
moto.mostrardatos()