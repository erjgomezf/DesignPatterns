"""
Módulo que define una Abstracción Refinada.
"""
from .shape import Shape


class Circle(Shape):
    """
    Una Abstracción Refinada.
    """
    def __init__(self, renderer, radius: float):
        super().__init__(renderer)
        self._radius = radius

    def draw(self) -> None:
        """
        La abstracción delega el trabajo de bajo nivel a la implementación.
        """
        print("Abstracción: Pidiendo al motor de renderizado que dibuje un círculo.")
        self._renderer.render_circle(self._radius)

    def resize(self, factor: float) -> None:
        print(f"Abstracción: Redimensionando el círculo por un factor de {factor}.")
        self._radius *= factor
