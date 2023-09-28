from zooAnimales.animal import Animal

class Zoologico:
    _zonas = []
    def __init__(self,nombre,ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion

    def getNombre(self):
        return self._nombre
    
    def setNombre(self,nombre):
        self._nombre = nombre

    def getUbicacion(self):
        return self._ubicacion
    
    def setUbicacion(self,ubicacion):
        self._ubicacion = ubicacion

    classmethod
    def getZonas(cls):
        return cls._zonas


    def agregarZonas(self,zona):
        if self._zonas ==None:
            self._zonas = []
            self._zonas.append(zona)
        else:
            self._zonas.append(zona)
    
    def cantidadTotalAnimales():
        return Animal.getTotalAnimales()
        