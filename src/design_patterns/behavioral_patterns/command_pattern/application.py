"""
Módulo que define la aplicación principal, que actúa como Invocador y coordinador.
"""
from .command import Command, CommandHistory
from .editor import Editor


class Application:
    """
    La aplicación principal que configura y coordina todo.
    """
    def __init__(self):
        self.editor = Editor()
        self.history = CommandHistory()
        self.clipboard = ""
        self.active_command: Command | None = None

    def set_active_command(self, command: Command):
        self.active_command = command

    def execute_active_command(self):
        if self.active_command:
            print(f"\nEjecutando el comando activo...")
            if self.active_command.execute():
                self.history.push(self.active_command)
            self.active_command = None

    def undo(self):
        print("\n--- Deshaciendo la última operación ---")
        command_to_undo = self.history.pop()
        if command_to_undo:
            print(f"Deshaciendo un comando...")
            command_to_undo.undo()
        else:
            print("No hay nada que deshacer.")

