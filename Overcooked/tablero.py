# Importando la librería pyxel
import pyxel
# Importando la clase Chef para poder usarla en la clase Tablero
from chef import Chef
from casilla import Casilla

class Tablero:
    def __init__(self, ancho: int, alto: int):
        # El mapa va a ser una matriz, y en función del número que tenga las casillas sera un "objeto" u otro
        # Diccionario que guarde que significa cada número de la matriz -> (tupla_sprite, es_transitable) # 
        CONFIG_CELDAS = {
            0: ((0, 32, 16, 16, 16), True),    # Suelo (se puede caminar)
            # TODO
        }
        self.mapa = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Fila 0
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Fila 1
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Fila 2
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Fila 3
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Fila 4
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Fila 5
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Fila 6
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Fila 7
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Fila 8
        ]
        # Transformamos la matriz de números en una matriz de objetos Casilla
        self.casillas = []
        for i in range(len(self.mapa)):
            fila_objetos = []
            for j in range(len(self.mapa[i])):
                sprite = CONFIG_CELDAS[self.mapa[i][j]][0] # Pillar la tupla del sprite en funcion de la casilla que se encuentre
                es_transitable = CONFIG_CELDAS[self.mapa[i][j]][1] # Pillar si 
                nueva_casilla = Casilla(i, j, self.mapa[i][j], sprite, es_transitable)
                fila_objetos.append(nueva_casilla)
            self.casillas.append(fila_objetos)
        # Estableciendo los atributos
        self.ancho = ancho # Ancho del tablero
        self.alto = alto # Alto del tablero
        self.chef = Chef(self.ancho // 2, self.alto // 2)

        # En este init también necesitamos inicializar pyxel
        # Esta instrucción se usa para inicializar pyxel, consulta la API para
        # ver más parámetros
        pyxel.init(self.ancho, self.alto, title="Overcooked en pyxel",display_scale=4)

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
        velocidad = 2

        if pyxel.btn(pyxel.KEY_A): # Velocidad negativa porque se mueve hacia la izquierda en las x
            self.chef.mover(-velocidad, 0, self.ancho, self.alto)
        if pyxel.btn(pyxel.KEY_D): # Velocidad positiva porque se mueve hacia la derecha en las x
            self.chef.mover(velocidad, 0, self.ancho, self.alto)
        if pyxel.btn(pyxel.KEY_W): # Velocidad negativa porque se mueve hacia arriba en las y (este eje va al reves)
            self.chef.mover(0, -velocidad, self.ancho, self.alto)
        if pyxel.btn(pyxel.KEY_S): # Velocidad positiva porque se mueve hacia abajo en las y (este eje va al reves)
            self.chef.mover(0, velocidad, self.ancho, self.alto)

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
            pyxel.blt(self.chef.x, self.chef.y, *self.chef.imagen[2], 0) # Ponemos un , 0) al final del pyxel.blt para que tenga fondo trasnparente
            self.chef.guardar_movimiento = 2
        elif pyxel.btn(pyxel.KEY_D):
            pyxel.blt(self.chef.x, self.chef.y, *self.chef.imagen[3], 0) # Ponemos un , 0) al final del pyxel.blt para que tenga fondo trasnparente
            self.chef.guardar_movimiento = 3
        elif pyxel.btn(pyxel.KEY_W):
            pyxel.blt(self.chef.x, self.chef.y, *self.chef.imagen[1], 0) # Ponemos un , 0) al final del pyxel.blt para que tenga fondo trasnparente
            self.chef.guardar_movimiento = 1
        elif pyxel.btn(pyxel.KEY_S): # Si tocas la tecla 6 
            pyxel.blt(self.chef.x, self.chef.y, *self.chef.imagen[0], 0) # Ponemos un , 0) al final del pyxel.blt para que tenga fondo trasnparente
            self.chef.guardar_movimiento = 0
        else:
            pyxel.blt(self.chef.x, self.chef.y, *self.chef.imagen[self.chef.guardar_movimiento], 0) # Ponemos un , 0) al final del pyxel.blt para que tenga fondo trasnparente

        
        # Un texto para mostrar la posición del chef, los parámetros de
        # pyxel.text son (x, y, texto, color)
        pyxel.text(10, 10, f"({self.chef.x}, {self.chef.y})", 7)