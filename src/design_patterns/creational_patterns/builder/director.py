from .builders import ComputerBuilder


class HardwareDirector:
    """
    El Director es responsable de ejecutar los pasos de construcción en una
    secuencia particular. Es útil cuando se producen productos de acuerdo a un
    orden o configuración específica. El Director es opcional, ya que el cliente
    puede controlar los builders directamente.
    """

    def __init__(self) -> None:
        self._builder: ComputerBuilder | None = None

    @property
    def builder(self) -> ComputerBuilder:
        if not self._builder:
            raise ValueError("Builder no está asignado")
        return self._builder

    @builder.setter
    def builder(self, builder: ComputerBuilder) -> None:
        self._builder = builder

    def build_gaming_pc(self) -> None:
        """Construye un PC para gaming de gama alta."""
        self.builder.build_cpu("Intel Core i9").build_ram(32).build_storage(1024).build_gpu("NVIDIA RTX 4080").add_extra("Refrigeración Líquida").add_extra("Caja con RGB")

    def build_office_pc(self) -> None:
        """Construye un PC básico para oficina."""
        self.builder.build_cpu("Intel Core i5").build_ram(16).build_storage(512)