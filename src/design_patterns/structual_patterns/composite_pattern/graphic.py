"""
Módulo que define la interfaz base para todos los componentes gráficos.
"""
from abc import ABC, abstractmethod


class Graphic(ABC):
    """
    La interfaz Componente declara operaciones comunes tanto para los objetos
    simples (hojas) como para los complejos (compuestos).
    """

    @abstractmethod
    def draw(self, indentation: str = "") -> None:
        """Dibuja el componente gráfico."""
        pass

    def add(self, component: 'Graphic') -> None:
        """
        Por defecto, los componentes hoja no pueden tener hijos.
        """
        raise NotImplementedError("Este es un componente hoja (leaf).")

    def remove(self, component: 'Graphic') -> None:
        """
        Por defecto, los componentes hoja no pueden tener hijos.
        """
        raise NotImplementedError("Este es un componente hoja (leaf).")
