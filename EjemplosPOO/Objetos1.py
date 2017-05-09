#Definir clase; Sintaxis
#class nombreclase: acciones
class Vehiculo:
    pass
#pass se pone para que no de error(vacio)


#Crear objetos; Sintaxis
#variable = nombreclase()
coche = Vehiculo()


"""Asignar atributos; Sintaxis
nombreobjeto.nombreatributo = valor"""
coche.color = "Azul"
coche.modelo = "Audi"
coche.ruedas = 4
coche.velocidades = 9

print("Color: ", coche.color)
print("Modelo: ", coche.modelo)
print("Ruedas: ", coche.ruedas)
print("Velocidades: ", coche.velocidades)