"""
Cliente que demuestra el uso del patrón Bridge.
"""
from .vector_renderer import VectorRenderer
from .raster_renderer import RasterRenderer
from .circle import Circle
from .square import Square


def client_code():
    """
    El código cliente puede ahora combinar cualquier abstracción (forma)
    con cualquier implementación (motor de renderizado).
    """

    # Crear los motores de renderizado (Implementaciones)
    vector_renderer = VectorRenderer()
    raster_renderer = RasterRenderer()

    # --- Usar el motor de renderizado vectorial ---
    print("--- Creando formas con Renderizado Vectorial ---")
    circle_vector = Circle(vector_renderer, 5)
    square_vector = Square(vector_renderer, 10)

    circle_vector.draw()
    square_vector.draw()

    circle_vector.resize(1.5)
    circle_vector.draw()
    print("------------------------------------------------\n")

    # --- Usar el motor de renderizado raster ---
    print("--- Creando formas con Renderizado Raster ---")
    circle_raster = Circle(raster_renderer, 5)
    square_raster = Square(raster_renderer, 10)

    circle_raster.draw()
    square_raster.draw()

    square_raster.resize(0.5)
    square_raster.draw()
    print("---------------------------------------------")


if __name__ == "__main__":
    client_code()
