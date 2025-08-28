"""
Módulo que define la interfaz común (Asunto) para el servicio real y el proxy.
"""
from abc import ABC, abstractmethod


class DatabaseService(ABC):
    """
    La interfaz Asunto (Subject) declara las operaciones comunes tanto para el
    RealSubject como para el Proxy. Mientras el cliente trabaje con el RealSubject
    usando esta interfaz, podrás pasarle un proxy en lugar del objeto real.
    """

    @abstractmethod
    def request_data(self, query: str) -> str:
        pass
