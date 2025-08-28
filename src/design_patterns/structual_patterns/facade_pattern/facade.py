"""
El módulo Facade que proporciona una interfaz simplificada al complejo subsistema de la casa inteligente.
"""
from .lighting_system import LightingSystem
from .climate_control import ClimateControl
from .security_system import SecuritySystem


class SmartHomeFacade:
    """
    La Fachada (Facade) que simplifica la interacción con los subsistemas de la casa.
    El cliente solo necesita interactuar con esta clase.
    """
    def __init__(self):
        """
        La fachada crea y mantiene las instancias de los subsistemas.
        """
        self._lighting = LightingSystem()
        self._climate = ClimateControl()
        self._security = SecuritySystem()

    def arrive_home(self):
        """
        Orquesta una secuencia de acciones para cuando el usuario llega a casa.
        """
        print("\n--- Usuario llegando a casa... ---")
        self._security.disarm_alarm()
        self._lighting.turn_on("Entrada")
        self._lighting.turn_on("Sala de estar")
        self._climate.set_temperature(22)
        print("----------------------------------\n")

    def leave_home(self):
        """
        Orquesta una secuencia de acciones para cuando el usuario se va de casa.
        """
        print("\n--- Usuario saliendo de casa... ---")
        self._lighting.turn_off("Entrada")
        self._lighting.turn_off("Sala de estar")
        self._climate.turn_off()
        self._security.activate_cameras()
        self._security.arm_alarm()
        print("---------------------------------")
