from abc import ABC, abstractmethod
from .product import Computer


class ComputerBuilder(ABC):
    """
    La interfaz Builder (o clase abstracta) declara los pasos de construcción del
    producto que son comunes a todos los tipos de builders.
    """

    @property
    @abstractmethod
    def computer(self) -> Computer:
        ...

    @abstractmethod
    def build_cpu(self, cpu_model: str) -> "ComputerBuilder":
        ...

    @abstractmethod
    def build_ram(self, size_gb: int) -> "ComputerBuilder":
        ...

    @abstractmethod
    def build_storage(self, size_gb: int) -> "ComputerBuilder":
        ...

    @abstractmethod
    def build_gpu(self, gpu_model: str) -> "ComputerBuilder":
        ...

    @abstractmethod
    def add_extra(self, extra: str) -> "ComputerBuilder":
        ...


class DesktopComputerBuilder(ComputerBuilder):
    """
    El ConcreteBuilder sigue la interfaz Builder y proporciona implementaciones
    específicas de los pasos de construcción. Mantiene su propia instancia
    del producto que está construyendo.
    """

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._computer = Computer()

    @property
    def computer(self) -> Computer:
        product = self._computer
        self.reset()
        return product

    def build_cpu(self, cpu_model: str) -> "DesktopComputerBuilder":
        self._computer.cpu = cpu_model
        return self

    def build_ram(self, size_gb: int) -> "DesktopComputerBuilder":
        self._computer.ram_gb = size_gb
        return self

    def build_storage(self, size_gb: int) -> "DesktopComputerBuilder":
        self._computer.storage_gb = size_gb
        return self

    def build_gpu(self, gpu_model: str) -> "DesktopComputerBuilder":
        self._computer.gpu = gpu_model
        return self

    def add_extra(self, extra: str) -> "DesktopComputerBuilder":
        self._computer.extras.append(extra)
        return self