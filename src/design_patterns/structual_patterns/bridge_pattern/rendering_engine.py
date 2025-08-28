"""
Módulo que define la interfaz de Implementación (Implementor) para el renderizado.
"""
from abc import ABC, abstractmethod


class RenderingEngine(ABC):
    """
    La interfaz de Implementación declara métodos comunes a todas las
    implementaciones concretas. No tiene por qué coincidir con la interfaz
    de la Abstracción.
    """

    @abstractmethod
    def render_circle(self, radius: float) -> None:
        pass

    @abstractmethod
    def render_square(self, side: float) -> None:
        pass
