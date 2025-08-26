import whisper
from typing import Optional
from ..processors import TranscriberProtocol



class AudioTranscriber(TranscriberProtocol):
    """
    Clase responsable de transcribir un archivo de audio a texto usando Whisper.
    """

    def __init__(self, model_name: str = "large"):
        """
        Inicializa el transcriptor cargando el modelo de Whisper especificado.

        Args:
            model_name: El nombre del modelo de Whisper a utilizar (ej. "base", "large").
        """
        print(f"Cargando el modelo de whisper...")
        # Guardamos el modelo como un atributo de la instancia
        self.model = whisper.load_model(model_name)
        print(f"Modelo cargado exitosamente...")

    def transcribe_audio(self, audio_path: str) -> Optional[str]:
        """
        Transcribe un archivo de audio y devuelve el texto resultante.

        Args:
            audio_path: La ruta al archivo de audio a transcribir.

        Returns:
            El texto transcrito, o None si ocurre un error.
        """
        print(f"Transcribiendo el audio...")

        try:
            result = self.model.transcribe(audio_path, fp16=False)
            print(f"Audio transcrito exitosamente...")
            return result["text"]
        except Exception as e:
            print(f"Error al transcribir el audio: {e}")
            return None