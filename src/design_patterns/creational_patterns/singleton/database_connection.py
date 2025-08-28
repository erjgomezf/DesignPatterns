import time
import random
from threading import Lock, Thread


class DatabaseConnection:
    """
    La clase Singleton.
    En Python, es común implementar el patrón Singleton usando un método de clase
    que gestione la creación de la instancia, o sobrescribiendo el método __new__.

    Esta implementación es thread-safe.
    """

    _instance = None
    _lock: Lock = Lock()

    def __new__(cls, *args, **kwargs):
        # El primer chequeo de la instancia se hace sin bloqueo para mejorar el rendimiento.
        if cls._instance is None:
            # Si la instancia no existe, se adquiere el bloqueo.
            # El bloqueo asegura que solo un hilo pueda crear la instancia.
            with cls._lock:
                # Se vuelve a comprobar si otro hilo ya creó la instancia
                # mientras el hilo actual esperaba el bloqueo.
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """
        El inicializador se llamará cada vez que se intente "crear" un objeto,
        pero la instancia será siempre la misma. Para evitar reinicializar,
        se puede comprobar si los atributos ya existen.
        """
        if not hasattr(self, 'connection_id'):
            # Simula una conexión costosa
            time.sleep(1)
            self.connection_id = random.randint(1000, 9999)
            print(f"Nueva conexión a la base de datos establecida. ID: {self.connection_id}")

    def query(self, sql: str):
        """Un método de ejemplo para usar la conexión."""
        print(f"Ejecutando query '{sql}' en la conexión {self.connection_id}")
