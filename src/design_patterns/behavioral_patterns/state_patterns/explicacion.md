# Patrón de Diseño: State (Estado)

Este documento ofrece una explicación didáctica del patrón **State**, utilizando el código de este proyecto como referencia.

---

## 1. ¿Qué es el Patrón State?

> El **State** es un patrón de diseño de comportamiento que permite a un objeto alterar su comportamiento cuando su estado interno cambia. El objeto parecerá cambiar su clase.

Imagina un reproductor de música. Los botones "Play" y "Pause" hacen cosas diferentes dependiendo del estado actual del reproductor (si está sonando, pausado o detenido). En lugar de tener un método `handle_click()` con muchos `if` sobre el estado, el patrón State sugiere crear clases separadas para cada estado (`PlayingState`, `PausedState`) y delegar la lógica a la clase del estado actual.

### ¿Qué Problema Resuelve?

- **Evita condicionales masivos**: Limpia el código de clases que tienen métodos enormes cuyo comportamiento depende del estado del objeto.
- **Organiza la lógica de estados**: Agrupa el comportamiento relacionado con un estado particular en una sola clase.
- **Cumple el Principio de Responsabilidad Única (SRP)**: La lógica de cada estado está en su propia clase.
- **Cumple el Principio de Abierto/Cerrado (OCP)**: Puedes añadir nuevos estados sin cambiar las clases de estado existentes o la clase de contexto.

---

## 2. Componentes del Patrón

| Componente | Rol | Archivo de Ejemplo |
| :--- | :--- | :--- |
| **Context (Contexto)** | La clase cuyo comportamiento cambia con el estado. Mantiene una referencia al objeto de estado actual. | `document.py` -> `Document` |
| **State (Estado)** | La interfaz que encapsula el comportamiento asociado con un estado particular del `Context`. | `document_state.py` -> `DocumentState` |
| **ConcreteState** | Implementa el comportamiento específico de un estado. Es responsable de las transiciones de estado. | `concrete_states.py` -> `DraftState`, `ModerationState`, `PublishedState` |

---

## 3. Análisis del Código de Ejemplo

Nuestro ejemplo modela el flujo de trabajo de un documento que puede estar en estado `Borrador`, `Moderación` o `Publicado`.

### a. El `Context` y la Interfaz `State`

- **`Document`**: Es el `Context`.
    - No contiene ninguna lógica sobre los estados.
    - Mantiene una referencia `_state` al objeto de estado actual.
    - Delega todas las acciones (`request_review`, `publish`) al objeto `_state`.
    - Proporciona un método `transition_to()` que permite a los estados cambiar el estado actual del documento.

- **`DocumentState(ABC)`**: Es la interfaz `State`.
    - Declara los métodos que cada estado concreto debe implementar.
    - Mantiene una referencia de vuelta al `Document` para poder acceder a sus datos y cambiar su estado.

### b. Los `ConcreteState`

- **`DraftState`, `ModerationState`, `PublishedState`**: Son los `ConcreteState`.
    - Cada clase implementa los métodos de la interfaz `State` con la lógica que corresponde a ese estado.
    - Por ejemplo, `DraftState.publish()` no hace nada y muestra un mensaje, pero `DraftState.request_review()` cambia el estado del documento a `ModerationState`.
    - Las transiciones de estado están controladas dentro de las propias clases de estado, lo que mantiene la lógica encapsulada.

### c. El `Client`: `main.py`

- El `client_code` crea un `Document` con un estado inicial (`DraftState`).
- Interactúa con el documento a través de su interfaz pública (`request_review`, `publish`).
- El cliente no sabe (ni le importa) qué clase de estado concreta está manejando la solicitud. Solo ve que el comportamiento del objeto `Document` cambia.

---

## 4. Ventajas y Desventajas

### Ventajas

1.  **Código más limpio y organizado**: Elimina la necesidad de grandes condicionales.
2.  **Lógica de estado cohesiva**: Todo el comportamiento de un estado está en un solo lugar.
3.  **Transiciones de estado explícitas**: Facilita el entendimiento del flujo de trabajo.

### Desventajas

1.  **Aumento del número de clases**: Puede ser excesivo si los estados son pocos y la lógica es simple.

---

## 5. Cómo Ejecutar el Ejemplo

Para que las importaciones funcionen correctamente, ejecuta el código como un módulo desde el directorio raíz del proyecto.

1.  **Sitúate en la raíz del proyecto:**
    ```bash
    cd /ruta/a/tu/proyecto/DesignPatterns
    ```

2.  **Ejecuta el módulo `main`:**
    ```bash
    python3 -m src.design_patterns.behavioral_patterns.state_pattern.main
    ```

