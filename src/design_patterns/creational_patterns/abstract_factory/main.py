import platform
from .gui_factory import GUIFactory, WindowsFactory, MacOSFactory


class Application:
    """
    El código cliente que utiliza la fábrica.
    No le importa la implementación concreta de la fábrica, solo sabe que
    puede crear botones y checkboxes.
    """

    def __init__(self, factory: GUIFactory):
        self.factory = factory
        self.button = None
        self.checkbox = None

    def create_ui(self):
        self.button = self.factory.create_button()
        self.checkbox = self.factory.create_checkbox()

    def paint_ui(self):
        print("Pintando la UI:")
        self.button.paint()
        self.checkbox.paint()


def client_code():
    """
    La aplicación elige el tipo de fábrica dependiendo de la configuración
    actual o del entorno (en este caso, el sistema operativo).
    """
    os_name = platform.system()
    factory = WindowsFactory() if os_name == "Windows" else MacOSFactory()

    app = Application(factory)
    app.create_ui()
    app.paint_ui()


if __name__ == "__main__":
    client_code()
