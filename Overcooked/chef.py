import random

class Chef:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        # La tupla es (banco_imagen, x_inicial, y_inicial, tamaño_horizontal, tamaño_vertical)
        # El atributo imagen va a contener distintas posicion que son las que representan cada accion 
        # imagen[0] = abajo ; imagen[1] = arriba ; imagen[2] = izquierda ; imagen[3] = derecha
        self.imagen = ((0, 0, 0, 16, 16), (0, 0, 16, 16, 16), (0, 0, 32, 16, 16), (0, 0, 48, 16, 16))
        self.guardar_movimiento = 0 # Atributo que guarda el último movimiento el chef registrado 
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
        for i in range(len(imagen)):
            if not isinstance(imagen, tuple):
                raise TypeError("La imagen debe ser una tupla con 5 elementos")
            elif len(imagen[i]) != 5:
                raise ValueError("La imagen debe ser una tupla con 5 elementos")
        self.__imagen = imagen

    @tiene_plato.setter
    def tiene_plato(self, plato: bool):
        if not isinstance(plato, bool):
            raise TypeError("El atributo tiene_plato debe ser booleano")
        else:
            self.__tiene_plato = plato
            
    # Método que controla el movimiento del chef
    def mover(self, mover_x: int, mover_y: int, ancho_tablero: int, alto_tablero: int):
        # Declaración de constantes
        TAMAÑO_IMAGEN = 16 

        # Calculamos la posición a la que intenta ir
        posicion_nueva_x = self.x + mover_x
        posicion_nueva_y = self.y + mover_y

        # Asignar la nueva posicion calculada y controlar que no se salga de la pantalla
        # La función máx se encarga de asegurar que el valor de la posición nunca baja de 0 (no se salga de la pantalla)
        # Comprobar si la poscion se ha salido o no de la pantalla (hay que restarle 16 porque es el tamaño del sprite) 
        if posicion_nueva_x > ancho_tablero - TAMAÑO_IMAGEN:
            posicion_nueva_x = ancho_tablero - TAMAÑO_IMAGEN 
        if posicion_nueva_y > alto_tablero - TAMAÑO_IMAGEN:
            posicion_nueva_y = alto_tablero - TAMAÑO_IMAGEN
        self.x = max(0, posicion_nueva_x)
        self.y = max(0, posicion_nueva_y)


    