"""
Módulo que simula un sistema antiguo que solo entiende datos en formato JSON.
"""
import json
from typing import Dict, Any

def display_json(data: Dict[str, Any]) -> None:
    """
    Función del sistema antiguo que toma un diccionario (simulando JSON)
    y lo muestra de una manera específica.
    """
    print("--- Mostrando datos en el sistema antiguo (formato JSON) ---")
    # Simula un procesamiento o visualización específica para JSON
    pretty_json = json.dumps(data, indent=4)
    print(pretty_json)
    print("----------------------------------------------------------\n")

