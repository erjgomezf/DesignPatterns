from .subjects import WeatherStation
from .observers import TemperatureDisplay, FanController


def main():
    """
    Función principal que demuestra el patrón Observer.
    """
    print("--- Demostración del Patrón de Diseño Observer ---\n")

    # 1. Crear el sujeto (el objeto que será observado).
    weather_station = WeatherStation()

    # 2. Crear los observadores.
    temp_display = TemperatureDisplay()
    fan_controller = FanController(threshold=25.0)

    # 3. Adjuntar (suscribir) los observadores al sujeto.
    weather_station.attach(temp_display)
    weather_station.attach(fan_controller)

    # 4. Cambiar el estado del sujeto. Esto debería notificar a todos los observadores.
    print("Cambiando la temperatura a 22°C...")
    weather_station.set_temperature(22.0)

    print("\nCambiando la temperatura a 28°C (el ventilador debería encenderse)...")
    weather_station.set_temperature(28.0)

    # 5. Desadjuntar un observador.
    print("\nQuitando el display de temperatura...")
    weather_station.detach(temp_display)

    print("\nCambiando la temperatura a 24°C (el ventilador debería apagarse, el display no reacciona)...")
    weather_station.set_temperature(24.0)

    print("\n--- Fin de la demostración ---")

if __name__ == "__main__":
    main()