# Clase que controla las casillas del mapa
import pyxel

class Casilla:
    TAMANO = 16

    def __init__(self, fila: int, col: int, tipo: int, sprite: tuple, transitable: bool):
        self.fila = fila
        self.col = col
        # Coordenadas exactas en píxeles (sumando los 32 px del tablero de comandas)
        self.x = col * self.TAMANO
        self.y = 32 + fila * self.TAMANO
        self.tipo = tipo
        self.sprite = sprite
        self.transitable = transitable
        # Aquí se guardará el ingrediente o plato apoyado sobre esta mesa (None si está vacía)
        self.objeto_encima = None

    def dibujar(self):
        # 1. Dibuja el suelo o la encimera base
        pyxel.blt(self.x, self.y, *self.sprite)

        # 2. Si tiene un ingrediente o plato encima, lo dibuja automáticamente
        if self.objeto_encima is not None:
            pyxel.blt(self.x, self.y, *self.objeto_encima.imagen)