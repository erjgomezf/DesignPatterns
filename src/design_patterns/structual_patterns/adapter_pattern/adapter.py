"""
El módulo Adapter que hace que dos interfaces incompatibles trabajen juntas.
"""
import xml.etree.ElementTree as ET
from typing import Dict, Any

from .modern_service import XMLData


class XMLToJSONAdapter:
    """
    El Adaptador que envuelve un objeto XMLData y expone una interfaz
    compatible con el sistema antiguo (que espera un diccionario/JSON).
    """
    def __init__(self, xml_data: XMLData):
        self._xml_data = xml_data

    def to_dict(self) -> Dict[str, Any]:
        """
        Realiza la conversión de la cadena XML a un diccionario de Python.
        Esta es la esencia del adaptador.
        """
        print("Adaptador: Convirtiendo XML a Diccionario (JSON)...
")
        try:
            root = ET.fromstring(self._xml_data.xml_content)
            # Lógica de conversión simple para el ejemplo
            data = {}
            for item in root.findall('item'):
                name = item.get('name')
                price = item.find('price')
                if name and price is not None and price.text:
                    data[name] = float(price.text)
            return {"items": data}
        except ET.ParseError:
            return {"error": "No se pudo parsear el XML"}

