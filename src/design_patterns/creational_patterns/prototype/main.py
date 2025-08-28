from .shapes import Rectangle, Circle, Shape


class PrototypeRegistry:
    """
    Un registro para almacenar y recuperar prototipos por nombre.
    Esto facilita la gestión de los objetos que se pueden clonar.
    """

    def __init__(self):
        self._prototypes = {}

    def add_prototype(self, name: str, prototype: Shape):
        self._prototypes[name] = prototype

    def get_prototype(self, name: str) -> Shape:
        prototype = self._prototypes.get(name)
        if not prototype:
            raise ValueError(f"Prototype with name '{name}' not found.")
        # Devuelve una copia, no el prototipo original
        return prototype.clone()


def client_code():
    """
    El código cliente que utiliza el registro de prototipos para crear nuevos objetos.
    """
    # 1. Crear y configurar los prototipos iniciales
    print("1. Creando y registrando prototipos iniciales...")
    registry = PrototypeRegistry()

    default_rectangle = Rectangle(x=0, y=0, color="blue", width=100, height=50)
    registry.add_prototype("default_rectangle", default_rectangle)

    default_circle = Circle(x=10, y=10, color="red", radius=25)
    registry.add_prototype("default_circle", default_circle)

    # 2. El cliente ahora puede crear nuevos objetos clonando los prototipos
    print("\n2. Clonando prototipos para crear nuevos objetos...")

    # Crear un nuevo rectángulo a partir del prototipo y modificarlo
    new_rectangle = registry.get_prototype("default_rectangle")
    new_rectangle.x = 150
    new_rectangle.color = "green"

    print(f"   - Prototipo Original: {default_rectangle}")
    print(f"   - Clon Modificado:    {new_rectangle}")
    print(f"   - ¿Son el mismo objeto? {'Sí' if new_rectangle is default_rectangle else 'No'}")


if __name__ == "__main__":
    client_code()
