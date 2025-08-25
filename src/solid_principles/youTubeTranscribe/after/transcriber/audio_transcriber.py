import whisper
import os


class AudioTranscriber:
    """
    Clase que recibe una ruta de un archivo de audio y retorna el texto transcrito.
    :param audio_path: Ruta del archivo de audio.
    :type audio_path: str
    :return: Texto transcrito.
    :rtype: str

    """
    def __init__(self, model_name: str = "large"):
        """
        Inicializa la clase transcribe_youtube_video.
        :param model_name: Nombre del modelo de Whisper a utilizar.
        :type model_name: str
        """
        print(f"Cargando el modelo de whisper...")
        # Guardamos el modulo como un atributo de la instacia
        self.model = whisper.load_model(model_name)
        print(f"Modelo cargado exitosamente...")

    def transcribe_audio(self, audio_path) -> str:
        """
        Transcribe un video de audio y retorna el texto transcrito.
        :param audio_path: Ruta del archivo de audio.
        :type audio_path: str
        :return: Texto transcrito.
        :rtype: str
        """
        print(f"Transcribiendo el audio...")
        
        try:
            result = self.model.transcribe(audio_path, fp16=False)
            print(f"Audio transcrito exitosamente...")
            return result["text"]
        except Exception as e:
            print(f"Error al transcribir el audio: {e}")
            return None
        finally:
            try:
                os.remove(audio_path)
            except Exception as e:
                print(f"Error al eliminar el archivo de audio: {e}")
                