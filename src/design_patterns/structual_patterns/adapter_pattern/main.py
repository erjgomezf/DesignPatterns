"""
Cliente que demuestra el uso del patrón Adapter.
"""
from .legacy_system import display_json
from .modern_service import ModernService
from .adapter import XMLToJSONAdapter


def client_code():
    """
    El código cliente que necesita usar el servicio moderno con el sistema antiguo.
    """
    # 1. Obtenemos los datos del servicio moderno en su formato nativo (XML)
    modern_service = ModernService()
    xml_data = modern_service.get_data()

    # 2. El sistema antiguo no puede manejar estos datos directamente.
    # display_json(xml_data)  # Esto daría un error de tipo

    # 3. Usamos el adaptador para convertir la interfaz del objeto XMLData
    #    a la interfaz que el sistema antiguo espera (un diccionario).
    adapter = XMLToJSONAdapter(xml_data)
    json_compatible_data = adapter.to_dict()

    # 4. Ahora podemos pasar los datos adaptados al sistema antiguo.
    display_json(json_compatible_data)


if __name__ == "__main__":
    client_code()
