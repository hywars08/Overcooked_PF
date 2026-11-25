import random

class Chef:
    def __init__(self, x: int, y: int):
        # Índices donde se ubica el chef 
        self.x = x 
        self.y = y 

        # Atributos que manejan la posicion del chef, con píxeles (multiplicar por 16 (tamaño de la casilla))
        self.x_pixel = self.x * 16  
        self.y_pixel = self.y * 16

        # Atributos que controlan lo que tiene delante el chef (por defecto mira hacia debajo)
        self.x_delante = self.x
        self.y_delante = self.y + 1

        # La tupla es (banco_imagen, x_inicial, y_inicial, tamaño_horizontal, tamaño_vertical)
        # El atributo imagen va a contener distintas posicion que son las que representan cada accion 
        # imagen[0] = abajo ; imagen[1] = arriba ; imagen[2] = izquierda ; imagen[3] = derecha
        self.imagen = ((0, 0, 0, 16, 16), (0, 0, 16, 16, 16), (0, 0, 32, 16, 16), (0, 0, 48, 16, 16))
        self.guardar_movimiento = 0 # Atributo que guarda el último movimiento el chef registrado 
    
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
     
    # Método que controla el movimiento del chef
    def mover(self, direccion: str, ancho_tablero: int, alto_tablero: int):
        # Declaración de constantes 
        # TAMANO_IMAGEN = 16 
        VELOCIDAD = 1 

        # Dirección a la que se mueve
        self.direccion = direccion
        self.ancho_tablero = ancho_tablero
        self.alto_tablero = alto_tablero

        # Calculamos la posición a la que intenta ir
        if direccion == "arriba":
            self.y = max(0, self.y - VELOCIDAD)
            self.y_delante = self.y - 1 # Desplazar una casilla más adelante del chef
        elif direccion == "abajo": 
            self.y = min(alto_tablero - 1, self.y + VELOCIDAD) # Restarle 1, ya que la posicion de la matriz empieza en 0 
            self.y_delante = self.y + 1 # Desplazar una casilla más adelante del chef
        elif direccion == "derecha":
            self.x = min(ancho_tablero - 1, self.x + VELOCIDAD) # Restarle 1, ya que la posicion de la matriz empieza en 0
            self.x_delante = self.x + 1 # Desplazar una casilla más adelante del chef
        else: # direccion == "izquierda"
            self.x = max(0, self.x - VELOCIDAD)
            self.x_delante = self.x + 1 # Desplazar una casilla más adelante del chef
        
        # Hacer el cálculo de los píxeles (imprimir los píxeles)
        self.x_pixel = self.x * 16  
        self.y_pixel = self.y * 16

        # Asignar la nueva posicion calculada y controlar que no se salga de la pantalla
        # La función máx se encarga de asegurar que el valor de la posición nunca baja de 0 (no se salga de la pantalla)
        # Comprobar si la poscion se ha salido o no de la pantalla (hay que restarle 16 porque es el tamaño del sprite) 
        # if posicion_nueva_x > ancho_tablero - TAMANO_IMAGEN:
        #     posicion_nueva_x = ancho_tablero - TAMANO_IMAGEN 
        # if posicion_nueva_y > alto_tablero - TAMANO_IMAGEN:
        #     posicion_nueva_y = alto_tablero - TAMANO_IMAGEN
        # self.x = max(0, posicion_nueva_x) 
        # self.y = max(0, posicion_nueva_y)    