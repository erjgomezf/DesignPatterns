# Patrones de Diseño de Comportamiento (Behavioral Patterns)

Este documento sirve como un resumen y una guía de referencia rápida para los patrones de diseño de comportamiento implementados en este proyecto.

---

## 1. ¿Qué son los Patrones de Comportamiento?

Los patrones de comportamiento se centran en los **algoritmos y la asignación de responsabilidades entre objetos**. No describen solo patrones de objetos o clases, sino también los patrones de comunicación entre ellos. Estos patrones aumentan la flexibilidad en la forma en que los objetos se comunican y colaboran.

---

## 2. Resumen de Patrones

A continuación se detalla el propósito y el caso de uso de cada patrón de comportamiento.

---

### Strategy (Estrategia)
- **Propósito**: Encapsula una familia de algoritmos y los hace intercambiables, permitiendo que el algoritmo varíe independientemente de los clientes que lo utilizan.
- **Cuándo Usarlo**:
    - Cuando tienes múltiples variantes de un algoritmo y quieres que el cliente elija una en tiempo de ejecución.
    - Para eliminar condicionales complejos (`if/elif/else`) que seleccionan un comportamiento.
- **Ventajas**: Permite intercambiar algoritmos en tiempo de ejecución. Aísla la lógica del algoritmo (SRP). Facilita la introducción de nuevas estrategias (OCP).
- **Desventajas**: Aumenta el número de clases si solo tienes unos pocos algoritmos que no cambian.
---

### State (Estado)
- **Propósito**: Permite a un objeto alterar su comportamiento cuando su estado interno cambia. El objeto parecerá cambiar su clase.
- **Cuándo Usarlo**:
    - Para modelar máquinas de estado o flujos de trabajo complejos.
    - Cuando el comportamiento de un objeto depende de su estado y debe cambiar en tiempo de ejecución para evitar condicionales masivos.
- **Ventajas**: Organiza la lógica de estados en clases separadas (SRP). Elimina condicionales masivos. Facilita la adición de nuevos estados (OCP).
- **Desventajas**: Aumenta el número de clases, lo que puede ser excesivo para máquinas de estado simples.
---

### Mediator (Mediador)
- **Propósito**: Centraliza la comunicación compleja entre un grupo de objetos en un único mediador, reduciendo las dependencias directas entre ellos.
- **Cuándo Usarlo**:
    - Para desacoplar un conjunto de objetos que se comunican de forma caótica ("malla de araña").
    - Cuando es difícil reutilizar un objeto porque depende de muchos otros.
- **Ventajas**: Reduce el acoplamiento entre componentes. Centraliza la lógica de interacción, simplificando el mantenimiento.
- **Desventajas**: El mediador puede convertirse en un "God Object" monolítico y complejo si no se diseña con cuidado.
---

### Command (Comando)
- **Propósito**: Encapsula una solicitud o una operación en un objeto independiente.
- **Cuándo Usarlo**:
    - Para implementar operaciones deshacibles (undo/redo).
    - Para poner operaciones en cola, registrarlas o ejecutarlas de forma remota.
    - Para desacoplar el objeto que invoca una operación del que sabe cómo realizarla.
- **Ventajas**: Desacopla el invocador del receptor. Facilita la implementación de colas y operaciones de undo/redo. Permite componer comandos complejos.
- **Desventajas**: Aumenta el número de clases, ya que cada acción requiere una nueva clase de comando.
---

### Observer (Observador)
- **Propósito**: Define una dependencia uno-a-muchos entre objetos. Cuando un objeto (sujeto) cambia de estado, todos sus dependientes (observadores) son notificados y actualizados automáticamente.
- **Cuándo Usarlo**:
    - Cuando cambios en un objeto requieren que otros objetos cambien, pero no quieres un acoplamiento directo.
    - Ideal para sistemas de eventos, notificaciones (UI, apps) y seguimiento de estado.
- **Ventajas**: Desacoplamiento total entre el sujeto y los observadores. Permite añadir o quitar observadores dinámicamente (OCP).
- **Desventajas**: El orden de notificación no está garantizado. Puede llevar a actualizaciones en cascada complejas y difíciles de depurar.
---

### Chain of Responsibility (Cadena de Responsabilidad)
- **Propósito**: Pasa una solicitud a través de una cadena de manejadores. Cada manejador decide si procesa la solicitud o la pasa al siguiente en la cadena.
- **Cuándo Usarlo**:
    - Cuando más de un objeto puede manejar una solicitud y el manejador no se conoce a priori.
    - Para desacoplar al emisor de la solicitud de sus receptores. Ideal para middlewares, filtros o sistemas de aprobación.
- **Ventajas**: Desacopla al emisor de los receptores. Ofrece gran flexibilidad para añadir o reordenar los manejadores en la cadena.
- **Desventajas**: No se garantiza que una solicitud sea manejada. Puede ser difícil de depurar si la cadena es larga.
---

## 3. Tabla Comparativa Rápida

| Patrón | Intención Principal | Foco | Analogía |
| :--- | :--- | :--- | :--- |
| **Strategy** | Encapsular algoritmos intercambiables. | Cómo un objeto realiza una tarea. | Elegir una ruta en un mapa (coche, bici, a pie). |
| **State** | Cambiar el comportamiento de un objeto según su estado. | Qué puede hacer un objeto en su estado actual. | Los botones de un reproductor de música (Play/Pause). |
| **Mediator** | Centralizar la comunicación entre objetos. | Cómo colabora un grupo de objetos. | Torre de control de un aeropuerto. |
| **Command** | Encapsular una acción en un objeto. | Convertir una operación en un objeto portable. | Un pedido en un restaurante. |
| **Observer** | Notificar a múltiples objetos sobre un cambio. | Mantener a los objetos sincronizados. | Suscripción a un canal de YouTube. |
| **Chain of Responsibility** | Pasar una solicitud por una cadena de posibles manejadores. | Desacoplar quién envía de quién recibe. | Línea de soporte técnico con varios niveles. |
---