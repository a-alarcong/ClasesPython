""" Ya habiamos visto la iteracion en un tipo secuencial o un iterable"""
lista = [1, 2, 'hola']
for elem in lista:
    print(elem, end=" | ")

""" si necesito iterar con un indice, me genero el iterador con range"""
print("\n")
print(type(range(3)), range(3))
for i in range(3):
    print(i, lista[i], end=" | ")
else:
    print("la sentencia else se ejecuta al agotar el bucle"
          " sin romperlo")
print("\n")


def buscarPrimos(y):
    for n in range(2, y):
        # nested loop
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n//x)

                if True:

                    print("foo")
                    break

            else:
                # loop fell through without finding a factor
                """
                else clause;
                it is executed when the loop terminates through exhaustion of the list (with for)
                or when the condition becomes false (with while),
                but not when the loop is terminated by a break statement
                """
                print(n, 'is a prime number')

buscarPrimos(5)

"""
Bucles controlados por condicional
"""
lista = list(range(10))
lista = [False, False]
while lista:
    x = lista.pop()
    print(x, end=" | ")
    #1/0
else:
    print("termino")