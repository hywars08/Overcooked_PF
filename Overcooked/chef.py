import random

class Chef:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        # El sprite inicial será siempre el mismo, así que no se necesita parámetro
        # En Pyxel la imagen es una tupla con las coordenadas de la imagen en
        # el banco de imágenes.
        # La tupla es (banco_imagen, x_inicial, y_inicial, tamaño_horizontal,
        # tamaño_vertical)
        # Sería buena idea hacer que el sprite sea de solo lectura, veremos cómo
        # hacerlo en próximas clases
        self.imagen = (0, 0, 0, 16, 16)
        valor = random.randint(0, 1)
        if valor == 1:
            self.tiene_plato = True
        else:
            self.tiene_plato = False

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    @property
    def imagen(self) -> tuple:
        return self.__imagen

    @property
    def tiene_plato(self) -> bool:
        return self.__tiene_plato

    @x.setter
    def x(self, x: int):
        if not isinstance(x, int):
            raise TypeError("La posición x debe ser un entero")
        elif x < 0:
            raise ValueError("La posición x no puede ser negativa")
        else:
            self.__x = x

    @y.setter
    def y(self, y: int):
        if not isinstance(y, int):
            raise TypeError("La posición y debe ser un entero")
        elif y < 0:
            raise ValueError("La posición y no puede ser negativa")
        else:
            self.__y = y

    @imagen.setter
    def imagen(self, imagen: tuple):
        if not isinstance(imagen, tuple):
            raise TypeError("La imagen debe ser una tupla con 5 elementos")
        elif len(imagen) != 5:
            raise ValueError("La imagen debe ser una tupla con 5 elementos")
        else:
            self.__imagen = imagen

    @tiene_plato.setter
    def tiene_plato(self, plato: bool):
        if not isinstance(plato, bool):
            raise TypeError("El atributo tiene_plato debe ser booleano")
        else:
            self.__tiene_plato = plato

    