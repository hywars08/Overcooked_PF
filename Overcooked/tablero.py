# Importando la librería pyxel
import pyxel
# Importando la clase Chef para poder usarla en la clase Tablero
from chef import Chef


class Tablero:
    def __init__(self, ancho: int, alto: int):
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

    def dibujar(self):
        """Este es el método de pyxel que se ejecuta en cada iteración del
        juego (cada fotograma). Aquí debes poner todo el código para dibujar
        los sprites del juego.
        """
        # Borrando la pantalla anterior
        pyxel.cls(0)
        # Dibujando al chef. Los parámetros de pyxel.blt son (x, y, tupla_sprite)
        # El * se usa para desempaquetar la tupla del sprite
        pyxel.blt(self.chef.x, self.chef.y, *self.chef.imagen)
        # Un texto para mostrar la posición del chef, los parámetros de
        # pyxel.text son (x, y, texto, color)
        pyxel.text(10, 10, f"({self.chef.x}, {self.chef.y})", 7)