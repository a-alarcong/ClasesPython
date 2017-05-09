import random
import math

n_limit = 10
number = random.randint(1, n_limit)
max_attempts = math.floor(math.log2(n_limit) + 1)

print(number, max_attempts)


def checkGame(guess):
    win = 0

    if int(guess) == number:
        print("Acertaste!!")
        win = 1
    elif int(guess) > number:
        print("Mi numero es menor que %s" %(guess,))
    elif int(guess) < number:
        print("Mi numero es mayor que %s" %(guess,))
    return win


def checkErrorType(guess):
    try:
        guess_int = int(guess)
    except:
        guess_int = -1
    finally:
        return guess_int


print("He pensado un numero entre el 1 y el %i" %(n_limit,))
for attempt in range(0, max_attempts):
    print("\nTe quedan %i intentos." %(max_attempts-attempt,))
    guess = input("Prueba un valor\n")

    while checkErrorType(guess) < 0:
        guess = input("Muy gracioso,... prueba con un entero si no quieres entrar en bucle\n")

    if checkGame(guess):
        break

else:
    print("Lo siento, has perdido")
