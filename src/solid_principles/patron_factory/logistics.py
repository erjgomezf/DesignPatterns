from abc import ABC, abstractmethod
from .transport import Transport, Truck, Ship


class Logistics(ABC):
    """
    La clase Creadora (Creator) declara el método de fábrica (factory method)
    que debe devolver un objeto de una clase de Producto. Las subclases de
    la Creadora suelen proporcionar la implementación de este método.
    """

    @abstractmethod
    def create_transport(self) -> Transport:
        """
        Este es el método de fábrica. Nótese que el tipo de retorno es la
        interfaz del producto abstracto (`Transport`). Las subclases lo
        implementarán para crear un producto concreto.
        """
        pass

    def plan_delivery(self) -> str:
        """
        El código principal de la Creadora no conoce el producto concreto que
        se creará, sino que trabaja con la interfaz del producto.
        """
        # 1. Llama al método de fábrica para obtener un objeto de producto.
        transport = self.create_transport()

        # 2. Ahora, usa el producto para realizar la operación.
        result = transport.deliver()
        return f"Logística: El código de la creadora acaba de funcionar con el siguiente resultado -> ({result})"


class RoadLogistics(Logistics):
    """Creador Concreto: Anula el método de fábrica para devolver un Camión."""
    def create_transport(self) -> Transport:
        print("RoadLogistics: Creando un nuevo transporte de tipo Camión.")
        return Truck()

class SeaLogistics(Logistics):
    """Creador Concreto: Anula el método de fábrica para devolver un Barco."""
    def create_transport(self) -> Transport:
        print("SeaLogistics: Creando un nuevo transporte de tipo Barco.")
        return Ship()
