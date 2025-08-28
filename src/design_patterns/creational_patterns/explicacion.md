# Patrones de Diseño Creacionales

Este documento ofrece un resumen y una comparación de los patrones de diseño creacionales, explicando su propósito, ventajas y casos de uso. Los patrones creacionales son fundamentales para construir sistemas de software flexibles y escalables, ya que se centran en los mecanismos de creación de objetos.

---

## ¿Qué son los Patrones Creacionales?

Los **patrones creacionales** son patrones de diseño que abstraen el proceso de instanciación de objetos. Ayudan a que un sistema sea independiente de cómo se crean, componen y representan sus objetos. En lugar de instanciar objetos directamente con el operador `new` (o su equivalente en Python, `Clase()`), estos patrones delegan la responsabilidad de la creación a objetos o métodos especializados.

**Ventaja principal:** Introducen flexibilidad en el proceso de creación, permitiendo que el código cliente trabaje con interfaces abstractas en lugar de implementaciones concretas. Esto promueve el desacoplamiento y facilita la aplicación de los principios SOLID, especialmente el de Inversión de Dependencias (DIP) y el de Abierto/Cerrado (OCP).

A continuación, se resumen los patrones creacionales cubiertos en este proyecto.

---

## 1. Factory Method (Método de Fábrica)

- **Propósito:** Define una interfaz para crear un objeto, pero delega la instanciación a las subclases.
- **Cuándo usarlo:** Cuando una clase no puede anticipar la clase de los objetos que necesita crear, y quiere que sus subclases especifiquen qué crear. Es ideal para cumplir con el Principio Abierto/Cerrado.
- **Ventajas:**
    - Desacopla el código cliente de las clases de productos concretos.
    - Permite introducir nuevos productos sin modificar el código cliente.
- **Desventajas:**
    - Requiere la creación de una jerarquía de clases paralela (una subclase de creador por cada producto).

---

## 2. Abstract Factory (Fábrica Abstracta)

- **Propósito:** Proporciona una interfaz para crear **familias de objetos relacionados o dependientes** sin especificar sus clases concretas.
- **Cuándo usarlo:** Cuando tu sistema debe ser configurable con múltiples familias de productos que deben ser consistentes entre sí (ej. temas de UI para Windows y macOS).
- **Ventajas:**
    - Garantiza la compatibilidad entre los productos de una misma familia.
    - Aísla completamente al cliente de las implementaciones concretas.
- **Desventajas:**
    - Es difícil añadir nuevos *tipos* de productos, ya que requiere modificar la interfaz de la fábrica abstracta y todas sus implementaciones.

---

## 3. Builder (Constructor)

- **Propósito:** Separa la construcción de un objeto complejo de su representación final, permitiendo que el mismo proceso de construcción cree diferentes representaciones.
- **Cuándo usarlo:** Cuando la creación de un objeto implica muchos pasos, parámetros opcionales o una configuración compleja. Ideal para crear objetos inmutables.
- **Ventajas:**
    - Permite construir objetos paso a paso y de forma legible (usando una "fluent interface").
    - Aísla el código de construcción complejo del objeto final.
- **Desventajas:**
    - Aumenta la verbosidad al requerir la creación de una clase `Builder` adicional.

---

## 4. Prototype (Prototipo)

- **Propósito:** Permite crear nuevos objetos copiando una instancia existente (un "prototipo").
- **Cuándo usarlo:** Cuando el coste de crear un objeto desde cero es alto (ej. por acceso a base de datos o cálculos pesados), o cuando se quiere evitar una jerarquía de fábricas.
- **Ventajas:**
    - Permite añadir y eliminar productos en tiempo de ejecución.
    - Reduce la necesidad de subclases de creación.
    - Puede ser más eficiente que la creación estándar.
- **Desventajas:**
    - La clonación de objetos complejos con referencias circulares puede ser complicada.

---

## 5. Singleton

- **Propósito:** Garantiza que una clase tenga **una única instancia** y proporciona un punto de acceso global a ella.
- **Cuándo usarlo:** Para recursos que deben ser compartidos y únicos en todo el sistema, como un gestor de configuración, un logger o una conexión a base de datos.
- **Ventajas:**
    - Asegura una única instancia y un acceso global controlado.
    - Permite la inicialización diferida (lazy initialization).
- **Desventajas:**
    - **¡Usar con precaución!** Viola el Principio de Responsabilidad Única, oculta dependencias, dificulta las pruebas unitarias y puede causar problemas en entornos multihilo si no se implementa correctamente. A menudo, la **Inyección de Dependencias** es una alternativa superior.

---

## Tabla Comparativa Rápida

| Patrón | Propósito Principal | Estructura Principal | ¿Cuándo es mejor? |
| :--- | :--- | :--- | :--- |
| **Factory Method** | Crear **un** objeto delegando a subclases. | Herencia | Para permitir que las subclases decidan qué objeto instanciar. |
| **Abstract Factory** | Crear **familias** de objetos relacionados. | Composición y Herencia | Para asegurar que los objetos creados sean de una misma variante (ej. tema, plataforma). |
| **Builder** | Construir un objeto **complejo** paso a paso. | Composición | Para simplificar la creación de objetos con muchos parámetros o pasos de configuración. |
| **Prototype** | Crear un objeto **clonando** uno existente. | Composición y Clonación | Para evitar el coste de la creación desde cero o para configurar objetos en tiempo de ejecución. |
| **Singleton** | Garantizar **una única instancia** global. | Variable de clase estática | Para recursos que deben ser únicos y compartidos globalmente (usar con cuidado). |
