"""
Módulo que define los comandos concretos.
"""
from .command import Command


class CopyCommand(Command):
    """Comando para copiar texto. No es deshacible."""
    @property
    def is_undoable(self) -> bool:
        return False

    def execute(self) -> bool:
        print("Comando Copiar: Ejecutando...")
        self._app.clipboard = self._editor.get_selection()
        return False  # No se guarda en el historial


class CutCommand(Command):
    """Comando para cortar texto. Es deshacible."""
    def execute(self) -> bool:
        print("Comando Cortar: Ejecutando...")
        self.save_backup()
        self._app.clipboard = self._editor.get_selection()
        self._editor.delete_selection()
        self._editor.text = ""
        return True  # Se guarda en el historial


class PasteCommand(Command):
    """Comando para pegar texto. Es deshacible."""
    def execute(self) -> bool:
        print("Comando Pegar: Ejecutando...")
        self.save_backup()
        self._editor.text += self._app.clipboard
        return True  # Se guarda en el historial