from chef import Chef
from plato import Plato


class Factory:
    # def crear_tomate(self):
    #     self.Chef.objeto = 

    def crear_plato(self):
        return Plato(self.Chef.x, self.Chef.y)
        
        