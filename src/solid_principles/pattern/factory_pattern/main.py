from .logistics import Logistics, RoadLogistics, SeaLogistics


def client_code(creator: Logistics) -> None:
    """
    El código cliente funciona con una instancia de un creador concreto,
    aunque a través de su interfaz base (Logistics). Mientras el cliente siga
    trabajando con el creador a través de la interfaz base, puedes pasarle
    cualquier subclase de creador sin que el cliente se entere.
    """
    print(f"Cliente: No conozco la clase del creador, pero sé que funciona.")
    print(creator.plan_delivery(), end="\n\n")


def main():
    """
    La aplicación elige el tipo de creador dependiendo de la configuración o
    el entorno, y el cliente se adapta sin cambios.
    """
    print("--- Demostración del Patrón de Diseño Factory Method ---\n")

    print("App: Lanzada con RoadLogistics.")
    client_code(RoadLogistics())

    print("App: Lanzada con SeaLogistics.")
    client_code(SeaLogistics())

if __name__ == "__main__":
    main()
