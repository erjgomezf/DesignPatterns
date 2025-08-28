"""
Módulo que define el objeto real que el proxy representará.
"""
import time
from .database_service import DatabaseService


class RealDatabaseService(DatabaseService):
    """
    El RealSubject contiene la lógica de negocio principal. Usualmente, los
    RealSubjects son capaces de hacer trabajo pesado, como en este caso,
    una consulta a la base de datos que consume mucho tiempo.
    """

    def request_data(self, query: str) -> str:
        print("RealDatabaseService: Conectando a la base de datos y ejecutando una consulta costosa...")
        # Simula una operación de red o de base de datos que consume tiempo
        time.sleep(2)
        result = f"Datos para la consulta '{query}'"
        print("RealDatabaseService: Consulta completada.")
        return result
