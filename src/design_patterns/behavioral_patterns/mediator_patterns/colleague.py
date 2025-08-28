"""
El Componente (o Colega) que se comunica a través del Mediador.
"""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .mediator import ChatMediator


class User:
    """
    El Componente (Colega) conoce al mediador pero no a otros colegas.
    """

    def __init__(self, name: str, mediator: ChatMediator):
        self._name = name
        self._mediator = mediator

    @property
    def name(self) -> str:
        return self._name

    def send(self, message: str) -> None:
        print(f"{self.name} envía: '{message}'")
        self._mediator.send_message(message, self)

    def receive(self, message: str, sender_name: str) -> None:
        print(f"[{self.name}] recibió de [{sender_name}]: '{message}'")

