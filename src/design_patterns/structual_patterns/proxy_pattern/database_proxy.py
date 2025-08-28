"""
Módulo que define el Proxy que controla el acceso al objeto real.
"""
from typing import Dict
from .database_service import DatabaseService
from .real_database_service import RealDatabaseService


class DatabaseProxy(DatabaseService):
    """
    El Proxy tiene una interfaz idéntica al RealSubject.
    Puede gestionar el ciclo de vida del objeto RealSubject y añadir
    funcionalidades adicionales como el caching o el control de acceso.
    """

    def __init__(self, real_service: RealDatabaseService, user_role: str):
        self._real_service = real_service
        self._user_role = user_role
        self._cache: Dict[str, str] = {}

    def check_access(self) -> bool:
        """Simula una comprobación de permisos de acceso."""
        print("Proxy: Comprobando permisos de acceso...")
        if self._user_role == "admin":
            print("Proxy: Acceso permitido.")
            return True
        print("Proxy: Acceso denegado.")
        return False

    def request_data(self, query: str) -> str:
        """
        La operación más común del proxy es el caching (inicialización diferida).
        A diferencia del RealSubject, el proxy puede pasar los datos cacheados
        si ya han sido solicitados anteriormente.
        """
        if not self.check_access():
            return "Error: No tienes permiso para realizar esta consulta."

        if query in self._cache:
            print(f"Proxy: Devolviendo resultado cacheado para la consulta '{query}'.")
            return self._cache[query]

        print(f"Proxy: La consulta '{query}' no está en caché. Delegando al servicio real.")
        result = self._real_service.request_data(query)
        self._cache[query] = result
        return result
