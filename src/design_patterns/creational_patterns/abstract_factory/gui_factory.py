from abc import ABC, abstractmethod

# --- Paso 1: Definir las interfaces de los Productos Abstractos ---
# Cada producto distinto en una familia de productos debe tener una interfaz base.


class Button(ABC):
    """Interfaz para un botón."""

    @abstractmethod
    def paint(self):
        pass


class Checkbox(ABC):
    """Interfaz para un checkbox."""

    @abstractmethod
    def paint(self):
        pass


# --- Paso 2: Definir la Fábrica Abstracta ---
# La interfaz de la Fábrica Abstracta declara un conjunto de métodos para crear
# cada uno de los productos abstractos.


class GUIFactory(ABC):
    """La fábrica abstracta sabe cómo crear todos los productos abstractos."""

    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


# --- Paso 3: Crear los Productos Concretos ---
# Para cada variante de una familia de productos, creamos clases de productos concretos.


class WindowsButton(Button):
    def paint(self):
        print("Renderizando un botón estilo Windows.")


class WindowsCheckbox(Checkbox):
    def paint(self):
        print("Renderizando un checkbox estilo Windows.")


class MacOSButton(Button):
    def paint(self):
        print("Renderizando un botón estilo macOS.")


class MacOSCheckbox(Checkbox):
    def paint(self):
        print("Renderizando un checkbox estilo macOS.")


# --- Paso 4: Crear las Fábricas Concretas ---
# Cada fábrica concreta implementa los métodos de creación de la fábrica abstracta
# para producir una familia específica de productos.


class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


class MacOSFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacOSButton()

    def create_checkbox(self) -> Checkbox:
        return MacOSCheckbox()
