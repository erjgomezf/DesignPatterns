"""
Implementación concreta del Mediador.
"""
from typing import List

from .colleague import User
from .mediator import ChatMediator


class ChatRoom(ChatMediator):
    """
    El Mediador Concreto. Orquesta la comunicación entre los usuarios (colegas).
    """

    def __init__(self):
        self._users: List[User] = []

    def add_user(self, user: User) -> None:
        print(f"ChatRoom: {user.name} se ha unido a la sala.")
        self._users.append(user)

    def send_message(self, message: str, sender: User) -> None:
        for user in self._users:
            if user is not sender:
                user.receive(message, sender.name)

