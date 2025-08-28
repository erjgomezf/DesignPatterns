"""
Implementaciones concretas del patrón Strategy.
"""
import json
from typing import Any, Dict

from .export_strategy import ExportStrategy


class JSONExportStrategy(ExportStrategy):
    """Estrategia para exportar datos a formato JSON."""

    def export(self, data: Dict[str, Any]) -> None:
        print("Exportando datos a JSON...")
        print(json.dumps(data, indent=2, ensure_ascii=False))


class CSVExportStrategy(ExportStrategy):
    """Estrategia para exportar datos a formato CSV."""

    def export(self, data: Dict[str, Any]) -> None:
        print("Exportando datos a CSV...")
        headers = ",".join(data.keys())
        values = ",".join(str(v) for v in data.values())
        csv_data = f"{headers}\n{values}"
        print(csv_data)
