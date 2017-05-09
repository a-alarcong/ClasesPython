import shelve

s = shelve.open('test_shelf.db')
try:
    for key, value in s.items():
        print(key, value, s[key])

finally:
    s.close()
