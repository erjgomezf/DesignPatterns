"""
Cliente que demuestra el uso del patrón Facade para interactuar con la casa inteligente.
"""
from .facade import SmartHomeFacade


def client_code():
    """
    El código cliente que solo necesita conocer la fachada simplificada.
    """
    # El cliente no necesita saber sobre LightingSystem, ClimateControl, etc.
    # Solo interactúa con la fachada.
    home = SmartHomeFacade()

    # Realiza acciones complejas con llamadas a métodos simples.
    home.arrive_home()
    home.leave_home()


if __name__ == "__main__":
    client_code()
