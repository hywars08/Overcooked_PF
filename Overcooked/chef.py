import pyxel 

class Chef:
    def __init__(self, x: int, y: int):
        # Índices donde se ubica el chef 
        self.x = x 
        self.y = y 

        # Dirección del chef
        self.direccion = "abajo" # dirección por defecto

        # Imagen por defecto del chef
        self.imagen = (0, 0, 0, 16, 16)

        # Variables que controlan la casilla delante de donde mira el chef (por defecto mira hacia abajo)
        self.x_delante_chef = self.x + 1
        self.y_delante_chef = self.y

        # La tupla es (banco_imagen, x_inicial, y_inicial, tamaño_horizontal, tamaño_vertical)
        # El atributo imagen va a contener distintas posicion que son las que representan cada accion 
        # imagen[0] = abajo ; imagen[1] = arriba ; imagen[2] = izquierda ; imagen[3] = derecha
        
    
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
            raise TypeError("La imagen debe ser una tupla")
        elif len(imagen) != 5:
            raise ValueError("La imagen debe ser una tupla con 5 elementos")
        self.__imagen = imagen
     
    # Método que controla el movimiento del chef
    def mover(self, direccion: str, ancho_tablero: int, alto_tablero: int):
        # Declaración de constantes 
        # TAMANO_IMAGEN = 16 
        VELOCIDAD = 1 

        # ANcho del tablero
        self.direccion = direccion
        self.ancho_tablero = ancho_tablero
        self.alto_tablero = alto_tablero

        # Calculamos la posición a la que intenta ir
        if direccion == "arriba":
            self.y = max(0, self.y - VELOCIDAD)

        elif direccion == "abajo": 
            self.y = min(alto_tablero - 1, self.y + VELOCIDAD) # Restarle 1, ya que la posicion de la matriz empieza en 0 
         
        elif direccion == "derecha":
            self.x = min(ancho_tablero - 1, self.x + VELOCIDAD) # Restarle 1, ya que la posicion de la matriz empieza en 0

        else: # self.direccion == "izquierda":
            self.x = max(0, self.x - VELOCIDAD)

    # Método que devuelve la dirección que esta mirando el chef
    def accion_chef(self):
        accion = "ninguna"
        if pyxel.btn(pyxel.KEY_A): 
            accion = "izquierda"
        if pyxel.btn(pyxel.KEY_D): 
            accion = "derecha"
        if pyxel.btn(pyxel.KEY_W):
            accion = "arriba"
        if pyxel.btn(pyxel.KEY_S): 
            accion = "abajo"
         
            
            
        return accion
    # Método que en función de la acción que este haciendo el chef, devuelve el sprite
    def dibujar_chef(self, accion: str, casilla_pyxeles: int):
        # Calculamos la posición a la que intenta ir
        if accion == "arriba":
            self.imagen = (0, 0, 16, 16, 16)
        elif accion == "abajo": 
            self.imagen = (0, 0, 0, 16, 16)
        elif accion == "derecha":
            self.imagen = (0, 0, 48, 16, 16)
        elif accion == "izquierda":
            self.imagen = (0, 0, 32, 16, 16)
        else:
            self.imagen = self.imagen
        return pyxel.blt(self.x * casilla_pyxeles, self.y * casilla_pyxeles, *self.imagen, 0)

