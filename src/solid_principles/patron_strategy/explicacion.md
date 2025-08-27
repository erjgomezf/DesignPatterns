# Patrón de Diseño: Strategy (Estrategia)

Este documento ofrece una explicación didáctica del patrón **Strategy**, utilizando el código de este proyecto como referencia.

---

## 1. ¿Qué es el Patrón Strategy?

> El **Strategy** es un patrón de diseño de comportamiento que permite definir una familia de algoritmos, encapsular cada uno de ellos en clases separadas y hacer que sus objetos sean intercambiables.

En esencia, el patrón Strategy permite que el algoritmo varíe independientemente del cliente que lo utiliza. Separa el "qué" hace una clase (el contexto) del "cómo" lo hace (la estrategia).

### ¿Qué Problema Resuelve?

Evita el uso de sentencias condicionales complejas (`if/elif/else`) dentro de una clase que necesita realizar una misma acción de diferentes maneras. En lugar de tener un "monolito" que lo hace todo, se delega el comportamiento específico a objetos más pequeños y enfocados.

---

## 2. Componentes del Patrón

Analicemos las piezas clave del patrón y su correspondencia en nuestro código de ejemplo:

| Componente | Rol | Archivo de Ejemplo |
| :--- | :--- | :--- |
| **Strategy (Estrategia)** | Define la interfaz común para todos los algoritmos soportados. Es el "contrato". | `strategies.py` -> `ExportStrategy` |
| **ConcreteStrategy** | Implementación de un algoritmo específico, siguiendo la interfaz `Strategy`. | `strategies.py` -> `JsonExportStrategy`, `CsvExportStrategy`, etc. |
| **Context (Contexto)** | La clase que utiliza una estrategia. Mantiene una referencia a un objeto `Strategy` y se comunica con él a través de su interfaz. | `context.py` -> `ReportGenerator` |

---

## 3. Análisis del Código de Ejemplo

### a. La Interfaz y las Estrategias Concretas: `strategies.py`

Este archivo es el corazón del patrón, donde se definen los algoritmos intercambiables.

- **`ExportStrategy(Protocol)`**: Actúa como la interfaz `Strategy`. Define un contrato claro: cualquier estrategia de exportación **debe** tener un método `export()`.
    > Esto es clave para el **Principio de Inversión de Dependencias (DIP)**: el contexto no dependerá de las clases concretas, sino de esta abstracción.

- **`JsonExportStrategy`, `CsvExportStrategy`, `HtmlExportStrategy`**: Son las `ConcreteStrategy`.
    - Cada una es una clase independiente que cumple con el protocolo `ExportStrategy`.
    - Cada una tiene una **única responsabilidad (SRP)**: formatear datos a JSON, CSV o HTML, respectivamente.

### b. El Contexto: `context.py`

El `ReportGenerator` es el `Contexto`. Utiliza una estrategia, pero es "ignorante" de sus detalles internos.

- **`__init__(self, strategy: ExportStrategy)`**: Aquí ocurre la **Inyección de Dependencias (DI)**. El `ReportGenerator` no crea su propia estrategia, la **recibe** desde fuera. Nota cómo depende de la abstracción `ExportStrategy`, no de una clase concreta.

- **`set_strategy(...)`**: Este método dota al contexto de una gran flexibilidad, permitiendo **cambiar la estrategia en tiempo de ejecución**.

- **`generate_report(...)`**: Aquí se produce la **delegación**. El contexto no implementa la lógica de exportación; simplemente invoca el método `export` de la estrategia que tiene asignada en ese momento (`self._strategy.export(data)`).

### c. El Cliente: `main.py`

El cliente es el responsable de orquestar todo. Es el único que necesita conocer las clases concretas para poder:
1.  Crear instancias de las estrategias que necesita (`JsonExportStrategy`, `CsvExportStrategy`).
2.  Crear la instancia del contexto (`ReportGenerator`).
3.  **Inyectar** la estrategia inicial en el contexto.
4.  Decidir cuándo y por qué cambiar de estrategia usando `set_strategy()`.

---

## 4. Ventajas Principales

- **Cumplimiento del Principio Abierto/Cerrado (OCP):** Puedes introducir nuevas estrategias (ej. `XmlExportStrategy`) sin modificar el código del `ReportGenerator` (el contexto).

- **Separación de Responsabilidades (SRP):** La lógica de negocio de alto nivel (`ReportGenerator`) se separa de los detalles de implementación de los algoritmos (las estrategias).

- **Flexibilidad y Reutilización:** Los algoritmos (estrategias) pueden ser reutilizados por diferentes contextos.

- **Eliminación de Condicionales:** Simplifica el código del contexto, haciéndolo más limpio y fácil de mantener.

---

## 5. Cómo Ejecutar el Ejemplo

Para que las importaciones funcionen, ejecuta el código como un módulo desde el directorio raíz del proyecto.

1.  **Sitúate en la raíz del proyecto:**
    ```bash
    cd /ruta/a/tu/proyecto/DesignPatterns
    ```

2.  **Ejecuta el módulo `main`:**
    ```bash
    python3 -m src.solid_principles.patron_strategy.main
    ```

Esto correrá el `client_code`, que demostrará cómo el `ReportGenerator` puede cambiar su comportamiento de exportación dinámicamente.