from typing import List, Dict, Any
from .strategies import ExportStrategy

class ReportGenerator:
    """
    El Contexto define la interfaz de interés para los clientes.
    Mantiene una referencia a un objeto de una de las estrategias y
    delega la ejecución del trabajo a ese objeto.
    """
    def __init__(self, strategy: ExportStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: ExportStrategy):
        """
        Permite cambiar la estrategia en tiempo de ejecución.
        """
        print(f"\nCambiando la estrategia de '{self._strategy.__class__.__name__}' a '{strategy.__class__.__name__}'.")
        self._strategy = strategy

    def generate_report(self, data: List[Dict[str, Any]]) -> str:
        """
        El Contexto delega el trabajo de exportación a la estrategia actual.
        No conoce los detalles de la implementación de la estrategia.
        """
        print("El generador de reportes (Contexto) está generando el reporte...")
        report = self._strategy.export(data)
        print("Reporte generado.")
        return report