from abc import ABC, abstractmethod

class DataProcessor(ABC):
    """
    Clase Abstracta que define el esqueleto del algoritmo de procesamiento de datos.
    """

    def process(self):
        """
        El método plantilla que define la secuencia del algoritmo.
        """
        self.read_data()
        self.transform_data()
        self.hook_after_transform()
        self.save_data()

    @abstractmethod
    def read_data(self):
        """Paso abstracto: Leer los datos."""
        pass

    @abstractmethod
    def transform_data(self):
        """Paso abstracto: Procesar los datos."""
        pass

    def save_data(self):
        """Paso con implementación por defecto: Guardar los datos."""
        print("Guardando los datos procesados en la base de datos.")

    def hook_after_transform(self):
        """
        Hook: un paso opcional que las subclases pueden anular.
        Por defecto, no hace nada.
        """
        pass
