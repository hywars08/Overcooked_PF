import pyxel
from item import Item

class Plato(Item):

    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.vacio = True # Plato esta vacio inicialmente

    def dibujar_item(self, casilla_pyxeles: int, en_mano: bool, direccion: str):
        if en_mano:
            if direccion == "abajo":
                self.imagen = (0, 0, 64, 16, 16)
            elif direccion == "derecha":
                self.imagen = (0, 0, 96, 16, 16)
            elif direccion == "izquierda":
                self.imagen = (0, 0, 80, 16, 16)
            elif direccion == "arriba":
                self.imagen = "ninguna"
        else:
            # Coordenadas (u, v) del plato completo cuando está apoyado en una encimera
            self.imagen = "ninguna"

        super().dibujar_item(casilla_pyxeles, self.imagen)


    
