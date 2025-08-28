"""
Módulo que define el objeto compuesto (Composite) que puede tener hijos.
"""
from typing import List
from .graphic import Graphic


class CompositeGraphic(Graphic):
    """
    La clase Compuesto (Composite) representa componentes complejos que pueden
    tener hijos. Usualmente, los objetos Compuesto delegan el trabajo real
    a sus hijos y luego "resumen" el resultado.
    """
    def __init__(self, name: str):
        self._name = name
        self._children: List[Graphic] = []

    def add(self, component: Graphic) -> None:
        """Añade un componente hijo."""
        self._children.append(component)

    def remove(self, component: Graphic) -> None:
        """Elimina un componente hijo."""
        self._children.remove(component)

    def draw(self, indentation: str = "") -> None:
        """
        Un compuesto ejecuta la operación `draw` sobre sí mismo y luego
        le pide a cada uno de sus hijos que se dibujen.
        """
        print(f"\n{indentation}[Contenedor: {self._name}]")
        for child in self._children:
            child.draw(indentation + "  ")
        print(f"{indentation}[/Contenedor: {self._name}]")

