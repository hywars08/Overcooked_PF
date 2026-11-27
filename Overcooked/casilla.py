# Clase que controla las casillas del mapa
import pyxel

class Casilla:
    TAMANO = 16
    def __init__(self, fila: int, col: int, tipo: int, tipo_casilla: int):
        self.fila = fila
        self.col = col
        # Coordenadas exactas en píxeles (sumando los 32 px del tablero de comandas)
        self.x = col * self.TAMANO
        self.y = fila * self.TAMANO
        self.tipo = tipo
        self.tipo_casilla = tipo_casilla    
        # Aquí se guardará el ingrediente o plato apoyado sobre esta mesa 
        self.objeto_encima = False

    def dibujar(self):
        # Dibuja la casilla
        pyxel.blt(self.x, self.y + 32, *self.imagen_casilla())
        
        
    # Metodo que devuelve que imagen corresponde a la casilla en función del tipo de casilla
    def imagen_casilla(self):
        if self.tipo_casilla == 0: # Suelo normal
            imagen = (1, 0, 0, self.TAMANO, self.TAMANO)
        elif self.tipo_casilla == 1: # Encimera
            imagen = (1, 0, 16, self.TAMANO, self.TAMANO)
        elif self.tipo_casilla == 2: # Muro
            imagen = (1, 0, 32, self.TAMANO, self.TAMANO)
        elif self.tipo_casilla == 3: # Caja Cebolla
            imagen = (1, 16, 0, self.TAMANO, self.TAMANO)
        elif self.tipo_casilla == 4: # Caja Huevo
            imagen = (1, 16, 16, self.TAMANO, self.TAMANO)
        elif self.tipo_casilla == 5: # Caja Chorizo
            imagen = (1, 16, 32, self.TAMANO, self.TAMANO)
        elif self.tipo_casilla == 6: # Caja Tomate
            imagen = (1, 16, 48, self.TAMANO, self.TAMANO)
        elif self.tipo_casilla == 7: # Caja Patata
            imagen = (1, 16, 64, self.TAMANO, self.TAMANO)
        elif self.tipo_casilla == 8: # Platos
            imagen = (1, 16, 80, self.TAMANO, self.TAMANO)
        elif self.tipo_casilla == 9: 
            imagen = (1, 0, 92, self.TAMANO, self.TAMANO)
        return imagen
