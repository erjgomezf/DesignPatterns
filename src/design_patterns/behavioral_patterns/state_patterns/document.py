"""
El Contexto (Document) que mantiene una referencia a su estado actual.
"""
from __future__ import annotations

from typing import TYPE_CHECKING

# Para evitar importaciones circulares, usamos TYPE_CHECKING
if TYPE_CHECKING:
    from .document_state import DocumentState


class Document:
    """
    El Contexto. Mantiene una instancia de una subclase de Estado que
    representa el estado actual del documento.
    """

    _state: DocumentState

    def __init__(self, state: DocumentState):
        self.content: str = ""
        self.transition_to(state)

    def transition_to(self, state: DocumentState) -> None:
        """Permite cambiar el objeto de Estado en tiempo de ejecución."""
        print(f"Documento: Transición a {type(state).__name__}.")
        self._state = state
        self._state.document = self

    def request_review(self) -> None:
        """Delega la acción al objeto de estado actual."""
        self._state.request_review()

    def publish(self) -> None:
        """Delega la acción al objeto de estado actual."""
        self._state.publish()

