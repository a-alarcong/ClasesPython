i = 1
print(id(i), i)
i = i +1
print(id(i), i)
for _ in range(0,3):
    i *= 2
    #i = i * 2
    print(id(i), i)