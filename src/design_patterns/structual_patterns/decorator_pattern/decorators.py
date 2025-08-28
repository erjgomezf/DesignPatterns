from abc import ABC
from .components import Notifier


class BaseNotifierDecorator(Notifier, ABC):
    """
    El Decorador Base (Base Decorator) sigue la misma interfaz que los otros componentes.
    Su propósito principal es definir la interfaz de envoltura para todos
    los decoradores concretos. Mantiene una referencia al objeto que envuelve.
    """

    _wrapped_component: Notifier

    def __init__(self, component: Notifier) -> None:
        self._wrapped_component = component

    def send(self, message: str) -> str:
        """
        El decorador base simplemente delega la llamada al componente envuelto.
        Los comportamientos extra se añadirán en los decoradores concretos.
        """
        return self._wrapped_component.send(message)


class SMSNotifierDecorator(BaseNotifierDecorator):
    """
    Los Decoradores Concretos (Concrete Decorators) definen comportamientos adicionales
    que se pueden añadir a los componentes dinámicamente. Sobrescriben métodos del
    decorador base y ejecutan su comportamiento antes o después de llamar
    al método del objeto envuelto.
    """

    def send(self, message: str) -> str:
        """
        Añade la funcionalidad de enviar un SMS y LUEGO llama al método
        del componente envuelto (que podría ser otro decorador o el componente base).
        """
        sms_notification = f"Notificación por SMS: '{message}'"
        original_result = super().send(message)
        return f"{sms_notification}\n{original_result}"


class SlackNotifierDecorator(BaseNotifierDecorator):
    """Otro Decorador Concreto que añade notificación por Slack."""

    def send(self, message: str) -> str:
        slack_notification = f"Notificación por Slack: '{message}'"
        original_result = super().send(message)
        return f"{slack_notification}\n{original_result}"