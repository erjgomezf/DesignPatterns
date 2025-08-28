"""
El Contexto que utiliza una estrategia para realizar su trabajo.
"""
from typing import Any, Dict

from .export_strategy import ExportStrategy


class ReportGenerator:
    """
    El Contexto define la interfaz de interés para los clientes. Mantiene una
    referencia a una de las estrategias y delega el trabajo en ella.
    """

    def __init__(self, data: Dict[str, Any]):
        self._data = data
        self._strategy: ExportStrategy | None = None

    def set_strategy(self, strategy: ExportStrategy) -> None:
        """Permite al cliente cambiar la estrategia en tiempo de ejecución."""
        print(f"ReportGenerator: Usando la estrategia {type(strategy).__name__}")
        self._strategy = strategy

    def generate_report(self) -> None:
        """Delega la generación del reporte a la estrategia actual."""
        if not self._strategy:
            raise ValueError("La estrategia de exportación no ha sido establecida.")
        self._strategy.export(self._data)
