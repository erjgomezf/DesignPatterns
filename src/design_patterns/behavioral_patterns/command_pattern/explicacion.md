# Patrón de Diseño: Command (Comando)

Este documento ofrece una explicación didáctica del patrón **Command**, utilizando el código de este proyecto como referencia.

---

## 1. ¿Qué es el Patrón Command?

> El **Command** es un patrón de diseño de comportamiento que convierte una solicitud en un **objeto independiente** que contiene toda la información sobre la solicitud. Esta transformación te permite parametrizar métodos con diferentes solicitudes, retrasar o poner en cola la ejecución de una solicitud y soportar operaciones que se pueden deshacer.

Imagina que estás en un restaurante. El cliente (tú) no va a la cocina a preparar la comida. En su lugar, le das una orden (un "comando") al camarero. El camarero toma la orden, la anota en un ticket (el objeto `Command`) y la pone en una cola en la cocina. El cocinero (el "receptor") recoge el ticket y ejecuta la orden. El ticket es un objeto que encapsula la solicitud, separando a quien la pide (cliente) de quien la ejecuta (cocinero).

### ¿Qué Problema Resuelve?

- **Desacopla el emisor de la solicitud del receptor**: El objeto que invoca la operación no necesita saber nada sobre quién la va a realizar ni cómo se va a realizar.
- **Permite operaciones deshacibles (Undo/Redo)**: Al encapsular la operación en un objeto, podemos guardar el estado anterior y revertir la operación.
- **Permite la creación de colas y logs de comandos**: Puedes almacenar comandos en una lista, ejecutarlos más tarde, guardarlos en un log, etc.
- **Parametrización de la interfaz de usuario**: Los botones o menús de una UI no necesitan implementar la lógica ellos mismos. Simplemente se les asigna un objeto `Command` y lo ejecutan.

---

## 2. Componentes del Patrón

| Componente | Rol | Archivo de Ejemplo |
| :--- | :--- | :--- |
| **Command (Comando)** | La interfaz que declara un método para la ejecución (`execute`) y opcionalmente para deshacer (`undo`). | `command.py` -> `Command` |
| **ConcreteCommand** | Implementa la interfaz `Command` y vincula a un `Receiver` con una acción. | `concrete_commands.py` -> `CopyCommand`, `CutCommand`, `PasteCommand` |
| **Receiver (Receptor)** | El objeto que contiene la lógica de negocio real y sabe cómo realizar las operaciones. | `editor.py` -> `Editor` |
| **Invoker (Invocador)** | El objeto que pide al comando que ejecute la solicitud. | `application.py` -> `Application` |
| **Client (Cliente)** | Crea los objetos `ConcreteCommand` y los configura con sus `Receivers`. | `main.py` -> `client_code` |

---

## 3. Análisis del Código de Ejemplo

Nuestro ejemplo simula una aplicación de edición de texto con funciones de copiar, cortar, pegar y deshacer.

### a. El `Receiver`: `editor.py`

- **`Editor`**: Contiene la lógica de negocio. Tiene atributos como `text` y `clipboard` y métodos para manipularlos. No sabe nada sobre comandos, solo ejecuta acciones.

### b. La Interfaz `Command`: `command.py`

- **`Command(ABC)`**: Define la interfaz para todos los comandos. Requiere un método `execute()`.
- Incluye lógica para `save_backup()` y `undo()`, que permite a los comandos que modifican el estado del editor guardar una copia de seguridad y restaurarla.

### c. Los `ConcreteCommand`: `concrete_commands.py`

- **`CopyCommand`, `CutCommand`, `PasteCommand`**: Cada uno implementa el método `execute()`.
    - `CopyCommand` llama a la lógica del `Editor` para poner texto en el portapapeles. No es deshacible.
    - `CutCommand` y `PasteCommand` primero llaman a `save_backup()` y luego ejecutan su lógica. Devuelven `True` para indicar que deben ser guardados en el historial para poder deshacerse.

### d. El `Invoker`: `application.py`

- **`Application`**: Actúa como el invocador central.
    1.  **Mantiene el historial**: Tiene una instancia de `CommandHistory`.
    2.  **Ejecuta comandos**: El método `execute_active_command()` llama al `execute()` del comando actual. Si el comando devuelve `True`, lo añade al historial.
    3.  **Gestiona el Undo**: El método `undo()` saca el último comando del historial y llama a su método `undo()`, revirtiendo la operación.

### e. El `Client`: `main.py`

- El `client_code` configura la aplicación, crea instancias de los comandos y se los pasa a la aplicación para su ejecución. Demuestra cómo el estado del editor cambia y cómo la función de deshacer revierte esos cambios paso a paso.

---

## 4. Ventajas y Desventajas

### Ventajas

1.  **Principio de Responsabilidad Única (SRP)**: Las clases que invocan operaciones están separadas de las que las realizan.
2.  **Principio de Abierto/Cerrado (OCP)**: Puedes introducir nuevos comandos en la aplicación sin romper el código existente.
3.  **Implementación de Undo/Redo**: El patrón proporciona una forma sencilla de implementar estas funcionalidades.
4.  **Desacoplamiento**: El invocador está completamente desacoplado del receptor.

### Desventajas

1.  **Aumento de la Complejidad**: Introduce muchas clases nuevas, lo que puede ser excesivo para aplicaciones con pocas operaciones.

---

## 5. Command vs. Strategy

Ambos patrones pueden parecer similares, pero su intención es diferente.

| Patrón | Intención | ¿Cuándo se usa? |
| :--- | :--- | :--- |
| **Command** | **Encapsular una acción** en un objeto. | Para implementar operaciones deshacibles, colas de tareas o parametrizar objetos con una acción. |
| **Strategy** | **Encapsular un algoritmo** en un objeto. | Para permitir que un algoritmo varíe independientemente de los clientes que lo utilizan. Se enfoca en *cómo* se hace algo. |

En resumen: usa **Command** para convertir una operación en un objeto que puedes pasar, almacenar y ejecutar. Usa **Strategy** para tener diferentes formas de hacer la misma cosa y poder intercambiarlas.

---

## 6. Cómo Ejecutar el Ejemplo

Para que las importaciones funcionen correctamente, ejecuta el código como un módulo desde el directorio raíz del proyecto.

1.  **Sitúate en la raíz del proyecto:**
    ```bash
    cd /ruta/a/tu/proyecto/DesignPatterns
    ```

2.  **Ejecuta el módulo `main`:**
    ```bash
    python3 -m src.design_patterns.behavioral_patterns.command_pattern.main
    ```

La salida mostrará el estado del editor a medida que se ejecutan los comandos y cómo la función `undo` restaura los estados anteriores, demostrando el poder y la flexibilidad del patrón.
