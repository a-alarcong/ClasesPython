
class ListaHabladora(list):
    def append(self, p_object):
        print("He añadido", p_object)


class MiEntero(int):
    def __add__(self, other):
         return 42

foo = ListaHabladora("hola")
foo.append("asd")


int1 = MiEntero(0)
print(int1)

print(int1+int1)