
from item import Item


class Plato(Item):
    #Representa un plato y su contenido.

    def __init__(self, x: int, y: int):
        #Crea un plato vacío en la casilla indicada.
        super().__init__(x, y)
        self.contenido = []

    def agregar_ingrediente(self, ingrediente):
        #Añade un ingrediente al plato.
        self.contenido.append(ingrediente)

    def vaciar(self):
        #Devuelve la comida que llevaba el plato y lo deja vacío.
        contenido = self.contenido
        self.contenido = []
        return contenido

    def comprobar_esta_vacio(self):
        #Indica si el plato está vacío.
        return len(self.contenido) == 0

    def cargar(self, comida: list):
        #Añade al plato todos los elementos de la lista.
        self.contenido.extend(comida)

    def traspasar_a(self, otro_plato: "Plato"):
        #Vuelca el contenido de este plato en otro.
        if otro_plato is not self:
            otro_plato.cargar(self.vaciar())


    
