import os
from ..processors import SaverProtocol



class TextSaver(SaverProtocol):
    """
    Clase responsable de guardar texto en un archivo de forma segura.
    """

    def save_text(self, text: str, output_filename: str) -> bool:
        """
        Guarda el texto proporcionado en un archivo, creando el directorio si no existe.

        Args:
            text: El contenido de texto a guardar.
            output_filename: La ruta completa del archivo de salida.

        Returns:
            True si el guardado fue exitoso, False en caso contrario.
        """
        try:
            output_dir = os.path.dirname(output_filename)
            if output_dir:
                os.makedirs(output_dir, exist_ok=True)

            with open(output_filename, "w", encoding="utf-8") as f:
                f.write(text)
            return True
        except IOError as e:
            print(f"Error al guardar el archivo '{output_filename}': {e}")
            return False