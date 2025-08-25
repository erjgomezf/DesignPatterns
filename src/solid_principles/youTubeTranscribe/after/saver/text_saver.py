import datetime


class TextSaver:
    """
    Clase que recibe un texto y lo guarda en un archivo.
    :param text: Texto a guardar.
    :type text: str
    :return: None
    """    
    def save_text(self, text):
        date_now = datetime.datetime.now()
        date_format = "%Y-%m-%d_%H-%M-%S"
        date_string = date_now.strftime(date_format)
        file_name = f"file_{date_string}.txt"
        with open(file_name, "w") as file:
            file.write(text)
        print(text)