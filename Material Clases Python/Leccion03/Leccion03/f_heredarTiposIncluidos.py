class listaHabladora(list):
    def append(self, p_object):
        print("Estoy añadiento", str(p_object))
        super(listaHabladora, self).append(p_object)

l1 = listaHabladora([1,2,3])
l1.append("algo")
print(l1)

class miEntero(int):
    def __add__(self, other):
        return 42


i1 = miEntero(0)
print(i1 + i1)
print(i1 + 1)
print(1 + i1)

print(3*"a")