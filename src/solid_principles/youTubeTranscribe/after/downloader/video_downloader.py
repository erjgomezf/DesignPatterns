import os
import pytube as pt
import uuid
from typing import Optional
from ..processors import DownloaderProtocol


class VideoDownloader(DownloaderProtocol):
    """
    Clase responsable de descargar el audio de un video de YouTube.

    Attributes:
        output_path (str): El directorio donde se guardarán los archivos de audio.
    """

    def __init__(self, output_path: str = "temp_audio"):
        self.output_path = output_path
        # Aseguramos que el directorio de salida exista
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)

    def download_video(self, video_url: str) -> Optional[str]:
        """
        Descarga el audio de un video de YouTube y lo guarda en un archivo MP3.

        Args:
            video_url: La URL completa del video de YouTube.

        Returns:
            La ruta al archivo de audio descargado, o None si ocurre un error.
        """
        try:
            yt = pt.YouTube(video_url)
            stream = yt.streams.filter(only_audio=True)[0]
            file_path = stream.download(output_path=self.output_path, filename=f"{uuid.uuid4()}.mp3")
            print(f"Audio descargado exitosamente en: {file_path}")
            return file_path
        except Exception as e:
            print(f"Error al descargar el video: {e}")
            return None