# Importando la librería pyxel
import pyxel
# Importando la clase Chef para poder usarla en la clase Tablero
from chef import Chef
from casilla import Casilla

class Tablero:
    def __init__(self, ancho: int, alto: int):
        # Declaración de constantes
        TAMANO_CASILLA = 16 # SOn 16 píxeles

        # Estableciendo los atributos
        self.ancho = ancho # Ancho del tablero
        self.alto = alto # Alto del tablero

        # El mapa va a ser una matriz, y en función del número que tenga las casillas sera un "objeto" u otro
        # Diccionario que guarde que significa cada número de la matriz -> (tupla_sprite, es_transitable) # 
        TIPO_CELDAS = {
            0: ((0, 32, 16, 16, 16), True),    # Suelo (se puede caminar)
            1: ((0, 32, 0, 16, 16), False),
            # TODO
        }
        self.mapa = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # Fila 0
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Fila 1
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Fila 2
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Fila 3
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # Fila 4
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Fila 5
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Fila 6
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Fila 7
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]   # Fila 8
        ]
        # Transformamos la matriz de números en una matriz de objetos Casilla
        self.casillas = []
        for i in range(len(self.mapa)):
            fila_objetos = []
            for j in range(len(self.mapa[i])):
                sprite = TIPO_CELDAS[self.mapa[i][j]][0] # Pillar la tupla del sprite en funcion de la casilla que se encuentre en la matriz
                es_transitable = TIPO_CELDAS[self.mapa[i][j]][1] # Pillar si se va a poder caminar o no
                nueva_casilla = Casilla(i, j, self.mapa[i][j], sprite, es_transitable) 
                fila_objetos.append(nueva_casilla)
            self.casillas.append(fila_objetos)

        self.chef = Chef(1, 4) # Posición inicial del chef, por defecto mira hacia abajo

        # En este init también necesitamos inicializar pyxel
        # Esta instrucción se usa para inicializar pyxel, consulta la API para
        # ver más parámetros
        pyxel.init(self.ancho * TAMANO_CASILLA, self.alto * TAMANO_CASILLA, title="Overcooked en pyxel",display_scale=4, fps= 8)

        # Cargando el archivo pyxres con las imágenes
        pyxel.load("assets/my_resource.pyxres")

        # Ejecutando el juego, esto llamará a los métodos actualizar y dibujar en
        # cada fotograma, consulta la API para más información
        pyxel.run(self.actualizar, self.dibujar)

    # Propiedades y setters
    @property
    def ancho(self) -> int:
        return self.__ancho

    @property
    def alto(self) -> int:
        return self.__alto

    @ancho.setter
    def ancho(self, ancho: int):
        if not isinstance(ancho, int):
            raise TypeError("El ancho debe ser un número entero")
        elif ancho < 1:
            raise ValueError("El ancho debe ser un número entero positivo")
        else:
            self.__ancho = ancho

    @alto.setter
    def alto(self, alto: int):
        if not isinstance(alto, int):
            raise TypeError("El alto debe ser un número entero")
        elif alto < 1:
            raise ValueError("El alto debe ser un número entero positivo")
        else:
            self.__alto = alto

    def actualizar(self):
        """Este es el método de pyxel que se ejecuta en cada iteración del
        juego (cada fotograma). Aquí debes poner todo el código que tenga que
        ejecutarse en cada fotograma. Ahora solo contiene la lógica para salir
        del programa si se pulsa una tecla."""
        # Para salir del juego
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()

        # Movimiento del chef
        

        if pyxel.btn(pyxel.KEY_A): 
            self.chef.mover("izquierda", self.ancho, self.alto)
        if pyxel.btn(pyxel.KEY_D): # Velocidad positiva porque se mueve hacia la derecha en las x
            self.chef.mover("derecha", self.ancho, self.alto)
        if pyxel.btn(pyxel.KEY_W): # Velocidad negativa porque se mueve hacia arriba en las y (este eje va al reves)
            self.chef.mover("arriba", self.ancho, self.alto)
        if pyxel.btn(pyxel.KEY_S): # Velocidad positiva porque se mueve hacia abajo en las y (este eje va al reves)
            self.chef.mover("abajo", self.ancho, self.alto)

    def dibujar(self):
        """Este es el método de pyxel que se ejecuta en cada iteración del
        juego (cada fotograma). Aquí debes poner todo el código para dibujar
        los sprites del juego.
        """
        # Borrando la pantalla anterior
        pyxel.cls(0)
        # Bucle que recorre la matriz del mapa y lo pinta en funcion de la casilla que encuentre
        for fila in self.casillas:
            for casilla in fila:
                casilla.dibujar()

        # Dibujando al chef. Los parámetros de pyxel.blt son (x, y, tupla_sprite)
        # El * se usa para desempaquetar la tupla del sprite
        # En función de que tecla estes pulsando se muestra un sprite u otro
        if pyxel.btn(pyxel.KEY_A):
            pyxel.blt(self.chef.x_pixel, self.chef.y_pixel, *self.chef.imagen[2], 8) # Ponemos un , 0) al final del pyxel.blt para que tenga fondo trasnparente
            self.chef.guardar_movimiento = 2
        elif pyxel.btn(pyxel.KEY_D):
            pyxel.blt(self.chef.x_pixel, self.chef.y_pixel, *self.chef.imagen[3], 8) # Ponemos un , 0) al final del pyxel.blt para que tenga fondo trasnparente
            self.chef.guardar_movimiento = 3
        elif pyxel.btn(pyxel.KEY_W):
            pyxel.blt(self.chef.x_pixel, self.chef.y_pixel, *self.chef.imagen[1], 8) # Ponemos un , 0) al final del pyxel.blt para que tenga fondo trasnparente
            self.chef.guardar_movimiento = 1
        elif pyxel.btn(pyxel.KEY_S):  
            pyxel.blt(self.chef.x_pixel, self.chef.y_pixel, *self.chef.imagen[0], 8) # Ponemos un , 0) al final del pyxel.blt para que tenga fondo trasnparente
            self.chef.guardar_movimiento = 0
        else:
            pyxel.blt(self.chef.x_pixel, self.chef.y_pixel, *self.chef.imagen[self.chef.guardar_movimiento], 8) # Ponemos un , 0) al final del pyxel.blt para que tenga fondo trasnparente

        
        # Un texto para mostrar la posición del chef, los parámetros de
        # pyxel.text son (x, y, texto, color)
        pyxel.text(10, 10, f"({self.chef.x}, {self.chef.y})", 7)