"""
Módulo que define el objeto Flyweight que contiene el estado intrínseco (compartido).
"""

class TreeType:
    """
    La clase Flyweight contiene la porción del estado de un árbol que puede ser
    compartida entre varios árboles. A esto se le llama "estado intrínseco".
    """
    def __init__(self, name: str, color: str, texture: str):
        print(f"** Creando un nuevo tipo de árbol (Flyweight): {name} **")
        self._name = name
        self._color = color
        self._texture = texture

    def draw(self, x: int, y: int):
        """
        El método que "dibuja" el árbol. Recibe el estado extrínseco
        (las coordenadas) como parámetros.
        """
        print(f"Dibujando un '{self._name}' de color '{self._color}' en ({x}, {y})")
