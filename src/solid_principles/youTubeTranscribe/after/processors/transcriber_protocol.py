from typing import Protocol, Optional



class TranscriberProtocol(Protocol):
    """
    Protocolo que define la interfaz para un transcriptor de audio.
    """
    def transcribe_audio(self, audio_path: str) -> Optional[str]:
        """
        Transcribe un archivo de audio y devuelve el texto.
        """
        ...