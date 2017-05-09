import shelve

s = shelve.open('fileshelve.db')
try:
    var = {'int': 10, 'float': 9.5, 'string': 'Sample data' }
    s['key1'] = var
    s['key2'] = 'un string'
finally:
    s.close()