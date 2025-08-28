"""
Cliente que demuestra el uso del patrón Flyweight para renderizar un bosque.
"""
import random
from .tree import Tree
from .tree_factory import TreeFactory


class Forest:
    """
    El código cliente que simula la creación y el dibujo de un bosque.
    """
    def __init__(self):
        self._trees: list[Tree] = []

    def plant_tree(self, x: int, y: int, name: str, color: str, texture: str):
        tree_type = TreeFactory.get_tree_type(name, color, texture)
        tree = Tree(x, y, tree_type)
        self._trees.append(tree)

    def draw(self):
        print("\n--- Dibujando el bosque completo ---")
        for tree in self._trees:
            tree.draw()
        print("-------------------------------------")


if __name__ == "__main__":
    forest = Forest()

    # Plantar miles de árboles de solo unos pocos tipos
    tree_types_to_plant = [
        ("Roble", "Verde Oscuro", "Textura de Roble"),
        ("Pino", "Verde Claro", "Textura de Pino"),
        ("Abedul", "Blanco y Negro", "Textura de Abedul")
    ]

    print("Plantando 10 árboles...")
    for i in range(10):
        ttype = random.choice(tree_types_to_plant)
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        forest.plant_tree(x, y, ttype[0], ttype[1], ttype[2])

    forest.draw()

    # A pesar de haber creado 10 árboles, solo se han instanciado 3 tipos de árbol (flyweights).
    TreeFactory.list_tree_types()

