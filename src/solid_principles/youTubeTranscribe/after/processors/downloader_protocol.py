from typing import Protocol, Optional



class DownloaderProtocol(Protocol):
    """
    Protocolo que define la interfaz para un descargador de video/audio.
    """
    def download_video(self, video_url: str) -> Optional[str]:
        """
        Descarga un video/audio y devuelve la ruta al archivo local.
        """
        ...