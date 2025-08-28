"""
Cliente que demuestra el uso del patrón Strategy.
"""
from .concrete_strategies import CSVExportStrategy, JSONExportStrategy
from .report_generator import ReportGenerator


def client_code():
    """
    El código cliente que configura el contexto con diferentes estrategias
    y ejecuta la operación.
    """
    report_data = {
        "titulo": "Ventas Mensuales",
        "total_ventas": 15000,
        "mes": "Octubre",
    }

    generator = ReportGenerator(report_data)

    print("--- Generando reporte en formato JSON ---")
    generator.set_strategy(JSONExportStrategy())
    generator.generate_report()

    print("\n--- Cambiando de estrategia y generando en formato CSV ---")
    generator.set_strategy(CSVExportStrategy())
    generator.generate_report()


if __name__ == "__main__":
    client_code()