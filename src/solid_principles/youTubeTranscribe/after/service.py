from dataclasses import dataclass
import os
from .saver import TextSaver
from .processors import DownloaderProtocol, TranscriberProtocol

@dataclass
class TranscriptionService:
    """
    Servicio de alto nivel que orquesta el proceso de transcripción.
    Depende de abstracciones (protocolos) para ser flexible y extensible.
    """
    downloader: DownloaderProtocol
    transcriber: TranscriberProtocol
    saver: TextSaver

    def transcribe_video(self, video_url: str, output_filename: str):
        print("--- Iniciando proceso de transcripción ---")
        # 1. Descargar
        audio_path = self.downloader.download_video(video_url)
        if not audio_path:
            print("Fallo en la descarga. Abortando.")
            return

        try:
            # 2. Transcribir
            text = self.transcriber.transcribe_audio(audio_path)
            if not text:
                print("Fallo en la transcripción. Abortando.")
                return

            # 3. Guardar
            saved_successfully = self.saver.save_text(text, output_filename)
            if saved_successfully:
                print(f"Transcripción guardada exitosamente en '{output_filename}'")
            else:
                print("Fallo al guardar la transcripción. El archivo temporal será eliminado de todas formas.")

        finally:
            # 4. Limpieza robusta
            if os.path.exists(audio_path):
                print(f"Limpiando archivo temporal '{audio_path}'...")
                try:
                    os.remove(audio_path)
                    print(f"Archivo temporal '{audio_path}' eliminado.")
                except OSError as e:
                    print(f"Error al eliminar el archivo temporal '{audio_path}': {e}")
        
        print("--- Proceso de transcripción finalizado ---")
