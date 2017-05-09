__author__ = 'BLENDER'
#Como generar documentacion
class Persona():
    """
    Plantilla de la clase Persona

    instancia = Persona(nombre)

    """
    def __init__(self, nombre):
        self.nombre = nombre #asignacion del nombre al atributo nombre
        a = 1

    def saludo(self):
        """
        funcion que hace saludar a la persona
        :return:
        """
        print("hola soy una Persona")

Jessica = Persona("Jessica")
print(Jessica.__doc__)
print(Jessica.saludo.__doc__)