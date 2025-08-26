import sys
from .downloader import VideoDownloader
from .transcriber import AudioTranscriber
from .saver import TextSaver
from .service import TranscriptionService


def main(video_url: str):
    """
    Punto de entrada principal del script para descargar, transcribir y guardar
    el texto de un video de YouTube.
    """
    # Composición de dependencias: Aquí creamos las instancias concretas.
    service = TranscriptionService(
        downloader=VideoDownloader(output_path="temp_audio"),
        transcriber=AudioTranscriber(model_name="base"), # Usamos un modelo más pequeño para rapidez
        saver=TextSaver()
    )
    service.transcribe_video(video_url, "transcription.txt")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python -m src.solid_principles.youTubeTranscribe.after.main <youtube_video_url>")
        sys.exit(1)
    
    main(sys.argv[1])