import random

incognita = random.randint(1,10)

usuario = input("introduce un valor\n")
print(usuario)

str(incognita)
if int(usuario) == incognita:
    print("Acertaste!!")
else:
    print("Sigue intentandolo")

print(type(incognita),type(usuario))