"""
Módulo que define la interfaz de Comando y el historial de comandos.
"""
from abc import ABC, abstractmethod


class Command(ABC):
    """
    La interfaz de Comando declara un método para ejecutar un comando.
    También puede declarar métodos para deshacer la operación.
    """
    def __init__(self, app, editor):
        self._app = app
        self._editor = editor
        self._backup = None

    @property
    def is_undoable(self) -> bool:
        return True

    def save_backup(self):
        """Guarda el estado del editor antes de cambiarlo."""
        self._backup = self._editor.text

    def undo(self):
        """Restaura el estado del editor."""
        if self._backup is not None:
            self._editor.text = self._backup

    @abstractmethod
    def execute(self) -> bool:
        """
        Ejecuta el comando. Devuelve True si el comando debe guardarse
        en el historial, False en caso contrario.
        """
        pass


class CommandHistory:
    """Mantiene un historial de los comandos ejecutados."""
    def __init__(self):
        self._history: list[Command] = []

    def push(self, command: Command):
        self._history.append(command)

    def pop(self) -> Command | None:
        if self._history:
            return self._history.pop()
        return None
