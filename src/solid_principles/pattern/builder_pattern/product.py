from dataclasses import dataclass, field
from typing import List


@dataclass
class Computer:
    """
    El Producto: es el objeto complejo que queremos construir.
    En este caso, un ordenador con varias partes. Usamos un dataclass para
    mantenerlo simple y enfocado en los datos.
    """

    cpu: str = "Default CPU"
    ram_gb: int = 8
    storage_gb: int = 256
    gpu: str | None = None
    extras: List[str] = field(default_factory=list)

    def __str__(self) -> str:
        parts = [
            f"CPU: {self.cpu}",
            f"RAM: {self.ram_gb}GB",
            f"Almacenamiento: {self.storage_gb}GB",
        ]
        if self.gpu:
            parts.append(f"GPU: {self.gpu}")
        if self.extras:
            parts.append(f"Extras: {', '.join(self.extras)}")
        return "Configuración del Ordenador:\n" + "\n".join(f"  - {part}" for part in parts)