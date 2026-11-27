import pyxel 
from plato import Plato 

class Chef:
    def __init__(self, x: int, y: int, jugador: str):
        # Índices donde se ubica el chef 
        self.x = x 
        self.y = y 

        # Diferenciar los controles en función del jugador que sea.
        self.jugador = jugador

        if self.jugador == "jugador1":
            self.controles = {
                "arriba": pyxel.KEY_W,
                "abajo": pyxel.KEY_S,
                "izquierda": pyxel.KEY_A,
                "derecha": pyxel.KEY_D,
                "interactuar": pyxel.KEY_SPACE
            }
            self.sprite_x = 0
        else: # jugador == 2:
            self.controles = {
                "arriba": pyxel.KEY_UP,
                "abajo": pyxel.KEY_DOWN,
                "izquierda": pyxel.KEY_LEFT,
                "derecha": pyxel.KEY_RIGHT,
                "interactuar": pyxel.KEY_RSHIFT
            }
            self.sprite_x = 16

        # Atributo que controla que objeto lleva
        self.objeto = "ninguno"

        # Dirección del chef
        self.direccion = "abajo" # Por defecto mira hacia abajo el chef

        # Imagen por defecto del chef
        self.imagen = (0, 0, 0, 16, 16)

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    @property
    def jugador(self) -> int:
        return self.__jugador
    
    @property
    def imagen(self) -> tuple:
        return self.__imagen

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

    @jugador.setter
    def jugador(self, jugador: str):
        if not isinstance(jugador, str):
            raise TypeError("El jugador debe ser un string")
        elif jugador != "jugador1" and jugador != "jugador2":
            raise ValueError("El jugador debe ser 1 o 2")
        else:
            self.__jugador = jugador

    # Método que controla el movimiento del chef
    def mover(self, ancho_tablero: int, alto_tablero: int):
        # Declaración de constantes 
        VELOCIDAD = 1 

        # Ancho del tablero
        self.ancho_tablero = ancho_tablero
        self.alto_tablero = alto_tablero

        # Calculamos la posición a la que intenta ir
        if self.direccion == "arriba":
            self.y = max(0, self.y - VELOCIDAD)

        elif self.direccion == "abajo": 
            self.y = min(alto_tablero - 1, self.y + VELOCIDAD) # Restarle 1, ya que la posicion de la matriz empieza en 0 
        
        elif self.direccion == "derecha":
            self.x = min(ancho_tablero - 1, self.x + VELOCIDAD) # Restarle 1, ya que la posicion de la matriz empieza en 0
        else:
            self.x = max(0, self.x - VELOCIDAD)

    # Método que modifica la dirección que esta mirando el chef
    def direccion_chef(self):
        if pyxel.btn(self.controles["izquierda"]): 
            self.direccion = "izquierda"
        if pyxel.btn(self.controles["derecha"]): 
            self.direccion = "derecha"
        if pyxel.btn(self.controles["arriba"]):
            self.direccion = "arriba"
        if pyxel.btn(self.controles["abajo"]): 
            self.direccion = "abajo"

    # Método que en función de la acción que este haciendo el chef, devuelve el sprite
    def dibujar_chef(self, casilla_pyxeles: int):
        # Calculamos la posición a la que intenta ir
        if self.direccion == "arriba":
            self.imagen = (0, 0, 16, 16, 16)
        elif self.direccion == "abajo": 
            self.imagen = (0, 0, 0, 16, 16)
        elif self.direccion == "derecha":
            self.imagen = (0, 0, 48, 16, 16)
        else: # izquierda
            self.imagen = (0, 0, 32, 16, 16)

        if isinstance(self.objeto, Plato):
            banco, x, y, ancho, alto = self.imagen
            self.imagen = (banco, x, y + 64, ancho, alto)
        pyxel.blt(self.x * casilla_pyxeles, 32 + self.y * casilla_pyxeles, *self.imagen, 0) # Sumar 32 píxeles superiores (hueco para el HUD)
    
    def tiene_objeto(self):
        if self.objeto != "ninguno":
            tiene_objeto = True
        else:
            tiene_objeto = False

        return tiene_objeto

    def que_objeto(self):
        return self.objeto


    def interactuar(self, casilla_delante: int):
        # Comprobar si tiene o no objeto
        
        if not self.tiene_objeto():
            if casilla_delante == 3: # Caja de cebolla
                print("cebolla")
            elif casilla_delante == 4: # Caja de Huevos
                print("huevo")
            elif casilla_delante == 5: # Caja de Chorizo
                print("chorizo")
            elif casilla_delante == 6: # Caja de Tomates
                print("tomate")
            elif casilla_delante == 7: # Caja de Patatas
                print("patata")
            elif casilla_delante == 8: # Platos
                print("plato")
        else:
            if casilla_delante == 1: # Encimera
                print("encimera")
                    
            

            