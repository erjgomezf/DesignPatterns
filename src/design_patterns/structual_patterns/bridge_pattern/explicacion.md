# Patrón de Diseño: Bridge (Puente)

Este documento ofrece una explicación didáctica del patrón **Bridge**, utilizando el código de este proyecto como referencia.

---

## 1. ¿Qué es el Patrón Bridge?

> El **Bridge** es un patrón de diseño estructural que permite **desacoplar una abstracción de su implementación** para que las dos puedan evolucionar de forma independiente.

Imagina que tienes una clase `Shape` (Forma) con subclases como `Circle` (Círculo) y `Square` (Cuadrado). Ahora, quieres extender esta jerarquía para que las formas puedan dibujarse en diferentes formatos: como `Vector` o como `Raster` (mapa de bits). Si usas la herencia, tendrías que crear `VectorCircle`, `RasterCircle`, `VectorSquare` y `RasterSquare`. Si añades una nueva forma o un nuevo formato de dibujo, el número de clases explota. Esto se conoce como una "explosión de clases".

El patrón Bridge resuelve este problema dividiendo la jerarquía en dos: una para la **abstracción** (las formas) y otra para la **implementación** (los motores de renderizado). La abstracción contiene una referencia a la implementación, creando un "puente" entre ambas.

### ¿Qué Problema Resuelve?

- **Evita una "explosión de clases"**: Previene el crecimiento exponencial del número de clases cuando una clase y lo que hace varían en más de una dimensión.
- **Desacopla la interfaz de la implementación**: Permite que la forma en que un cliente ve una acción (la abstracción) y la forma en que esa acción se realiza (la implementación) cambien de forma independiente.
- **Cumple el Principio de Abierto/Cerrado**: Puedes introducir nuevas abstracciones e implementaciones sin modificar las existentes.

---

## 2. Componentes del Patrón

| Componente | Rol | Archivo de Ejemplo |
| :--- | :--- | :--- |
| **Abstraction (Abstracción)** | Define la interfaz de alto nivel para el cliente. Mantiene una referencia a un objeto `Implementor`. | `shape.py` -> `Shape` |
| **RefinedAbstraction** | Extiende la interfaz definida por `Abstraction`. | `circle.py`, `square.py` -> `Circle`, `Square` |
| **Implementor (Implementador)** | Define la interfaz para las clases de implementación. No tiene por qué corresponder con la interfaz de `Abstraction`. | `rendering_engine.py` -> `RenderingEngine` |
| **ConcreteImplementor** | Implementa la interfaz `Implementor`. Contiene el código de bajo nivel específico de la plataforma. | `vector_renderer.py`, `raster_renderer.py` -> `VectorRenderer`, `RasterRenderer` |

---

## 3. Análisis del Código de Ejemplo

Nuestro ejemplo desacopla las `Formas` (abstracción) de su `Motor de Renderizado` (implementación).

### a. La Jerarquía de `Implementor`

- **`RenderingEngine(ABC)`**: Es la interfaz `Implementor`. Define las operaciones de bajo nivel que cualquier motor de renderizado debe poder hacer, como `render_circle()` y `render_square()`.
- **`VectorRenderer` y `RasterRenderer`**: Son los `ConcreteImplementor`. Cada uno proporciona una implementación específica para los métodos de la interfaz. Uno "dibuja" con vectores y el otro con píxeles.

### b. La Jerarquía de `Abstraction`

- **`Shape(ABC)`**: Es la `Abstraction` base.
    1.  **Contiene el "Puente"**: En su constructor, recibe y almacena una referencia a un objeto `RenderingEngine`. Esta es la clave del patrón.
    2.  **Define métodos de alto nivel**: Declara métodos como `draw()` y `resize()` que son significativos para el cliente.
- **`Circle` y `Square`**: Son las `RefinedAbstraction`.
    - Implementan los métodos de `Shape`.
    - La parte crucial es que **delegan el trabajo de bajo nivel al implementador**. El método `draw()` de `Circle` no sabe cómo dibujar un círculo; simplemente llama a `self._renderer.render_circle()`. La forma no se preocupa por *cómo* se dibuja, solo por *qué* se dibuja.

### c. El `Client`: `main.py`

- El `client_code` demuestra la flexibilidad del patrón:
    - Puede crear un `Circle` y pasarle un `VectorRenderer`.
    - Puede crear otro `Circle` y pasarle un `RasterRenderer`.
    - Puede cambiar la implementación en tiempo de ejecución si fuera necesario.
- El cliente puede combinar cualquier forma con cualquier motor de renderizado, demostrando que las dos jerarquías son completamente independientes.

---

## 4. Ventajas y Desventajas

### Ventajas

1.  **Flexibilidad y Extensibilidad**: Puedes crear y modificar las abstracciones y las implementaciones de forma independiente.
2.  **Desacoplamiento Fuerte**: El cliente solo depende de la abstracción, y la abstracción solo depende de la interfaz de implementación, no de sus clases concretas.
3.  **Principio de Responsabilidad Única (SRP)**: La lógica de alto nivel (en `Shape`) está separada de la lógica de bajo nivel específica de la plataforma (en los `Renderers`).

### Desventajas

1.  **Aumento de la Complejidad**: El patrón introduce varias clases e interfaces nuevas, lo que puede hacer que el código sea más complicado para sistemas simples.

---

## 5. Bridge vs. Adapter

Son fáciles de confundir, pero su intención es diferente.

| Patrón | Intención | ¿Cuándo se usa? |
| :--- | :--- | :--- |
| **Bridge** | **Desacoplar** una abstracción de su implementación. | **Desde el principio**. Se usa en el diseño inicial para evitar una explosión de clases y permitir que dos jerarquías evolucionen por separado. |
| **Adapter** | **Hacer que interfaces incompatibles trabajen juntas**. | **Después de que el sistema ya existe**. Se usa para integrar código legado o de terceros sin cambiar su interfaz original. |

### Analogía para Recordar

- **Bridge (Interruptor de Luz y Aparato Eléctrico):**
  - Tienes un interruptor en la pared (`Abstraction`). Su trabajo es `encender()` y `apagar()`.
  - A ese interruptor puedes conectar diferentes aparatos: una bombilla, un ventilador, un altavoz (`Implementor`).
  - El interruptor no sabe ni le importa qué aparato está conectado. Su lógica de "encender/apagar" es independiente. El aparato, por su parte, no sabe qué tipo de interruptor lo controla.
  - Puedes cambiar la bombilla por un ventilador (`ConcreteImplementor`) sin cambiar el interruptor (`Abstraction`). Y puedes cambiar el interruptor por uno con regulador (`RefinedAbstraction`) sin cambiar el aparato.

---

## 6. Cómo Ejecutar el Ejemplo

Para que las importaciones funcionen correctamente, ejecuta el código como un módulo desde el directorio raíz del proyecto.

1.  **Sitúate en la raíz del proyecto:**
    ```bash
    cd /ruta/a/tu/proyecto/DesignPatterns
    ```

2.  **Ejecuta el módulo `main`:**
    ```bash
    python3 -m src.design_patterns.structual_patterns.bridge_pattern.main
    ```

La salida mostrará cómo las mismas formas (`Circle`, `Square`) pueden ser dibujadas por diferentes motores de renderizado, produciendo resultados distintos pero manteniendo la misma interfaz de alto nivel.
