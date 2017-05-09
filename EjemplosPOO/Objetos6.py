# HERENCIA DE CLASES
class Padre:
    def __init__(self, pel, oj, nar):
        self.pelo = pel
        self.ojos = oj
        self.nariz = nar

    def mostrardatos(self):
        print("Datos superclase1")
        print("Pelo: ", self.pelo)
        print("Ojos: ", self.ojos)
        print("Nariz: ", self.nariz)


class Madre:
    def __init__(self, pel, oj, nar):
        self.pelo = pel
        self.ojos = oj
        self.nariz = nar

    def mostrardatos(self):
        print("Datos superclase2")
        print("Pelo: ", self.pelo)
        print("Ojos: ", self.ojos)
        print("Nariz: ", self.nariz)


# SINTAXIS HERENCIA
class Hijo(Padre, Madre):
    pass


pedro = Padre("Rubio", "Azules", "Alargada")
pedro.mostrardatos()
sara = Madre("Castaño", "Verdes", "Achatada")
sara.mostrardatos()
jose = Hijo()
jose.mostrardatos()



# INDICES        0  1  2  3
listacompra = [15, 50, 10, 65]
print(listacompra[0])
