"""
Cliente que demuestra el uso del patrón Proxy.
"""
from .database_service import DatabaseService
from .real_database_service import RealDatabaseService
from .database_proxy import DatabaseProxy


def client_code(service: DatabaseService, query: str):
    """
    El código cliente trabaja con todos los objetos a través de la interfaz
    del servicio de base de datos, ya sea el objeto real o el proxy.
    """
    print(f"\nCliente: Ejecutando la consulta '{query}'...")
    result = service.request_data(query)
    print(f"Cliente: Resultado recibido -> {result}")


if __name__ == "__main__":
    # El objeto real que consume muchos recursos
    real_service = RealDatabaseService()

    # --- Demostración del control de acceso ---
    print("--- Probando con un usuario sin permisos de administrador ---")
    proxy_user = DatabaseProxy(real_service, user_role="user")
    client_code(proxy_user, "SELECT * FROM users")

    # --- Demostración del caching ---
    print("\n--- Probando con un usuario administrador ---")
    proxy_admin = DatabaseProxy(real_service, user_role="admin")

    # La primera llamada es lenta porque va a la base de datos real
    client_code(proxy_admin, "SELECT * FROM products")

    # La segunda llamada es instantánea porque devuelve los datos de la caché
    client_code(proxy_admin, "SELECT * FROM products")

