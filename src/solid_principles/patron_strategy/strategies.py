from typing import Protocol, List, Dict, Any
import json
import csv
import io

class ExportStrategy(Protocol):
    """
    La interfaz Strategy declara operaciones comunes a todas las versiones
    soportadas de algún algoritmo. El Contexto usa esta interfaz para llamar
    al algoritmo definido por las Concrete Strategies.
    """
    def export(self, data: List[Dict[str, Any]]) -> str:
        """
        Exporta los datos a un formato de string específico.
        """
        ...

class JsonExportStrategy:
    """
    Concrete Strategy: Implementa el algoritmo para exportar a formato JSON.
    """
    def export(self, data: List[Dict[str, Any]]) -> str:
        print("-> Usando la estrategia de exportación a JSON.")
        return json.dumps(data, indent=4)

class CsvExportStrategy:
    """
    Concrete Strategy: Implementa el algoritmo para exportar a formato CSV.
    """
    def export(self, data: List[Dict[str, Any]]) -> str:
        print("-> Usando la estrategia de exportación a CSV.")
        if not data:
            return ""
        
        # Usamos io.StringIO para escribir el CSV en memoria como un string
        output = io.StringIO()
        fieldnames = data[0].keys()
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(data)
        
        return output.getvalue()

class HtmlExportStrategy:
    """
    Concrete Strategy: Implementa el algoritmo para exportar a formato HTML.
    """
    def export(self, data: List[Dict[str, Any]]) -> str:
        print("-> Usando la estrategia de exportación a HTML.")
        if not data:
            return "<table></table>"

        headers = "".join([f"<th>{key}</th>" for key in data[0].keys()])
        
        rows = ""
        for item in data:
            row_data = "".join([f"<td>{value}</td>" for value in item.values()])
            rows += f"<tr>{row_data}</tr>"
            
        return f"""
<table border="1">
  <thead>
    <tr>{headers}</tr>
  </thead>
  <tbody>
    {rows}
  </tbody>
</table>
"""