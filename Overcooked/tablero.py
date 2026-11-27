# Importando la librería pyxel
import pyxel
# Importando la clase Chef para poder usarla en la clase Tablero
from chef import Chef
from casilla import Casilla
from plato import Plato

class Tablero:
    # Constantes de Tablero
    # Diccionario que guarda que significa cada número de la matriz -> tupla_sprite
    TIPO_CELDAS = {
        0: (0, 32, 16, 16, 16), # Suelo normal (cocina) 
        1: (0, 32, 0, 16, 16), # Encimera normal (se pueden dejar objetos)
        2: (0, 32, 32, 16, 16), # Caja de Cebolla
        3: (0, 32, 32, 16, 16), # Caja de Huevos
        4: (0, 32, 32, 16, 16), # Caja de Chorizo
        5: (0, 32, 32, 16, 16), # Caja de Tomates
        6: (0, 32, 32, 16, 16), # Caja de Patatas 
        7: (0, 32, 32, 16, 16) # Caja de Plato
        # TODO
    }
    # Declaración de constantes
    TAMANO_CASILLA = 16 # SOn 16 píxeles
    
    def __init__(self, ancho: int, alto: int):
        # Estableciendo los atributos
        self.ancho = ancho # Ancho del tablero
        self.alto = alto # Alto del tablero

        # El mapa va a ser una matriz, y en función del número que tenga las casillas sera un "objeto" u otro
        self.mapa = [
            [2, 3, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # Fila 0
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Fila 1
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Fila 2
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Fila 3
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # Fila 4
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Fila 5
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Fila 6
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Fila 7
            [5, 6, 1, 1, 1, 1, 1, 1, 1, 7, 1, 1]   # Fila 8
        ]
        # Transformamos la matriz de números en una matriz de objetos Casilla
        self.casillas = []
        for i in range(len(self.mapa)):
            fila_objetos = []
            for j in range(len(self.mapa[i])):
                sprite = Tablero.TIPO_CELDAS[self.mapa[i][j]] # Pillar la tupla del sprite en funcion de la casilla que se encuentre en la matriz
                nueva_casilla = Casilla(i, j, self.mapa[i][j], sprite) # Generar el objeto casilla
                fila_objetos.append(nueva_casilla)
            self.casillas.append(fila_objetos)

        self.chef1 = Chef(1, 2, "jugador1")
        self.chef2 = Chef(1, 6, "jugador2") 
        self.chefs = [self.chef1, self.chef2]
        # En este init también necesitamos inicializar pyxel
        # Esta instrucción se usa para inicializar pyxel, consulta la API para
        # ver más parámetros
        pyxel.init(self.ancho * Tablero.TAMANO_CASILLA, self.alto * Tablero.TAMANO_CASILLA, title="Overcooked en pyxel",display_scale=4, fps=6)

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

        # Controles del chef
        for chef in self.chefs:
            if (pyxel.btn(chef.controles["arriba"]) or pyxel.btn(chef.controles["abajo"]) or pyxel.btn(chef.controles["izquierda"]) or pyxel.btn(chef.controles["derecha"])):
                # Cambiar la dirección del chef
                chef.direccion_chef()

                # Comprobar si se puede mover
                if self.casilla_delante_chef(chef) == 0:
                    chef.mover(len(self.mapa[0]), len(self.mapa))

            if pyxel.btn(chef.controles["interactuar"]):
                chef.interactuar(self.casilla_delante_chef(chef))
                

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

        # Dibujando a los chefs. 
        for chef in self.chefs:
            chef.dibujar_chef(Tablero.TAMANO_CASILLA)

            if chef.interactuar(self.casilla_delante_chef(chef)):
                pyxel.text(chef.x * 16, ((chef.y) * 16) + 32 - 8, "Accion", 7)

            if chef.objeto != "ninguno":
                chef.objeto.x = chef.x
                chef.objeto.y = chef.y
                chef.objeto.dibujar_item(Tablero.TAMANO_CASILLA, chef.tiene_objeto(), chef.direccion)
            
        # Un texto para mostrar la posición del chef, los parámetros de
        # pyxel.text son (x, y, texto, color)
        pyxel.text(10, 10, f"({self.chef1.x}, {self.chef1.y})", 7)
        pyxel.text(12, 12, f"({self.chef2.x}, {self.chef2.y})", 7)
        
    def casilla_delante_chef(self, chef: Chef):
        x_delante = chef.x
        y_delante = chef.y 

        if chef.direccion == "arriba":
            y_delante -= 1
        elif chef.direccion == "abajo":
            y_delante += 1
        elif chef.direccion == "derecha":
            x_delante += 1
        else: 
            x_delante -= 1

        # Comprobar que esta dentro de los bordes
        if 0 <= y_delante < len(self.mapa) and 0 <= x_delante < len(self.mapa[0]): 
            return self.mapa[y_delante][x_delante]
        else:
            return -1 # casilla no válida
        
        

        
            