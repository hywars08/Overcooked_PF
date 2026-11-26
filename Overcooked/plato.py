import pyxel
from item import Item

class Plato(Item):

    def __init__(self):
        super().__init__()
        self.vacio = True # Plato esta vacio inicialmente

    def dibujar(self, en_mano: bool, direccion: str):
        if en_mano == True:
            if direccion == "abajo":
                imagen = (0, 0, 64, 16, 16)
                pyxel.blt(self.x, self.y, *imagen)


    
