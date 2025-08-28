"""
Módulo que define el objeto de Contexto que usa un Flyweight.
"""
from .tree_type import TreeType


class Tree:
    """
    La clase de Contexto. Contiene el estado extrínseco, que es único para
    cada árbol (sus coordenadas). También tiene una referencia a un objeto
    Flyweight (TreeType) que representa el estado intrínseco (compartido).
    """
    def __init__(self, x: int, y: int, tree_type: TreeType):
        self._x = x
        self._y = y
        self._tree_type = tree_type

    def draw(self):
        """
        El contexto delega la operación de dibujado al objeto Flyweight,
        pasándole el estado extrínseco necesario.
        """
        self._tree_type.draw(self._x, self._y)
