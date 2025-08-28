"""
Módulo que simula un servicio moderno que trabaja con datos en formato XML.
"""

class XMLData:
    """Una clase que representa datos en un formato similar a XML."""
    def __init__(self, content: str):
        # En un caso real, esto podría ser un árbol XML (ej. de ElementTree)
        self._content = content

    @property
    def xml_content(self) -> str:
        return self._content


class ModernService:
    """Este servicio obtiene datos y los devuelve en formato XMLData."""
    def get_data(self) -> XMLData:
        print("Servicio moderno: Obteniendo datos y empaquetándolos en XML.")
        # Simula la obtención de datos y su representación en XML
        xml_string = "<data><item name='Producto A'><price>120.50</price></item></data>"
        return XMLData(xml_string)
