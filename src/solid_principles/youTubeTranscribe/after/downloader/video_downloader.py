import pytube as pt
import uuid


class VideoDownloader:
    '''
    Clase que descarga un video y retorna la ruta del archivo.
    :param video_url: URL del video a descargar.
    :type video_url: str
    :return: Ruta del archivo descargado.
    :rtype: str
    
    '''  
     
    def download_video(self, video_url):
        try:
            yt = pt.YouTube(video_url)
            stream = yt.streams.filter(only_audio=True)[0]
            temp_file_name = f"{uuid.uuid4()}.mp3"
            stream.download(filename=temp_file_name)
            print(f"Video descargado exitosamente como {temp_file_name}")
            return temp_file_name
        except Exception as e:
            print(f"Error al descargar el video: {e}")
            return None