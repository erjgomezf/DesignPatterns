"""
Cliente que demuestra el uso del patrón Mediator.
"""
from .colleague import User
from .concrete_mediator import ChatRoom


def client_code():
    """
    El código cliente que configura el mediador y los colegas para
    demostrar la comunicación.
    """
    chat_room = ChatRoom()

    user1 = User("Ana", chat_room)
    user2 = User("Beto", chat_room)
    user3 = User("Carlos", chat_room)

    chat_room.add_user(user1)
    chat_room.add_user(user2)
    chat_room.add_user(user3)

    print("\n--- Comienza la conversación ---")
    user1.send("¡Hola a todos!")
    user2.send("Hola Ana, ¿qué tal?")


if __name__ == "__main__":
    client_code()

