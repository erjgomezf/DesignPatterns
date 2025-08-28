import copy
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    La interfaz del Prototipo. Define un método para clonarse a sí mismo.
    """

    def __init__(self, x: int, y: int, color: str):
        self.x = x
        self.y = y
        self.color = color

    @abstractmethod
    def clone(self) -> "Shape":
        """
        El método de clonación. En Python, es común usar `copy.deepcopy`
        para asegurar una copia completa del objeto y sus atributos.
        """
        pass

    def __str__(self):
        return f"Shape(x={self.x}, y={self.y}, color='{self.color}')"


class Rectangle(Shape):
    """
    Un Prototipo Concreto.
    """

    def __init__(self, x: int, y: int, color: str, width: int, height: int):
        super().__init__(x, y, color)
        self.width = width
        self.height = height

    def clone(self) -> "Rectangle":
        return copy.deepcopy(self)


class Circle(Shape):
    """
    Otro Prototipo Concreto.
    """

    def __init__(self, x: int, y: int, color: str, radius: int):
        super().__init__(x, y, color)
        self.radius = radius

    def clone(self) -> "Circle":
        return copy.deepcopy(self)
