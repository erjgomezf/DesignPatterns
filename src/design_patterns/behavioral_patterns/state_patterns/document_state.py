"""
La interfaz de Estado (State) que define los métodos para todos los estados.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

# Para evitar importaciones circulares, usamos TYPE_CHECKING
if TYPE_CHECKING:
    from .document import Document


class DocumentState(ABC):
    """
    La clase base Estado declara métodos que todos los estados concretos deben
    implementar y también proporciona una referencia al objeto Contexto.
    """

    _document: Document

    @property
    def document(self) -> Document:
        return self._document

    @document.setter
    def document(self, document: Document) -> None:
        self._document = document

    @abstractmethod
    def request_review(self) -> None:
        pass

    @abstractmethod
    def publish(self) -> None:
        pass

