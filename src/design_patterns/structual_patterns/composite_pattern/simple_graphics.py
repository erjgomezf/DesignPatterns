"""
Módulo que define los objetos hoja (leaf) del árbol de composición.
"""
from .graphic import Graphic


class Circle(Graphic):
    """
    La clase Hoja (Leaf) representa los objetos finales de una composición.
    Una hoja no puede tener hijos.
    """
    def __init__(self, name: str):
        self._name = name

    def draw(self, indentation: str = "") -> None:
        print(f"{indentation}- Círculo: {self._name}")


class Square(Graphic):
    """
    Otra clase Hoja.
    """
    def __init__(self, name: str):
        self._name = name

    def draw(self, indentation: str = "") -> None:
        print(f"{indentation}- Cuadrado: {self._name}")
