"""
Módulo que define una implementación concreta para renderizar como vectores.
"""
from .rendering_engine import RenderingEngine


class VectorRenderer(RenderingEngine):
    """
    Implementación Concreta: Renderiza las formas como gráficos vectoriales.
    """
    def render_circle(self, radius: float) -> None:
        print(f"Renderizando círculo como vectores con radio {radius}")

    def render_square(self, side: float) -> None:
        print(f"Renderizando cuadrado como vectores con lado {side}")
