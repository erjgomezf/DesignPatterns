"""
Cliente que demuestra el uso del patrón Command.
"""
from .application import Application
from .concrete_commands import CopyCommand, CutCommand, PasteCommand


def client_code():
    """
    El código cliente que configura y ejecuta los comandos a través de la aplicación.
    """
    app = Application()

    # El texto inicial del editor está vacío
    print(f"Estado inicial: {app.editor}")

    # --- Operación 1: Pegar (no hace nada porque el portapapeles está vacío) ---
    paste_cmd = PasteCommand(app, app.editor)
    app.set_active_command(paste_cmd)
    app.execute_active_command()
    print(f"Estado actual: {app.editor}")

    # --- Operación 2: Simular una selección y Copiar ---
    # (En una app real, la selección la haría el usuario en la UI)
    app.editor.text = "Hola Mundo"
    print(f"\nEstado actual: {app.editor}")
    copy_cmd = CopyCommand(app, app.editor)
    app.set_active_command(copy_cmd)
    app.execute_active_command()
    print(f"Portapapeles de la App: '{app.clipboard}'")

    # --- Operación 3: Pegar de nuevo ---
    app.set_active_command(paste_cmd)
    app.execute_active_command()
    print(f"Estado actual: {app.editor}")

    # --- Operación 4: Cortar ---
    cut_cmd = CutCommand(app, app.editor)
    app.set_active_command(cut_cmd)
    app.execute_active_command()
    print(f"Estado actual: {app.editor}")
    print(f"Portapapeles de la App: '{app.clipboard}'")

    # --- Operación 5: Deshacer la última operación (Cortar) ---
    app.undo()
    print(f"Estado después de deshacer: {app.editor}")

    # --- Operación 6: Deshacer de nuevo (Pegar) ---
    app.undo()
    print(f"Estado después de deshacer de nuevo: {app.editor}")


if __name__ == "__main__":
    client_code()
