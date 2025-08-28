"""
Cliente que demuestra el uso del patrón Composite.
"""
from .simple_graphics import Circle, Square
from .composite_graphic import CompositeGraphic


def client_code():
    """
    El código cliente trabaja con todos los componentes a través de la interfaz base (Graphic).
    Esto le permite tratar a los objetos simples y compuestos de la misma manera.
    """

    # Crear gráficos simples (hojas)
    circle1 = Circle("Círculo 1")
    square1 = Square("Cuadrado 1")
    circle2 = Circle("Círculo 2")

    # Crear un contenedor (compuesto)
    sub_drawing = CompositeGraphic("Sub-Dibujo 1")
    sub_drawing.add(circle1)
    sub_drawing.add(square1)

    # Crear otro contenedor que incluye el primer contenedor
    main_drawing = CompositeGraphic("Dibujo Principal")
    main_drawing.add(sub_drawing)
    main_drawing.add(circle2)

    # El cliente puede ahora dibujar todo el árbol con una sola llamada,
    # sin necesidad de saber la estructura interna exacta.
    print("Dibujando la estructura completa:")
    main_drawing.draw()


if __name__ == "__main__":
    client_code()
