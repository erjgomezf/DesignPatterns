from typing import Protocol


class Notifier(Protocol):
    """
    La interfaz Componente (Component) declara una operación que todos los componentes
    concretos y decoradores deben implementar. En nuestro caso, es enviar un mensaje.
    """

    def send(self, message: str) -> str:
        ...


class EmailNotifier:
    """
    El Componente Concreto (Concrete Component) es la clase base de los objetos que vamos a decorar.
    Define el comportamiento básico que puede ser alterado por los decoradores.
    """

    def send(self, message: str) -> str:
        return f"Notificación por Email: '{message}'"