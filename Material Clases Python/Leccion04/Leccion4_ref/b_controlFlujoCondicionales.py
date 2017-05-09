
"""
https://docs.python.org/2/tutorial/controlflow.html

"""


verdadero = False
minumero = 0
def adivinaNumero(numero):
    if verdadero:
        print("es verdad")
    elif minumero==5:
        print("mi numero es 5")
    elif minumero>=5:
        print("mi numero >= 5")
    elif minumero<5:
        print("mi numero < 5")
    elif minumero!=5:
        print("mi numero distinto 5")
    else:
        print("todo lo anterior es falso")


adivinaNumero("texto")
"Que ha pasado?"


"""
https://docs.python.org/3.6/library/stdtypes.html

Operaciones booleanas

    x or y 	if x is false, then y, else x 	(1)
    x and y 	if x is false, then x, else y 	(2)
    not x 	if x is false, then True, else False 	(3)

Comparisons
    < 	strictly less than
    <= 	less than or equal
    > 	strictly greater than
    >= 	greater than or equal
    == 	equal
    != 	not equal
    is 	object identity
    is not 	negated object identity

"""
