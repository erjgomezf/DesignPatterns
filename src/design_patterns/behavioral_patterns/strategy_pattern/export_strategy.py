"""
Define la interfaz (Protocol) para el patrón Strategy.
"""
from typing import Any, Dict, Protocol


class ExportStrategy(Protocol):
    """
    La interfaz Strategy declara operaciones comunes a todas las versiones
    soportadas de algún algoritmo.
    """

    def export(self, data: Dict[str, Any]) -> None:
        """El método que ejecuta la estrategia."""
        ...
