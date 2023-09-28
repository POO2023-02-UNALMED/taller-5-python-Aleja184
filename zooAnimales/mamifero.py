from .animal import Animal

class Mamifero(Animal):
    _listado = []
    caballos = 0
    leones = 0

    def __init__(self, nombre, edad, habitat, genero,pelaje,patas):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas

    def getColorPelaje(self):
        return self._pelaje
    
    def setColorPelaje(self,pelaje):
        self._pelaje = pelaje
    
    def getColorPatas(self):
        return self._patas
    
    def setColorPatas(self,patas):
        self._patas = patas

    classmethod
    def getListado(cls):
        return cls._listado

    classmethod
    def cantidadMamiferos(cls):
        return len(cls._listado)
    
    def crearCaballo(nombre,edad,genero):
        caballo = Mamifero(nombre,edad,"pradera",genero,True,4)
        Mamifero.caballos+=1
        return caballo

    def crearLeon(nombre,edad,genero):
        leon = Mamifero(nombre,edad,"selva",genero,True,4)
        Mamifero.leones+=1
        return leon