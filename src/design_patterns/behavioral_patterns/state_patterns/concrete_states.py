"""
Implementaciones concretas de los estados del documento.
"""
from .document_state import DocumentState


class DraftState(DocumentState):
    """Estado: El documento es un borrador."""

    def request_review(self) -> None:
        print("Estado Borrador: Solicitando revisión. Pasando a Moderación.")
        # pylint: disable=import-outside-toplevel
        from .concrete_states import ModerationState
        self.document.transition_to(ModerationState())

    def publish(self) -> None:
        print("Estado Borrador: No se puede publicar. Primero solicita una revisión.")


class ModerationState(DocumentState):
    """Estado: El documento está en revisión."""

    def request_review(self) -> None:
        print("Estado Moderación: Ya está en proceso de revisión.")

    def publish(self) -> None:
        print("Estado Moderación: Aprobando y publicando. Pasando a Publicado.")
        # pylint: disable=import-outside-toplevel
        from .concrete_states import PublishedState
        self.document.transition_to(PublishedState())


class PublishedState(DocumentState):
    """Estado: El documento ha sido publicado."""

    def request_review(self) -> None:
        print("Estado Publicado: No se puede solicitar revisión, ya está publicado.")

    def publish(self) -> None:
        print("Estado Publicado: El documento ya ha sido publicado.")