"""
Módulo que define otra Abstracción Refinada.
"""
from .shape import Shape


class Square(Shape):
    """
    Otra Abstracción Refinada.
    """
    def __init__(self, renderer, side: float):
        super().__init__(renderer)
        self._side = side

    def draw(self) -> None:
        """
        La abstracción delega el trabajo de bajo nivel a la implementación.
        """
        print("Abstracción: Pidiendo al motor de renderizado que dibuje un cuadrado.")
        self._renderer.render_square(self._side)

    def resize(self, factor: float) -> None:
        print(f"Abstracción: Redimensionando el cuadrado por un factor de {factor}.")
        self._side *= factor
