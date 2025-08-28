"""
La interfaz del Mediador que define el método de comunicación.
"""
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from .colleague import User


class ChatMediator(Protocol):
    """
    La interfaz del Mediador declara un método utilizado por los componentes
    para notificar al mediador sobre diversos eventos.
    """

    def send_message(self, message: str, sender: User) -> None:
        ...

