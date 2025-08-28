"""
Módulo que simula un subsistema de climatización de una casa inteligente.
"""

class ClimateControl:
    """Controla la temperatura de la casa."""

    def set_temperature(self, temp_celsius: int):
        print(f"Climatización: Ajustando temperatura a {temp_celsius}°C.")

    def turn_off(self):
        print("Climatización: Apagando sistema.")
