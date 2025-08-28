# Patrón de Diseño: Builder (Constructor)

Este documento ofrece una explicación didáctica del patrón **Builder**, utilizando el código de este proyecto como referencia.

---

## 1. ¿Qué es el Patrón Builder?

> El **Builder** es un patrón de diseño creacional que permite construir objetos complejos paso a paso. El patrón separa el proceso de construcción de un objeto de su representación final, de modo que el mismo proceso de construcción pueda crear diferentes representaciones.

Imagina un objeto que requiere muchos parámetros en su constructor, algunos de los cuales son opcionales. Un constructor con una larga lista de argumentos es propenso a errores. El patrón Builder resuelve esto proporcionando una API fluida y legible para construir el objeto.

### ¿Qué Problema Resuelve?

- **Constructores "Telescópicos":** Evita la necesidad de tener múltiples constructores con diferentes combinaciones de parámetros.
- **Complejidad en la Creación:** Simplifica la creación de objetos complejos que requieren una configuración detallada.
- **Inmutabilidad:** Facilita la creación de objetos inmutables, ya que el objeto final se construye y se entrega de una sola vez.

---

## 2. Componentes del Patrón

| Componente | Rol | Archivo de Ejemplo |
| :--- | :--- | :--- |
| **Product (Producto)** | El objeto complejo que se está construyendo. | `product.py` -> `Computer` |
| **Builder (Constructor)** | Interfaz o clase abstracta que define los pasos para construir el `Product`. | `builders.py` -> `ComputerBuilder` |
| **ConcreteBuilder** | Implementación del `Builder`. Construye y ensambla las partes del producto. Mantiene una referencia al producto que crea. | `builders.py` -> `DesktopComputerBuilder` |
| **Director (Director)** | (Opcional) Orquesta la construcción utilizando un objeto `Builder`. Define secuencias de construcción predefinidas. | `director.py` -> `HardwareDirector` |

---

## 3. Análisis del Código de Ejemplo

### a. El Producto: `product.py`

- **`Computer`**: Es el `Product`. Un `dataclass` que representa el objeto complejo que queremos crear. Tiene varios atributos como `cpu`, `ram`, `gpu`, etc.

### b. El Builder: `builders.py`

- **`ComputerBuilder(ABC)`**: Es la interfaz `Builder`. Define todos los posibles pasos para construir un ordenador (`build_cpu`, `build_ram`, etc.).

- **`DesktopComputerBuilder`**: Es el `ConcreteBuilder`.
    - **`reset()`**: Crea una nueva instancia vacía del producto (`Computer`).
    - **Métodos `build_...()`**: Cada uno de estos métodos configura una parte del `_computer`.
    - **Interfaz Fluida (Fluent Interface)**: Cada método `build_...()` devuelve `self`. Esto permite encadenar llamadas de una manera muy legible: `builder.build_cpu(...).build_ram(...)`.
    - **`computer` (propiedad)**: Este método es crucial. Devuelve el objeto `Computer` terminado y **reinicia el builder** para que esté listo para construir un nuevo objeto.

### c. El Director: `director.py`

- **`HardwareDirector`**: Es el `Director`. Su rol es opcional pero muy útil.
    - Encapsula la lógica para construir configuraciones específicas y reutilizables (como `build_gaming_pc` o `build_office_pc`).
    - El cliente solo necesita decirle al director qué "receta" usar, y el director se encarga de llamar a los métodos del builder en el orden correcto.
    - Esto desacopla al cliente de los detalles de construcción. El cliente no necesita saber qué componentes lleva un "PC Gaming".

### d. El Cliente: `main.py`

El `main.py` muestra las dos formas de usar el patrón:

1.  **Sin Director (Construcción Manual):** El cliente toma el control total. Crea una instancia de `DesktopComputerBuilder` y llama a los métodos de construcción paso a paso. Esto ofrece máxima flexibilidad para crear configuraciones personalizadas.

    ```python
    custom_pc = custom_builder.build_cpu(...) \
                              .build_ram(...) \
                              .get_computer()
    ```

2.  **Con Director (Construcción Dirigida):** El cliente delega la construcción. Crea un `Builder`, se lo pasa a un `Director`, y le pide al director que construya una configuración predefinida. Luego, le pide el resultado final al `Builder`.

    ```python
    director.builder = gaming_builder
    director.build_gaming_pc()
    gaming_pc = gaming_builder.computer
    ```

---

## 4. Ventajas Principales

- **Separación de Responsabilidades (SRP):** La lógica de construcción se aísla del objeto final y del cliente.
- **Legibilidad y Claridad:** La construcción de objetos complejos se vuelve mucho más fácil de leer y entender.
- **Flexibilidad:** El mismo proceso de construcción (`Director`) puede crear diferentes representaciones de objetos usando diferentes `Builders`.
- **Control sobre la Construcción:** Permite construir el objeto paso a paso, validando cada etapa si es necesario.

## 5. Builder vs. Factory

- **Factory:** Se enfoca en la creación de objetos en un solo paso. Es ideal cuando el proceso de creación no es muy complejo. Devuelve el producto directamente.
- **Builder:** Se enfoca en la construcción de objetos complejos paso a paso. Es ideal cuando el objeto tiene muchas partes configurables. El builder no devuelve el producto directamente; se le pide el resultado final.

---

## 6. Cómo Ejecutar el Ejemplo

Para que las importaciones funcionen, ejecuta el código como un módulo desde el directorio raíz del proyecto.

1.  **Sitúate en la raíz del proyecto:**
    ```bash
    cd /ruta/a/tu/proyecto/DesignPatterns
    ```

2.  **Ejecuta el módulo `main`:**
    ```bash
    python3 -m src.solid_principles.pattern.builder_pattern.main
    ```

Esto correrá el `main()`, que demostrará cómo construir diferentes configuraciones de ordenadores de forma flexible y legible.