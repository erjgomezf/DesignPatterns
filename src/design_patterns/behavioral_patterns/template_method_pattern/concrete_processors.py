from .data_processor import DataProcessor

class CSVDataProcessor(DataProcessor):
    """
    Clase Concreta para procesar datos de un archivo CSV.
    """
    def read_data(self):
        print("Leyendo datos de un archivo CSV.")

    def transform_data(self):
        print("Transformando los datos del CSV (ej. convirtiendo a JSON).")

class APIDataProcessor(DataProcessor):
    """
    Clase Concreta para procesar datos desde una API.
    """
    def read_data(self):
        print("Obteniendo datos desde un endpoint de API.")

    def transform_data(self):
        print("Transformando los datos de la API (ej. filtrando campos).")

    def hook_after_transform(self):
        print("Hook: Realizando una validación extra de los datos de la API.")

    def save_data(self):
        """Anulando el método para guardar en un sistema de archivos en la nube."""
        print("Guardando los datos procesados en un bucket de S3.")
