import math

class Punto(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distancia(self, otro):
        return math.sqrt((self.x - otro.x)**2 + (self.y - otro.y)**2)



if __name__ == "__main__":
    c1 = Punto(1,2)
    c2 = Punto(3,5)
    print("x: %s; y: %s" %(c1.x, c1.y))
    print(c1.distancia(c2))
    print(c1.distancia(c2) == c2.distancia(c1))