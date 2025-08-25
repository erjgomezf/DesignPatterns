import sys
from .downloader import VideoDownloader
from .transcriber import AudioTranscriber
from .saver import TextSaver


if __name__ == "__main__":
    video_downloader = VideoDownloader()
    audio_transcriber = AudioTranscriber()
    text_saver = TextSaver()
    
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <youtube_video_url>")
        sys.exit(1)

    youtube_video_url = sys.argv[1]
    audio_path = video_downloader.download_video(youtube_video_url)
    text = audio_transcriber.transcribe_audio(audio_path)
    text_saver.save_text(text)
    
        