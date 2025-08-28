"""
Módulo que define una implementación concreta para renderizar como píxeles (raster).
"""
from .rendering_engine import RenderingEngine


class RasterRenderer(RenderingEngine):
    """
    Implementación Concreta: Renderiza las formas como un mapa de bits (píxeles).
    """
    def render_circle(self, radius: float) -> None:
        print(f"Renderizando círculo como píxeles con radio {radius}")

    def render_square(self, side: float) -> None:
        print(f"Renderizando cuadrado como píxeles con lado {side}")
