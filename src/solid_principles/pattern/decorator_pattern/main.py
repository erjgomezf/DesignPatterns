from .components import Notifier, EmailNotifier
from .decorators import SMSNotifierDecorator, SlackNotifierDecorator


def client_code(component: Notifier, message: str) -> None:
    """
    El código cliente funciona con todos los objetos usando la interfaz Componente.
    De esta manera, no depende de las clases concretas de los componentes
    con los que trabaja. Puede tratar de la misma forma a un objeto simple
    o a uno decorado.
    """
    print("CLIENTE: He recibido un componente y voy a enviar una notificación.")
    result = component.send(message)
    print("\n--- RESULTADO ---")
    print(result)
    print("-----------------\n")


def main():
    """
    Función principal que demuestra el patrón Decorator.
    """
    print("--- Demostración del Patrón de Diseño Decorator ---\n")

    message = "¡Tu pedido ha sido enviado!"

    # El cliente puede trabajar con un componente simple.
    simple_notifier = EmailNotifier()
    print("Cliente: Tengo un componente simple (EmailNotifier):")
    client_code(simple_notifier, message)

    # ...así como con componentes decorados.
    # Nótese cómo los decoradores pueden envolver no solo componentes simples,
    # sino también otros decoradores (apilamiento).
    print("Cliente: Ahora tengo un componente decorado (Email + SMS).")
    decorator1 = SMSNotifierDecorator(simple_notifier)
    client_code(decorator1, message)

    print("Cliente: Y ahora tengo un componente con doble decoración (Email + SMS + Slack).")
    decorator2 = SlackNotifierDecorator(decorator1)
    client_code(decorator2, message)

    print("--- Fin de la demostración ---")


if __name__ == "__main__":
    main()