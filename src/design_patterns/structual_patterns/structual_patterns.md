s# Patrones de Diseño Estructurales

Este documento ofrece un resumen y una comparación de los patrones de diseño estructurales, explicando cómo ensamblan objetos y clases en estructuras más grandes, manteniendo al mismo tiempo estas estructuras flexibles y eficientes.

---

## ¿Qué son los Patrones Estructurales?

Los **patrones estructurales** se centran en cómo las clases y los objetos se componen para formar estructuras más grandes. Simplifican el diseño identificando formas sencillas de realizar relaciones entre entidades. Mientras que los patrones creacionales se ocupan de la *creación* de objetos, los estructurales se ocupan de su *composición*.

**Ventaja principal:** Ayudan a garantizar que cuando una parte de un sistema cambia, el sistema entero no necesita hacerlo. Promueven la flexibilidad y la eficiencia en la arquitectura del software.

A continuación, se resumen los patrones estructurales cubiertos en este proyecto.

---

## 2. Resumen de Patrones Estructurales

---

### Adapter (Adaptador)
- **Propósito**: Permite que interfaces incompatibles trabajen juntas.
- **Cuándo Usarlo**: Para integrar una clase existente (legado, terceros) cuya interfaz no coincide con la que el cliente espera, sin modificar el código fuente original.
- **Ventajas**: Separa la lógica de conversión (SRP). Permite introducir nuevos adaptadores sin cambiar el cliente (OCP).
- **Desventajas**: Aumenta la complejidad al introducir una nueva clase.

---

### Bridge (Puente)
- **Propósito**: Desacopla una abstracción de su implementación para que ambas puedan evolucionar de forma independiente.
- **Cuándo Usarlo**: Para evitar una "explosión de clases" cuando se tienen múltiples dimensiones de variación (ej. formas y motores de renderizado).
- **Ventajas**: Flexibilidad y extensibilidad al separar jerarquías. Desacoplamiento fuerte. Lógica de alto y bajo nivel separada (SRP).
- **Desventajas**: Aumenta la complejidad del código al introducir más clases e interfaces.

---

### Composite (Compuesto)
- **Propósito**: Permite componer objetos en estructuras de árbol y luego tratar a los objetos individuales y a las composiciones de manera uniforme.
- **Cuándo Usarlo**: Cuando se tiene una jerarquía de parte-todo (ej. sistema de archivos, menús gráficos) y se quiere que el cliente trate a todos los objetos de la misma manera.
- **Ventajas**: Simplifica el código cliente, que no necesita diferenciar entre objetos simples y compuestos. Facilita la adición de nuevos tipos de componentes (OCP).
- **Desventajas**: Puede ser difícil restringir los tipos de componentes que se pueden añadir a un compuesto. El diseño puede volverse demasiado general.

---

### Decorator (Decorador)
- **Propósito**: Añade nuevas funcionalidades a un objeto dinámicamente, envolviéndolo en objetos decoradores que comparten la misma interfaz.
- **Cuándo Usarlo**: Para extender el comportamiento de un objeto sin usar la herencia, especialmente cuando se necesitan múltiples combinaciones de funcionalidades.
- **Ventajas**: Gran flexibilidad para añadir responsabilidades. Evita la explosión de subclases. Permite añadir o quitar funcionalidades en tiempo de ejecución.
- **Desventajas**: Puede crear una gran cantidad de objetos pequeños. Puede ser complicado eliminar un decorador específico de la pila de envoltorios.

---

### Facade (Fachada)
- **Propósito**: Proporciona una interfaz simplificada y unificada para un subsistema complejo.
- **Cuándo Usarlo**: Para reducir la complejidad y desacoplar al cliente de los detalles internos de un conjunto de clases (ej. una librería, un framework).
- **Ventajas**: Aísla al cliente de la complejidad del subsistema. Promueve el bajo acoplamiento.
- **Desventajas**: La fachada puede convertirse en un "God Object" si asume demasiadas responsabilidades.

---

### Flyweight (Peso Ligero)
- **Propósito**: Minimiza el uso de memoria al compartir la mayor cantidad de datos posible con otros objetos similares, separando el estado intrínseco (compartido) del extrínseco (único).
- **Cuándo Usarlo**: Cuando se necesita una cantidad masiva de objetos que tienen estados parcialmente duplicados (ej. partículas en un juego, caracteres en un editor).
- **Ventajas**: Ahorro significativo de memoria RAM.
- **Desventajas**: Aumenta la complejidad del código al tener que gestionar el estado extrínseco fuera del objeto.

---

- **Propósito**: Proporciona un sustituto o intermediario para otro objeto con el fin de controlar el acceso a este.
- **Cuándo Usarlo**: Para implementar inicialización diferida (virtual proxy), control de acceso (protection proxy), caching (smart proxy) o para representar un objeto remoto.
- **Ventajas**: Permite ejecutar tareas antes o después de la solicitud al objeto real. Mejora el rendimiento y la seguridad.
- **Desventajas**: Puede introducir un pequeño retardo debido a la indirección. Aumenta el número de clases.

---

## 3. Tabla Comparativa Rápida

| Patrón | Intención Principal | Foco | Analogía |
| :--- | :--- | :--- | :--- |
| **Adapter** | Convertir una interfaz en otra. | Hacer que dos cosas incompatibles funcionen juntas. | Traductor de idiomas. |
| **Bridge** | Desacoplar abstracción de implementación. | Dividir una jerarquía monolítica en dos independientes. | Interruptor de luz y aparato eléctrico. |
| **Composite** | Tratar a un grupo de objetos como a uno solo. | Construir jerarquías de parte-todo. | Ejército (soldados y divisiones). |
| **Decorator** | Añadir comportamiento a un objeto. | Envolver un objeto para darle nuevas "capas" de funcionalidad. | Ponerse ropa (chaqueta, bufanda). |
| **Facade** | Simplificar la interfaz de un subsistema. | Ocultar la complejidad interna. | Conserje de hotel. |
| **Flyweight** | Ahorrar memoria compartiendo estado. | Optimizar el uso de recursos para un gran número de objetos. | Caracteres en un editor de texto. |
| **Proxy** | Controlar el acceso a un objeto. | Actuar como un intermediario con poder. | Tarjeta de crédito. |
