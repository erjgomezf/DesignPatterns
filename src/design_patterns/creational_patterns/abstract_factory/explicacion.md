# Patrón de Diseño: Abstract Factory (Fábrica Abstracta)

Este documento ofrece una explicación didáctica del patrón **Abstract Factory**, utilizando el código de este proyecto como referencia.

---

## 1. ¿Qué es el Patrón Abstract Factory?

> El **Abstract Factory** es un patrón de diseño creacional que proporciona una interfaz para crear **familias de objetos relacionados o dependientes** sin especificar sus clases concretas.

Imagina que estás construyendo una aplicación que debe tener una apariencia nativa en Windows y macOS. Los botones, checkboxes y ventanas se ven diferentes en cada sistema operativo, pero están relacionados entre sí (un botón de Windows pertenece a la "familia" de widgets de Windows).

Este patrón te permite crear una `GUIFactory` que puede ser una `WindowsFactory` o una `MacOSFactory`. El resto de tu aplicación no necesita saber cuál está usando; simplemente pide a la fábrica que "cree un botón" y obtendrá el correcto para el sistema operativo actual.

### ¿Qué Problema Resuelve?

Resuelve el problema de cómo crear objetos que pertenecen a una misma familia sin acoplar el código cliente a las clases concretas de esa familia. Permite que un sistema sea independiente de cómo se crean, componen y representan sus productos.

---

## 2. Componentes del Patrón

Este patrón tiene más piezas móviles que otros, pero su estructura es muy lógica.

| Componente | Rol | Archivo de Ejemplo |
| :--- | :--- | :--- |
| **AbstractProduct** | Declara una interfaz para un tipo de objeto producto. | `gui_factory.py` -> `Button`, `Checkbox` |
| **ConcreteProduct** | Implementa la interfaz `AbstractProduct`. Son los objetos reales que crea la fábrica. | `gui_factory.py` -> `WindowsButton`, `MacOSButton`, etc. |
| **AbstractFactory** | Declara una interfaz con métodos para crear cada `AbstractProduct`. | `gui_factory.py` -> `GUIFactory` |
| **ConcreteFactory** | Implementa los métodos de la `AbstractFactory` para crear una familia de `ConcreteProduct`. | `gui_factory.py` -> `WindowsFactory`, `MacOSFactory` |
| **Client** | Utiliza únicamente las interfaces `AbstractFactory` y `AbstractProduct`. | `main.py` -> `Application` |

---

## 3. Análisis del Código de Ejemplo

### a. Fábricas y Productos: `gui_factory.py`

1.  **Productos Abstractos (`Button`, `Checkbox`)**: Son clases base abstractas que definen lo que un producto *puede hacer* (ej. `paint()`), pero no cómo lo hace.
2.  **Productos Concretos (`WindowsButton`, `MacOSButton`, etc.)**: Son las implementaciones reales. Un `WindowsButton` sabe cómo dibujarse al estilo de Windows.
3.  **Fábrica Abstracta (`GUIFactory`)**: Define un contrato. Cualquier fábrica que la implemente *debe* saber cómo crear un botón y un checkbox.
4.  **Fábricas Concretas (`WindowsFactory`, `MacOSFactory`)**: Son las que hacen el trabajo. `WindowsFactory` crea instancias de `WindowsButton` y `WindowsCheckbox`. `MacOSFactory` crea las suyas. La clave es que cada fábrica produce objetos que son consistentes entre sí.

### b. El Cliente: `main.py`

- **`Application`**: Esta clase es el `Client`. Su constructor recibe un objeto de tipo `GUIFactory`.
- **Desacoplamiento total**: La `Application` no tiene idea de si está trabajando con una `WindowsFactory` o una `MacOSFactory`. Solo sabe que la fábrica que recibió puede crear botones y checkboxes que responden al método `paint()`.
- **Configuración inicial**: La única parte del código que conoce las clases concretas es el punto de entrada (`client_code`), donde se decide qué fábrica instanciar. Una vez que la fábrica se pasa a la aplicación, todo el conocimiento concreto queda aislado.

---

## 4. Ventajas y Desventajas

### Ventajas

1.  **Aísla las clases concretas**: El cliente no sabe nada sobre `WindowsButton` o `MacOSCheckbox`. Esto hace que el código del cliente sea más limpio y fácil de mantener.
2.  **Facilita el intercambio de familias de productos**: Puedes cambiar toda la apariencia de la aplicación simplemente cambiando la clase de la fábrica que se instancia al principio.
3.  **Garantiza la consistencia entre productos**: Como una fábrica concreta crea todos los productos de una familia, te aseguras de que los objetos resultantes sean compatibles entre sí (no mezclarás un botón de Mac con una ventana de Windows).

### Desventajas

1.  **Difícil de extender con nuevos tipos de productos**: Si quieres añadir un nuevo producto (por ejemplo, un `TextBox`), tienes que modificar la interfaz `AbstractFactory` y **todas** sus subclases (`ConcreteFactory`). Esto puede ser mucho trabajo y viola el Principio de Abierto/Cerrado.

---

## 5. Abstract Factory vs. Otros Patrones Creacionales

| Patrón | Enfoque | Cuándo Usarlo |
| :--- | :--- | :--- |
| **Abstract Factory** | Crear **familias** de objetos relacionados. | Cuando tu sistema debe ser independiente de cómo se crean sus productos y necesitas trabajar con múltiples familias de objetos. |
| **Factory Method** | Crear **un** objeto, delegando la instanciación a subclases. | Cuando una clase no puede anticipar la clase de los objetos que debe crear y quieres que las subclases especifiquen qué crear. |
| **Builder** | Construir un objeto **complejo** paso a paso. | Cuando la construcción de un objeto es compleja, tiene muchas partes opcionales o requiere un orden específico. |
| **Prototype** | Crear un objeto **clonando** uno existente. | Cuando el coste de crear un objeto desde cero es alto. |

### Analogía para Recordar

- **Abstract Factory (Kit de Muebles de IKEA):**
  - Quieres amueblar una habitación con un estilo coherente (por ejemplo, la serie "Malm").
  - La `AbstractFactory` es el catálogo de IKEA que dice: "Podemos darte una cama, un armario y una mesita de noche".
  - La `ConcreteFactory` ("MalmFactory") te da una cama Malm, un armario Malm y una mesita de noche Malm. Todos encajan perfectamente.
  - Otra `ConcreteFactory` ("HemnesFactory") te daría el mismo conjunto de muebles, pero en el estilo Hemnes.
  - Tú, como cliente, solo pides "una cama" a la fábrica que te dieron, y confías en que será del estilo correcto.

---

## 6. Cómo Ejecutar el Ejemplo

1.  **Sitúate en la raíz del proyecto:**
    ```bash
    cd /ruta/a/tu/proyecto/DesignPatterns
    ```

2.  **Ejecuta el módulo `main`:**
    ```bash
    python3 -m src.design_patterns.creational_patterns.abstract_factory.main
    ```

La salida dependerá de tu sistema operativo. Si estás en Linux o macOS, verás los mensajes de "Renderizando... estilo macOS". Si estás en Windows, verás los de estilo Windows. Esto demuestra cómo el mismo código cliente se adapta a diferentes "familias" de productos.

```

¡Y con esto tienes un ejemplo completo del patrón Abstract Factory! Es un patrón muy elegante para sistemas que necesitan ser flexibles y soportar múltiples "temas" o "plataformas".

<!--
[PROMPT_SUGGESTION]Ahora crea un ejemplo para el patrón creacional "Builder".[/PROMPT_SUGGESTION]
[PROMPT_SUGGESTION]Compara en una tabla las ventajas y desventajas de todos los patrones creacionales que hemos visto.[/PROMPT_SUGGESTION]
->