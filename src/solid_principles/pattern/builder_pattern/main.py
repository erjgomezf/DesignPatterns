from .builders import DesktopComputerBuilder
from .director import HardwareDirector


def main():
    """
    Función principal que demuestra el patrón Builder.
    El código cliente puede construir un objeto complejo de varias maneras.
    """
    print("--- Demostración del Patrón de Diseño Builder ---\n")

    # --- Opción 1: Construcción manual sin un Director ---
    # El cliente tiene control total sobre la construcción.
    # Ideal para configuraciones personalizadas.
    print("Construyendo un PC personalizado sin Director:")
    custom_builder = DesktopComputerBuilder()
    custom_pc = (
        custom_builder.build_cpu("AMD Ryzen 7 5800X")
        .build_ram(16)
        .build_storage(1024)
        .build_gpu("AMD Radeon RX 6700 XT")
        .computer
    )
    print(custom_pc)
    print("\n--------------------------------------------------\n")

    # --- Opción 2: Usando un Director para configuraciones predefinidas ---
    # El Director oculta los detalles de construcción al cliente.
    # Ideal para crear objetos estándar.
    director = HardwareDirector()
    
    print("Usando el Director para construir un PC Gaming:")
    gaming_builder = DesktopComputerBuilder()
    director.builder = gaming_builder
    director.build_gaming_pc()
    gaming_pc = gaming_builder.computer
    print(gaming_pc)
    print("\n--------------------------------------------------\n")

    print("Usando el mismo Director para construir un PC de Oficina:")
    office_builder = DesktopComputerBuilder()
    director.builder = office_builder
    director.build_office_pc()
    office_pc = office_builder.computer
    print(office_pc)
    print("\n--- Fin de la demostración ---")


if __name__ == "__main__":
    main()