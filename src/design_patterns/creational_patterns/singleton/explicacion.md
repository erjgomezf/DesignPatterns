# Patrón de Diseño: Singleton

Este documento ofrece una explicación didáctica del patrón **Singleton**, utilizando el código de este proyecto como referencia.

---

## 1. ¿Qué es el Patrón Singleton?

> El **Singleton** es un patrón de diseño creacional que garantiza que una clase tenga **una única instancia** y proporciona un punto de acceso global a dicha instancia.

Es como tener una llave maestra para un recurso específico. No importa cuántas veces pidas la llave, siempre recibirás la misma. Esto es útil para objetos que deben coordinar acciones en todo el sistema, como un gestor de configuración, un servicio de logging o una conexión a una base de datos.

### ¿Qué Problema Resuelve?

Resuelve dos problemas a la vez:

1.  **Garantiza una única instancia**: Asegura que no se creen múltiples objetos de una clase que debe ser única (por ejemplo, para no tener múltiples conexiones a una base de datos que consuman recursos innecesariamente).
2.  **Proporciona un punto de acceso global**: Ofrece un lugar único y fácil para acceder a esa instancia desde cualquier parte del código, evitando la necesidad de pasar el objeto como parámetro por todo el sistema.

---

## 2. Componentes del Patrón

El patrón Singleton es bastante simple en su estructura. Su único componente es la propia clase `Singleton`.

| Componente | Rol | Archivo de Ejemplo |
| :--- | :--- | :--- |
| **Singleton** | La clase que se encarga de crear y gestionar su propia instancia única. | `database_connection.py` -> `DatabaseConnection` |

---

## 3. Análisis del Código de Ejemplo

### a. La Clase Singleton: `database_connection.py`

La implementación de `DatabaseConnection` muestra una forma robusta y segura de crear un Singleton en Python.

- **`_instance = None`**: Una variable de clase privada que almacenará la única instancia.
- **`_lock = Lock()`**: Un objeto `Lock` para manejar la concurrencia. Esto es **crucial** para que el Singleton funcione correctamente en aplicaciones con múltiples hilos (multi-threaded).
- **`__new__(cls, ...)`**: Este método especial de Python se invoca *antes* de `__init__` y es el lugar ideal para controlar la creación del objeto.
    1.  Primero, comprueba si `_instance` ya existe. Si es así, la devuelve inmediatamente. Esto es rápido y no requiere bloqueo.
    2.  Si no existe, adquiere un `_lock`. Esto asegura que solo un hilo pueda entrar en el bloque de código crítico a la vez.
    3.  Dentro del bloqueo, vuelve a comprobar si `_instance` existe. ¿Por qué? Porque otro hilo podría haberla creado mientras el hilo actual esperaba el bloqueo. Esto se llama *Double-Checked Locking*.
    4.  Si la instancia aún no existe, la crea (`super().__new__(cls)`) y la asigna a `_instance`.
    5.  Finalmente, devuelve la instancia.
- **`__init__(self)`**: El inicializador se ejecuta cada vez que se llama a `DatabaseConnection()`. Para evitar que la "conexión costosa" se ejecute repetidamente, comprobamos si el objeto ya tiene el atributo `connection_id`. Si no lo tiene, significa que es la primera vez que se inicializa la instancia.

### b. El Cliente: `main.py`

- **`client_code_single_thread`**: Demuestra el comportamiento básico. Crea dos variables, `db1` y `db2`, y luego usa el operador `is` para verificar que apuntan al *mismo objeto en memoria*.
- **`client_code_multi_thread`**: Simula dos hilos que intentan crear una instancia al mismo tiempo. Gracias a la implementación segura con `Lock`, solo se imprimirá una vez el mensaje "Nueva conexión a la base de datos establecida", demostrando que solo se crea una instancia.

---

## 4. Ventajas y Desventajas (¡Importante!)

El Singleton es un patrón poderoso pero también uno de los más criticados. Es fundamental conocer sus pros y contras.

### Ventajas

1.  **Instancia Única Garantizada**: Tienes la certeza absoluta de que solo existe un objeto de esa clase.
2.  **Acceso Global**: Puedes acceder a él desde cualquier parte del código.
3.  **Inicialización Diferida (Lazy Initialization)**: La instancia se crea solo cuando se necesita por primera vez, no al inicio del programa.

### Desventajas

1.  **Viola el Principio de Responsabilidad Única (SRP)**: La clase se encarga de dos cosas: su lógica de negocio y la gestión de su ciclo de vida (asegurar que sea única).
2.  **Oculta Dependencias**: Cuando una clase usa un Singleton, no es obvio a través de su constructor o métodos que depende de él. Esto hace que el código sea más difícil de entender y mantener.
3.  **Dificulta las Pruebas Unitarias**: Las pruebas deben ser independientes. Como el Singleton mantiene un estado global, una prueba podría modificar el Singleton y afectar el resultado de otra prueba. Es difícil "resetear" un Singleton o sustituirlo por un *mock*.
4.  **Problemas en Entornos Multihilo**: Una implementación ingenua del Singleton no es segura para hilos y puede llevar a la creación de múltiples instancias en condiciones de carrera. Nuestro ejemplo resuelve esto con `Lock`.

> **Recomendación**: Antes de usar un Singleton, considera si la **Inyección de Dependencias** podría ser una alternativa más limpia y flexible.

---

## 5. Analogía para Recordar

- **Singleton (El Gobierno):**
  - En un país, solo puede haber un gobierno oficial a la vez.
  - No importa qué ciudadano o ministerio intente "crear" un gobierno, todos deben interactuar con el único gobierno existente.
  - Este gobierno tiene un estado global (leyes, presupuesto) que afecta a todo el país.
  - Cambiar de gobierno es un proceso complejo y controlado, no algo que se pueda hacer a la ligera en diferentes partes del sistema.

---

## 6. Cómo Ejecutar el Ejemplo

Para que las importaciones funcionen, ejecuta el código como un módulo desde el directorio raíz del proyecto.

1.  **Sitúate en la raíz del proyecto:**
    ```bash
    cd /ruta/a/tu/proyecto/DesignPatterns
    ```

2.  **Ejecuta el módulo `main`:**
    ```bash
    python3 -m src.design_patterns.creational_patterns.singleton.main
    ```

Verás en la salida cómo ambas variables apuntan a la misma instancia y cómo, incluso con hilos, solo se crea una conexión.

```
