"""
Creacion de un modulo basico para ilustrar el solape del namespace
"""

def sqrt(x):
    """
    Calculo sencillo que hemos llamado sqrt para que solape con la raiz de otro modulo
    :param x:
    :return x**2:
    """
    return x**2

print("todo lo que este fuera del bloque se va a declarar o ejecutar al importar")
if __name__ == "__main__":
    """
    Este bloque condicional, compara el valor "built-in" del modulo __name__ para saber
    si se ha invocado directamente o se ha importado
    """
    print(sqrt(5))