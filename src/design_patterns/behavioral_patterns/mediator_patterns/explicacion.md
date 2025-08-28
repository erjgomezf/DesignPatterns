# Patrón de Diseño: Mediator (Mediador)

Este documento ofrece una explicación didáctica del patrón **Mediator**, utilizando el código de este proyecto como referencia.

---

## 1. ¿Qué es el Patrón Mediator?

> El **Mediator** es un patrón de diseño de comportamiento que te permite reducir las dependencias caóticas entre objetos. El patrón restringe las comunicaciones directas entre los objetos y los fuerza a colaborar únicamente a través de un objeto mediador.

Imagina una torre de control en un aeropuerto. Los aviones no se comunican directamente entre sí para coordinar despegues y aterrizajes; eso sería un caos. En su lugar, todos se comunican con la torre de control (el mediador), que gestiona el tráfico aéreo. El mediador centraliza la comunicación y la lógica de coordinación.

### ¿Qué Problema Resuelve?

- **Reduce el acoplamiento**: Evita que los objetos se refieran entre sí explícitamente, creando una "malla de araña" de dependencias. Los objetos solo necesitan conocer al mediador.
- **Centraliza la lógica de interacción**: La lógica compleja de cómo colaboran los objetos se traslada al mediador, simplificando los objetos individuales.
- **Facilita la reutilización**: Los objetos individuales (llamados "colegas" o "componentes") son más fáciles de reutilizar porque no dependen de otros colegas.

---

## 2. Componentes del Patrón

| Componente | Rol | Archivo de Ejemplo |
| :--- | :--- | :--- |
| **Mediator (Mediador)** | La interfaz que declara los métodos de comunicación utilizados por los `Colleagues`. | `mediator.py` -> `ChatMediator` |
| **ConcreteMediator** | Implementa la lógica de comunicación y coordina a los objetos `Colleague`. | `concrete_mediator.py` -> `ChatRoom` |
| **Colleague (Colega)** | La interfaz o clase base para los objetos que se comunican. Cada colega tiene una referencia al mediador. | `colleague.py` -> `User` |
| **ConcreteColleague** | Implementa la lógica de un colega individual. Se comunica con otros colegas a través del mediador. | `colleague.py` -> `User` (en este caso, la clase base y la concreta son la misma) |

---

## 3. Análisis del Código de Ejemplo

Nuestro ejemplo simula una sala de chat donde varios usuarios se comunican sin conocerse directamente.

### a. El `Mediator` y los `Colleagues`

- **`ChatMediator(Protocol)`**: Es la interfaz del mediador. Define un método `send_message()` que los usuarios usarán para enviar mensajes.
- **`User`**: Es el `Colleague`.
    - Cada `User` tiene una referencia a un objeto `ChatMediator`.
    - Cuando un usuario quiere enviar un mensaje (`send()`), no lo envía directamente a otro usuario. En su lugar, llama al método `send_message()` del mediador.
    - También tiene un método `receive()` para que el mediador pueda entregarle mensajes.

### b. El `ConcreteMediator`

- **`ChatRoom`**: Es el `ConcreteMediator`.
    - Mantiene una lista de todos los `User` que están en la sala.
    - Cuando se llama a su método `send_message()`, recorre la lista de usuarios y reenvía el mensaje a todos, excepto al remitente original.
    - Centraliza toda la lógica de distribución de mensajes.

### c. El `Client`: `main.py`

- El `client_code` crea el mediador (`ChatRoom`).
- Crea varios colegas (`User`), pasándoles una referencia al mediador en su constructor.
- Registra a los usuarios en la sala de chat.
- Simula la conversación: cuando `user1.send()` es llamado, el `ChatRoom` se encarga de que `user2` y `user3` reciban el mensaje.

---

## 4. Ventajas y Desventajas

### Ventajas

1.  **Desacoplamiento fuerte**: Los colegas pueden variar independientemente del mediador y de otros colegas.
2.  **Principio de Responsabilidad Única (SRP)**: Los colegas se centran en su propia lógica, y el mediador en la lógica de interacción.
3.  **Mantenimiento simplificado**: Es más fácil entender y modificar la lógica de interacción porque está en un solo lugar.

### Desventajas

1.  **El Mediador puede convertirse en un "God Object"**: Si no se diseña con cuidado, el mediador puede volverse muy complejo y monolítico, asumiendo demasiadas responsabilidades.

---

## 5. Cómo Ejecutar el Ejemplo

Para que las importaciones funcionen correctamente, ejecuta el código como un módulo desde el directorio raíz del proyecto.

1.  **Sitúate en la raíz del proyecto:**
    ```bash
    cd /ruta/a/tu/proyecto/DesignPatterns
    ```

2.  **Ejecuta el módulo `main`:**
    ```bash
    python3 -m src.design_patterns.behavioral_patterns.mediator_pattern.main
    ```

