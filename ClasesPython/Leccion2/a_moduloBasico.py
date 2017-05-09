"""
Vamos a romper una funcion
"""

def sqrt(x):
    """
    No me he dado cuenta, y defino la raiz como el cubo
    :param x:
    :return:
    """
    return x**3

print("ejecutado desde el modulo:", sqrt(3))

if __name__ == "__main__":
    a = 4
    print(sqrt(4))