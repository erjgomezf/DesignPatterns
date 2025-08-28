"""
Módulo que define la fábrica de Flyweights.
"""
from typing import Dict, List
from .tree_type import TreeType


class TreeFactory:
    """
    La fábrica de Flyweights crea y gestiona los objetos Flyweight.
    Asegura que los flyweights se compartan correctamente.
    """
    _tree_types: Dict[str, TreeType] = {}

    @classmethod
    def get_key(cls, name: str, color: str, texture: str) -> str:
        """Genera una clave para un tipo de árbol dado."""
        return f"{name}_{color}_{texture}"

    @classmethod
    def get_tree_type(cls, name: str, color: str, texture: str) -> TreeType:
        """
        Devuelve un Flyweight existente con un nombre, color y textura dados,
        o crea uno nuevo si no existe.
        """
        key = cls.get_key(name, color, texture)
        if key not in cls._tree_types:
            print("TreeFactory: No se encontró un tipo de árbol, creando uno nuevo.")
            cls._tree_types[key] = TreeType(name, color, texture)
        else:
            print("TreeFactory: Reutilizando un tipo de árbol existente.")
        
        return cls._tree_types[key]

    @classmethod
    def list_tree_types(cls) -> None:
        """Muestra la cantidad de flyweights creados."""
        print(f"\nTreeFactory: Tenemos {len(cls._tree_types)} tipos de árboles (flyweights) en total.")
        for key in cls._tree_types:
            print(f"  - {key}")

