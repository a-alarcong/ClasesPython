milista = ["a", "b", "c", "d", "e"]
indice  = [ 0,   1,   2,   3,   4]
indiceinv=[-5,  -4,  -3,  -2,  -1]

longitud = len(milista)

# quiero los elementos bcd
print(milista[1])
print(milista[1:4])

# quiero los elementos bd
print(milista[1:4:2])

# quiero los elementos bd
print(milista[1:longitud-1:2])
print(milista[-2:0:-2])

mistring = "unafrase"

#Valor por defecto argumento = "algo"
#Valor opcional secuencial *args
#Valor opcional diccionario **kwargs
def hablaralreves(vector = [0, 1, 2, 3], *args, **kwargs):
    for elem in reversed(vector):
        print(type(elem), elem,end="*")

hablaralreves()
hablaralreves(milista)
hablaralreves(mistring)

miLista2 = list([1, [1, 2, 3, 4], list()])
print(miLista2)
print(miLista2[1][2])

print(id(miLista2), miLista2[0])
miLista2[0] = "cambiar un valor"
print(id(miLista2), miLista2[0])