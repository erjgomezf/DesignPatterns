from typing import Protocol


class SaverProtocol(Protocol):
    """
    Protocolo que define la interfaz para un guardador de texto.
    """
    def save_text(self, text: str, output_filename: str) -> bool:
        """
        Guarda el texto proporcionado en un destino.
        """
        ...