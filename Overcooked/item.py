import pyxel

class Item:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def dibujar_item(self, casilla_pyxeles: int, imagen: tuple):
        if imagen != "ninguna": # Solo imprima si le han pasado una imagen
            pyxel.blt(self.x * casilla_pyxeles, 32 + self.y * casilla_pyxeles, *imagen, 0) # Sumar 32 píxeles superiores (hueco para el HUD)  

      
