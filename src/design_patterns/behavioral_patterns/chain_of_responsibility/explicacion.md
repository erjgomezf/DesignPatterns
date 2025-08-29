# Patrón de Diseño: Chain of Responsibility (Cadena de Responsabilidad)

Este documento ofrece una explicación didáctica del patrón **Chain of Responsibility**, utilizando el código de este proyecto como referencia.

---

## 1. ¿Qué es el Patrón Chain of Responsibility?

![Cadena de Responsabilidad](../images/chain_of_responsibility.png)

> El **Chain of Responsibility** es un patrón de diseño de comportamiento que permite pasar solicitudes a lo largo de una cadena de manejadores. Al recibir una solicitud, cada manejador decide si la procesa o si la pasa al siguiente manejador en la cadena.


Imagina una fila de personas donde cada una tiene una tarea específica. Cuando llega un trabajo, la primera persona lo mira. Si puede hacerlo, lo hace. Si no, se lo pasa a la siguiente persona en la fila, y así sucesivamente, hasta que alguien lo maneja o la solicitud llega al final de la fila sin ser procesada.

### ¿Qué Problema Resuelve?

Resuelve el problema de acoplar el emisor de una solicitud con su receptor. En lugar de que el emisor sepa exactamente quién debe manejar la solicitud, simplemente la envía a la cadena, y la cadena se encarga de encontrar al manejador adecuado. Esto permite:

- **Desacoplamiento:** El emisor no necesita conocer la estructura de la cadena ni las clases concretas de los manejadores.
- **Flexibilidad:** Puedes añadir o quitar manejadores, o cambiar el orden de la cadena en tiempo de ejecución, sin afectar al código cliente.
- **Responsabilidad Única (SRP):** Cada manejador tiene una única responsabilidad: intentar procesar la solicitud o pasarla.

---

## 2. Componentes del Patrón

| Componente | Rol | Archivo de Ejemplo |
| :--- | :--- | :--- |
| **Handler (Manejador)** | Interfaz o clase abstracta que declara el método para manejar solicitudes y, opcionalmente, un método para establecer el siguiente manejador en la cadena. | `handlers.py` -> `ApprovalHandler` |
| **ConcreteHandler** | Implementa la interfaz `Handler`. Contiene la lógica para procesar la solicitud y decide si la pasa al siguiente. | `handlers.py` -> `ManagerApprovalHandler`, `DirectorApprovalHandler`, `CEOApprovalHandler` |
| **Client (Cliente)** | Crea la cadena de manejadores y envía solicitudes al primer manejador de la cadena. | `main.py` |

---

## 3. Análisis del Código de Ejemplo

### a. La Solicitud: `request.py`

- **`PurchaseRequest`**: Es una simple `dataclass` que representa la solicitud que se va a procesar. En este caso, contiene un `id` y un `amount`.

### b. Los Manejadores: `handlers.py`

- **`ApprovalHandler(ABC)`**: Es la interfaz `Handler`.
    - Define el método `set_next(handler)` para construir la cadena.
    - Define el método `handle(request)` que cada manejador concreto debe implementar.
    - Incluye una implementación por defecto para `set_next` que permite encadenar manejadores fácilmente.
    - La implementación por defecto de `handle` en la clase base simplemente pasa la solicitud al siguiente manejador si existe. Esto es crucial para la propagación de la cadena.

- **`ManagerApprovalHandler`, `DirectorApprovalHandler`, `CEOApprovalHandler`**: Son los `ConcreteHandler`.
    - Cada uno hereda de `ApprovalHandler`.
    - Implementan su propia lógica en el método `handle()`:
        - Comprueban si pueden manejar la solicitud (basado en el `amount` de la `PurchaseRequest`).
        - Si pueden, la procesan (imprimen un mensaje de aprobación).
        - Si no pueden, llaman a `super().handle(request)` para pasar la solicitud al siguiente manejador en la cadena.

### c. El Cliente: `main.py`

El cliente es el que orquesta la creación y el uso de la cadena.

1.  **Creación de Manejadores:** Se instancian los `ConcreteHandler`.
2.  **Construcción de la Cadena:** Se utiliza el método `set_next()` para vincular los manejadores en un orden específico: `manager -> director -> ceo`.
3.  **Envío de Solicitudes:** Se crean varias `PurchaseRequest` con diferentes montos.
4.  **Inicio de la Cadena:** Cada solicitud se envía al primer manejador de la cadena (`manager.handle(request)`). El cliente no necesita saber quién la aprobará, solo que la cadena se encargará.

---

## 4. Ventajas Principales

- **Desacoplamiento:** El emisor de la solicitud no está acoplado a los receptores concretos.
- **Flexibilidad:** La cadena puede ser modificada dinámicamente (añadir/quitar/reordenar manejadores).
- **Simplificación del Objeto Cliente:** El cliente solo necesita conocer el primer manejador de la cadena.
- **Principio Abierto/Cerrado (OCP):** Puedes añadir nuevos tipos de manejadores sin modificar el código existente de los manejadores o del cliente.

## 5. Cuándo Usar Chain of Responsibility

- Cuando más de un objeto puede manejar una solicitud, y el manejador real no se conoce de antemano.
- Cuando quieres emitir una solicitud a uno de varios objetos sin especificar explícitamente el receptor.
- Cuando el conjunto de objetos que pueden manejar una solicitud debe ser especificado dinámicamente.

---

## 6. Cómo Ejecutar el Ejemplo

Para que las importaciones funcionen, ejecuta el código como un módulo desde el directorio raíz del proyecto.

1.  **Sitúate en la raíz del proyecto:**
    ```bash
    cd /ruta/a/tu/proyecto/DesignPatterns
    ```

2.  **Ejecuta el módulo `main`:**
    ```bash
    python3 -m src.design_patterns.behavioral_patterns.chain_of_responsibility.main
    ```

Esto correrá el `main()`, que demostrará cómo las solicitudes de compra son procesadas por el manejador apropiado en la cadena.