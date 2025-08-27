from typing import Protocol


class Transport(Protocol):
    """
    La interfaz del Producto declara las operaciones que todos los productos
    concretos deben implementar. En nuestro caso, todos los transportes
    deben poder realizar una entrega.
    """
    def deliver(self) -> str:
        ...

class Truck:
    """Producto Concreto: Camión. Implementa la interfaz Transport."""
    def deliver(self) -> str:
        return "Entrega por tierra en un camión."

class Ship:
    """Producto Concreto: Barco. Implementa la interfaz Transport."""
    def deliver(self) -> str:
        return "Entrega por mar en un barco."
