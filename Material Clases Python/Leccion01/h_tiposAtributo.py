__author__ = 'BLENDER'


class CajaFuerte():
    def __init__(self,secreto, PIN):
        self.secreto = secreto

        self._secreto = self.secreto

        self.__PIN = PIN


micajafuerte = CajaFuerte("le gusta mas FORTRAN", "0000")

print(micajafuerte._secreto)

micajafuerte.secreto = "ademas en Notepad"
print(micajafuerte._secreto)

micajafuerte._CajaFuerte__PIN = "1111"
print(micajafuerte._CajaFuerte__PIN)