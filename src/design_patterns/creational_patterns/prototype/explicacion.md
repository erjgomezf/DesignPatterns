# Patrón de Diseño: Prototype (Prototipo)

Este documento ofrece una explicación didáctica del patrón **Prototype**, utilizando el código de este proyecto como referencia.

---

## 1. ¿Qué es el Patrón Prototype?

> El **Prototype** es un patrón de diseño creacional que permite crear nuevos objetos copiando una instancia existente, conocida como "prototipo".

En lugar de construir un objeto desde cero (lo que puede ser costoso y complejo), clonas un objeto pre-configurado. Esto es especialmente útil cuando la creación de un objeto implica operaciones costosas o cuando se quiere evitar una jerarquía de clases de fábricas paralelas a la jerarquía de clases de productos.

### ¿Qué Problema Resuelve?

Resuelve el problema de tener que acoplar el código cliente a las clases concretas que necesita instanciar. El cliente puede obtener un nuevo objeto sin saber su clase exacta, simplemente pidiendo a un objeto prototipo que se clone a sí mismo.

---

## 2. Componentes del Patrón

Analicemos las piezas clave del patrón y su correspondencia en nuestro código de ejemplo:

| Componente | Rol | Archivo de Ejemplo |
| :--- | :--- | :--- |
| **Prototype (Prototipo)** | Define la interfaz para clonarse a sí mismo. | `shapes.py` -> `Shape` |
| **ConcretePrototype** | Implementación concreta de la interfaz `Prototype`. Es el objeto que será copiado. | `shapes.py` -> `Rectangle`, `Circle` |
| **Client (Cliente)** | Crea un nuevo objeto pidiendo a un prototipo que se clone. | `main.py` -> `client_code` |
| **Prototype Registry (Opcional)** | Proporciona una forma fácil de acceder a los prototipos de uso frecuente, a menudo mediante un identificador de cadena. | `main.py` -> `PrototypeRegistry` |

---

## 3. Análisis del Código de Ejemplo

### a. Los Prototipos: `shapes.py`

- **`Shape(ABC)`**: Actúa como la interfaz `Prototype`.
    - Declara el método abstracto `clone()`, que obliga a las subclases a ser clonables.
    - Contiene atributos comunes a todas las formas (`x`, `y`, `color`).
- **`Rectangle` y `Circle`**: Son los `ConcretePrototype`.
    - Implementan el método `clone()`. En Python, la forma más robusta de hacerlo es usando `copy.deepcopy(self)`. Esto asegura que se cree una copia completamente independiente del objeto, incluyendo todos sus atributos, incluso si son otros objetos.

### b. El Cliente y el Registro: `main.py`

- **`PrototypeRegistry`**: Aunque es opcional en el patrón, es una adición muy común y útil.
    - Actúa como un "almacén" de prototipos. El cliente puede solicitar un prototipo por su nombre (ej. "default_rectangle").
    - Cuando se le pide un prototipo, no devuelve el objeto original, sino una **copia** de él. Esto protege al prototipo original de modificaciones accidentales.

- **`client_code`**:
    - Primero, crea y configura las instancias de prototipo iniciales y las guarda en el registro.
    - Luego, para crear un nuevo objeto, simplemente le pide al registro una copia de un prototipo existente.
    - El cliente puede entonces modificar las propiedades del objeto clonado sin afectar al prototipo original.
    - El cliente está desacoplado de las clases `Rectangle` y `Circle`. Solo necesita saber los nombres de los prototipos en el registro.

---

## 4. Ventaja Principal: Flexibilidad y Reducción de Subclases

La fortaleza del Prototype es que **permite añadir y eliminar productos en tiempo de ejecución**.

> Puedes introducir nuevos tipos de objetos en la aplicación simplemente creando una instancia de su clase, configurándola como desees y registrándola como un prototipo.

Esto contrasta con el Factory Method, que requiere la creación de una nueva subclase de `Creator` para cada nuevo tipo de producto.

- **Flexibilidad**: Puedes crear objetos complejos y configurarlos una sola vez. Las siguientes instancias se crean mediante una clonación mucho más barata.
- **Reducción de código**: Evita la necesidad de crear una jerarquía de creadores paralela a la jerarquía de productos.

---

## 5. Prototype vs. Factory Method: Una Diferencia Clave

Ambos son patrones creacionales, pero resuelven el problema de la creación de objetos de maneras fundamentalmente diferentes.

| Característica | Prototype (Prototipo) | Factory Method (Método de Fábrica) |
| :--- | :--- | :--- |
| **Propósito** | Crear objetos copiando un prototipo existente. | Crear objetos a través de la herencia, delegando la instanciación a subclases. |
| **Estructura** | Basado en **composición** y **clonación**. | Basado en **herencia**. |
| **Jerarquía** | No requiere una jerarquía de clases para la creación. | Requiere una jerarquía de Creadores paralela a la de Productos. |
| **Flexibilidad** | Permite configurar nuevos "creadores" (prototipos) en tiempo de ejecución. | La decisión de qué producto crear está fijada en la subclase del Creador. |

### Analogía para Recordar

- **Prototype (Máquina de Fotocopias):**
  - Tienes un documento original perfectamente diseñado (el `prototipo`).
  - Cuando necesitas una nueva copia, no lo redactas desde cero. Vas a la fotocopiadora (`clone()`) y obtienes una copia idéntica que puedes usar o modificar (escribir sobre ella).
  - Puedes fotocopiar cualquier documento que pongas en la máquina.

- **Factory Method (Línea de Ensamblaje Especializada):**
  - Tienes una línea de ensamblaje para coches (`RoadLogistics`) y otra para barcos (`SeaLogistics`).
  - La línea de coches *siempre* producirá coches (`Truck`). La de barcos *siempre* producirá barcos (`Ship`).
  - Para producir un nuevo tipo de vehículo, como un avión, necesitas construir una línea de ensamblaje completamente nueva (`AirLogistics`).

---

## 6. Cómo Ejecutar el Ejemplo

Para que las importaciones funcionen, ejecuta el código como un módulo desde el directorio raíz del proyecto.

1.  **Sitúate en la raíz del proyecto:**
    ```bash
    cd /ruta/a/tu/proyecto/DesignPatterns
    ```

2.  **Ejecuta el módulo `main`:**
    ```bash
    python3 -m src.design_patterns.creational_patterns.prototype.main
    ```

Esto correrá el `client_code`, que demostrará cómo se pueden crear nuevos objetos complejos simplemente clonando prototipos pre-configurados.
