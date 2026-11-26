# Clase que controla las casillas del mapa
import pyxel

class Casilla:
    TAMANO = 16
    CAJA_OBJETOS = [2, 3, 4 , 5, 6, 7]
    IMAGENES_OBJETOS = {
        2: (0, 16, 0, 16, 16), # Tomate
        3: (0, 16, 16, 16, 16), # Patata 
        4: (0, 16, 32, 16, 16), # Huevo
        5: (0, 16, 48, 16, 16), # Cebolla
        6: (0, 16, 64, 16, 16),  # Chorizo
        7: (0, 16, 80, 16, 16)
    }
    def __init__(self, fila: int, col: int, tipo: int, sprite: tuple):
        self.fila = fila
        self.col = col
        # Coordenadas exactas en píxeles (sumando los 32 px del tablero de comandas)
        self.x = col * self.TAMANO
        self.y = fila * self.TAMANO
        self.tipo = tipo
        self.sprite = sprite    
        # Aquí se guardará el ingrediente o plato apoyado sobre esta mesa 
        self.objeto_encima = False

    def dibujar(self):
        # 1. Dibuja el suelo o la encimera base
        pyxel.blt(self.x, self.y + 32, *self.sprite)
        if self.tipo in self.CAJA_OBJETOS: # Si el tipo de la casilla esta entre las que son cajas imprimir encima el sprite correspondiente
            pyxel.blt(self.x, self.y + 32, *self.IMAGENES_OBJETOS[self.tipo], 0) # Quitar el fondo del sprite
        # 2. Si tiene un ingrediente o plato encima, lo dibuja automáticamente
        if self.objeto_encima:
            pyxel.blt(self.x, self.y + 32, *self.objeto_encima.imagen)
