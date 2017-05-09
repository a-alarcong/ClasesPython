#Importamos modulo vehículos
from EjemplosPOO.modulovehiculos import Coche, Moto, Camion    #SI QUEREMOS IMPORTAR TOD O PONEMOS *

#Creación de los objetos
coche1 = Coche("Rojo","BMW",4,7)
coche1.mostrardatos()


coche2 = Coche("Negro","Toyota",4,5)
coche2.mostrardatos()


moto1 = Moto("Morado","Honda",2,10)
moto1.mostrardatos()


camion1 = Camion("Verde","Scania",8,16)
camion1.mostrardatos()