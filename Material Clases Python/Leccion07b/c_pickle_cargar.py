import pickle

"""
w:write
r:leer
a:
"""
with open('filename','rb') as f:
    var2 = pickle.load(f)

print(var2)