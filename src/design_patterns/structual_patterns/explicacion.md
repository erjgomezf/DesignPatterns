# Patrones de Diseño Estructurales

Este documento ofrece un resumen y una comparación de los patrones de diseño estructurales, explicando cómo ensamblan objetos y clases en estructuras más grandes, manteniendo al mismo tiempo estas estructuras flexibles y eficientes.

---

## ¿Qué son los Patrones Estructurales?

Los **patrones estructurales** se centran en cómo las clases y los objetos se componen para formar estructuras más grandes. Simplifican el diseño identificando formas sencillas de realizar relaciones entre entidades. Mientras que los patrones creacionales se ocupan de la *creación* de objetos, los estructurales se ocupan de su *composición*.

**Ventaja principal:** Ayudan a garantizar que cuando una parte de un sistema cambia, el sistema entero no necesita hacerlo. Promueven la flexibilidad y la eficiencia en la arquitectura del software.

A continuación, se resumen los patrones estructurales cubiertos en este proyecto.

---

## Resumen de Patrones

### 1. Adapter (Adaptador)
- **Propósito:** Permite que interfaces incompatibles trabajen juntas. Actúa como un traductor entre dos objetos.
- **Cuándo usarlo:** Para integrar una clase existente (legado, terceros) cuya interfaz no coincide con la que el cliente espera.

### 2. Bridge (Puente)
- **Propósito:** Desacopla una abstracción de su implementación para que ambas puedan evolucionar de forma independiente.
- **Cuándo usarlo:** Para evitar una "explosión de clases" cuando se tienen múltiples dimensiones de variación (ej. formas y colores, interfaces y plataformas).

### 3. Composite (Compuesto)
- **Propósito:** Permite componer objetos en estructuras de árbol y luego tratar a estos objetos (individuales y compuestos) de manera uniforme.
- **Cuándo usarlo:** Cuando se tiene una jerarquía de parte-todo y se quiere que el cliente ignore la diferencia entre objetos individuales y contenedores.

### 4. Decorator (Decorador)
- **Propósito:** Añade nuevas funcionalidades a un objeto dinámicamente, envolviéndolo en un objeto decorador.
- **Cuándo usarlo:** Para extender el comportamiento de un objeto sin usar la herencia, especialmente cuando se necesitan múltiples combinaciones de funcionalidades.

### 5. Facade (Fachada)
- **Propósito:** Proporciona una interfaz simplificada y unificada para un subsistema complejo.
- **Cuándo usarlo:** Para reducir la complejidad y desacoplar al cliente de los detalles internos de un conjunto de clases.

### 6. Flyweight (Peso Ligero)
- **Propósito:** Minimiza el uso de memoria al compartir la mayor cantidad de datos posible con otros objetos similares.
- **Cuándo usarlo:** Cuando se necesita una gran cantidad de objetos que tienen estados parcialmente duplicados.

### 7. Proxy
- **Propósito:** Proporciona un sustituto o intermediario para otro objeto con el fin de controlar el acceso a este.
- **Cuándo usarlo:** Para implementar inicialización diferida (virtual proxy), control de acceso (protection proxy), caching (smart proxy) o para representar un objeto remoto (remote proxy).

---

## Tabla Comparativa Rápida

| Patrón | Intención Principal | Foco | Analogía |
| :--- | :--- | :--- | :--- |
| **Adapter** | Convertir una interfaz en otra. | Hacer que dos cosas incompatibles funcionen juntas. | Traductor de idiomas. |
| **Bridge** | Desacoplar abstracción de implementación. | Dividir una jerarquía monolítica en dos independientes. | Interruptor de luz y aparato eléctrico. |
| **Composite** | Tratar a un grupo de objetos como a uno solo. | Construir jerarquías de parte-todo. | Ejército (soldados y divisiones). |
| **Decorator** | Añadir comportamiento a un objeto. | Envolver un objeto para darle nuevas "capas" de funcionalidad. | Ponerse ropa (chaqueta, bufanda). |
| **Facade** | Simplificar la interfaz de un subsistema. | Ocultar la complejidad interna. | Conserje de hotel. |
| **Flyweight** | Ahorrar memoria compartiendo estado. | Optimizar el uso de recursos para un gran número de objetos. | Caracteres en un editor de texto. |
| **Proxy** | Controlar el acceso a un objeto. | Actuar como un intermediario con poder. | Tarjeta de crédito. |
