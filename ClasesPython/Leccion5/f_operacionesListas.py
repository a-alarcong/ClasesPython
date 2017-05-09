milista = list(range(0, 11))
milista.extend(milista)
print(milista)

numerospares = list()
numerospares2 = ["",]*7
numerospares2 = [1,]*7
numerospares2 = [[],]*7

print()
print(type(numerospares2), numerospares2)
for elem in milista:
    if elem % 2 == 0:
        numerospares.append(elem)

print(numerospares)

n_par1 = [elem for elem in milista if (elem %2 == 0)]
n_par2 = (elem for elem in milista if (elem %2 == 0))
n_par3 = {elem for elem in milista if (elem %2 == 0)}

print()
print(type(n_par1), n_par1)
print(type(n_par2), n_par2)
print(type(n_par3), n_par3)

print()
for elem1, elem2, elem3, in zip(n_par1, n_par2, n_par3):
    print(elem1, elem2, elem3)