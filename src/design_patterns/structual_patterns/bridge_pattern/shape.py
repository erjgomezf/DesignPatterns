"""
Módulo que define la Abstracción base en el patrón Bridge.
"""
from abc import ABC, abstractmethod
from .rendering_engine import RenderingEngine


class Shape(ABC):
    """
    La "Abstracción" define la interfaz para la parte de "control" de las dos
    jerarquías de clases. Mantiene una referencia a un objeto de la jerarquía
    de Implementación y delega todo el trabajo real a este objeto.
    """
    def __init__(self, renderer: RenderingEngine):
        self._renderer = renderer

    @abstractmethod
    def draw(self) -> None:
        pass

    @abstractmethod
    def resize(self, factor: float) -> None:
        pass
