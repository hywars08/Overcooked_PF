from posicion import Posicion

class Player(Posicion):
    def __init__(self, x, y, objeto: bool = False):
        super().__init__(x, y)
        self.objeto = objeto


    