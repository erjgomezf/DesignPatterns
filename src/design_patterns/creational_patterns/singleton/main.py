from threading import Thread
from .database_connection import DatabaseConnection


def client_code_single_thread():
    """
    Demostración del Singleton en un solo hilo.
    """
    print("1. Demostración en un solo hilo:")
    # Se intentan crear dos instancias
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()

    # Se comprueba si son la misma instancia
    if db1 is db2:
        print("   - Correcto: Ambas variables contienen la misma instancia de la base de datos.")
        db1.query("SELECT * FROM users")
        db2.query("SELECT * FROM products")
    else:
        print("   - Error: El patrón Singleton ha fallado; se crearon instancias diferentes.")


def client_code_multi_thread():
    """
    Demostración del Singleton en un entorno multihilo.
    """
    print("\n2. Demostración en un entorno multihilo:")
    print("   - Si el Singleton está bien implementado, solo se debe ver un mensaje de 'Nueva conexión'.")

    threads = []
    for i in range(2):
        thread = Thread(target=DatabaseConnection)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    client_code_single_thread()
    client_code_multi_thread()
