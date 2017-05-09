"""
https://daganu.wordpress.com/2011/04/09/decoradores-en-python/

http://www.3engine.net/wp/2015/09/decoradores-python-con-parametros/
"""


def decorador(funcion_a_decorar):
    def funcion_definida_dentro_del_decorador(*args, **kwargs):
        print("decorador: aqui podriamos introducir las instrucciones del decorador")
        funcion_a_decorar(args[0] + 1, args[1] + 1)
        print("seguimos en el decorador")

    return funcion_definida_dentro_del_decorador


@decorador
def a_decorar(x, y):
    print(x + y)

a_decorar(1, 2)


"""
Vamos a aplicarlo

"""
def avisar(f):
    def inner(*args, **kwargs):
        f(*args, **kwargs)
        print("Se ha ejecutado %s" % f.__name__)
    return inner


def abrir_puerta():
    print("Abrir puerta")


def cerrar_puerta():
    print("Cerrar puerta")


abrir_puerta()
cerrar_puerta()

abrir_puerta2 = avisar(abrir_puerta)
cerrar_puerta2 = avisar(cerrar_puerta)
abrir_puerta2()
cerrar_puerta2()


@avisar
def abrir_puerta3():
    print("Abrir puerta")

def cerrar_puerta3():
    print("Cerrar puerta")

abrir_puerta3()
cerrar_puerta3()