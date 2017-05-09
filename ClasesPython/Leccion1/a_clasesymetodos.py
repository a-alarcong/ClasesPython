__author__ = 'Álvaro'

# Con el simbolo # incluyo una linea de comentario

"""
La otra opcion es generar un string
Si lo quiero en varias lineas con triple " o triple '
"""

# Voy a generar mi primera clase vacia
class MiPrimeraClase:
    pass #pass es una palabra clave para rellenar el bloque

# Voy a definir una funcion
def misaludo():
    print("Hola")

# Voy a generar mi primera clase vacia
class Persona():
    def __init__(self, nombre):
        self.nombre = nombre

    def saludo(self):
        print("hola soy una Persona")

misaludo()
Sergio = Persona("Sergio")
Sergio.saludo()


class Alumno(Persona):
    def saludo(self):
        print("Hola, soy " + self.nombre)

Daniel = Alumno("Daniel")
Daniel.saludo()

print(Alumno.__mro__)