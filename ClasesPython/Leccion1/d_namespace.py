def misaludo():
    print("Hola")

class Persona():

    def __init__(self, nombre):
        self.nombre = nombre #asignacion del nombre al atributo nombre

    def saludo(self):

        print("hola soy una Persona")
        return "Greetings"


Juan = Persona("Juan")

print(Juan.saludo())
print(Juan.saludo)
print(id(Juan.saludo))

print("Juan:")
print(Juan)
print(id(Juan))

Alberto = Juan
print("Alberto:")
print(Alberto)
print(id(Alberto))

Alberto.nombre = "Alberto"
print("Juan: Soy " + Juan.nombre)