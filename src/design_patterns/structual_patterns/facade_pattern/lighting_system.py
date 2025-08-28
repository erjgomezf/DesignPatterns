"""
Módulo que simula un subsistema de iluminación de una casa inteligente.
"""

class LightingSystem:
    """Controla las luces de la casa."""

    def turn_on(self, area: str):
        print(f"Iluminación: Encendiendo luces en '{area}'.")

    def turn_off(self, area: str):
        print(f"Iluminación: Apagando luces en '{area}'.")

    def set_brightness(self, area: str, level: int):
        if 0 <= level <= 100:
            print(f"Iluminación: Ajustando brillo en '{area}' al {level}%")
        else:
            print("Iluminación: Nivel de brillo inválido.")
