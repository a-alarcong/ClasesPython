"""
https://docs.python.org/2/library/json.html

https://docs.python.org/3/library/json.html

https://pythontips.com/2013/08/08/storing-and-loading-data-with-json/

http://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file-in-python
"""

import json

with open('filenameJson', 'w') as f:
    var = {1: 'a', 2: 'b'}
    json.dump(var, f)


