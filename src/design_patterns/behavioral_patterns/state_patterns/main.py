"""
Cliente que demuestra el uso del patrón State.
"""
from .concrete_states import DraftState
from .document import Document


def client_code():
    """
    El código cliente que crea un documento y lo hace pasar por
    diferentes estados.
    """
    doc = Document(DraftState())
    doc.content = "Este es mi primer borrador."

    print("\n--- Intentando publicar desde el estado Borrador ---")
    doc.publish()

    print("\n--- Solicitando revisión ---")
    doc.request_review()

    print("\n--- Intentando solicitar revisión de nuevo (en Moderación) ---")
    doc.request_review()

    print("\n--- Publicando el documento ---")
    doc.publish()

    print("\n--- Intentando publicar de nuevo (ya Publicado) ---")
    doc.publish()


if __name__ == "__main__":
    client_code()

