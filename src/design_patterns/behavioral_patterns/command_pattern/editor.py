"""
Módulo que define el "Receptor" (Receiver), que contiene la lógica de negocio.
"""

class Editor:
    """
    El Receptor. Contiene la lógica de negocio real. Casi cualquier objeto puede
    ser un receptor. La mayoría de los comandos solo manejan los detalles de cómo
    una solicitud se pasa a un receptor.
    """
    def __init__(self):
        self.text = ""
        self.clipboard = ""

    def get_selection(self) -> str:
        # En una aplicación real, esto obtendría el texto seleccionado
        print("Editor: Obteniendo selección (simulado)")
        return "texto seleccionado"

    def delete_selection(self):
        # En una aplicación real, esto eliminaría el texto seleccionado
        print("Editor: Eliminando selección (simulado)")

    def __str__(self) -> str:
        return f"Editor(Texto: '{self.text}', Portapapeles: '{self.clipboard}')"
