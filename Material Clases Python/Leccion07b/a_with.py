"""

http://effbot.org/zone/python-with-statement.htm

http://stackoverflow.com/questions/3012488/what-is-the-python-with-statement-designed-for

https://www.python.org/dev/peps/pep-0343/

"""

# @contextmanager
# def opening(filename):
#     f = open(filename)
#     try:
#         yield f
#     finally:
#         f.close()
#
#
# with f = opening("n0012.dat"):
#     for line in f:
#     myList.append(line)
# print(myList)


myList = []
with open('n0012.dat', 'r') as f:
    for line in f:
        print(line)
