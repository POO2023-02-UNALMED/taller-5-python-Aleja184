from zooAnimales.animal import Animal

class Zoologico:
    def __init__(self,nombre,ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = None

    def getNombre(self):
        return self._nombre
    
    def setNombre(self,nombre):
        self._nombre = nombre

    def getUbicacion(self):
        return self._ubicacion
    
    def setUbicacion(self,ubicacion):
        self._ubicacion = ubicacion

    def getZonas(self):
        return self._zonas
    
    def setZonas(self,zonas):
        self._zonas = zonas

    def agregarZonas(self,zona):
        if self._zonas ==None:
            self._zonas = []
            self._zonas.append(zona)
        else:
            self._zonas.append(zona)
    
    def cantidadTotalAnimal():
        Animal.getTotalAnimales
        