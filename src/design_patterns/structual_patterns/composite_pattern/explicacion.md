# Patrón de Diseño: Composite (Compuesto)

Este documento ofrece una explicación didáctica del patrón **Composite**, utilizando el código de este proyecto como referencia.

---

## 1. ¿Qué es el Patrón Composite?

> El **Composite** es un patrón de diseño estructural que permite componer objetos en **estructuras de árbol** para representar jerarquías de parte-todo. El patrón Composite permite que los clientes traten a los objetos individuales (hojas) y a las composiciones de objetos (compuestos) de manera uniforme.

Imagina un sistema de archivos. Un directorio puede contener archivos y otros directorios. Un archivo es un objeto simple (una "hoja"), mientras que un directorio es un objeto complejo (un "compuesto") que contiene otros objetos. Sin embargo, a menudo queremos realizar la misma operación en ambos, como `calcular_tamaño()` o `buscar()`. El patrón Composite nos permite hacer exactamente eso: tratar a un solo archivo y a un directorio lleno de archivos de la misma manera.

### ¿Qué Problema Resuelve?

Resuelve el problema de tener que tratar de manera diferente a los objetos simples y a los contenedores de objetos. Sin este patrón, el código cliente tendría que estar lleno de condicionales (`if objeto es un archivo... else if objeto es un directorio...`) para manejar una estructura de árbol, lo que lo hace complejo y difícil de mantener.

El patrón Composite simplifica al cliente al proporcionar una interfaz común para todos los objetos de la jerarquía.

---

## 2. Componentes del Patrón

| Componente | Rol | Archivo de Ejemplo |
| :--- | :--- | :--- |
| **Component (Componente)** | La interfaz o clase base abstracta para todos los objetos de la composición. Declara los métodos para las hojas y los compuestos. | `graphic.py` -> `Graphic` |
| **Leaf (Hoja)** | El objeto simple y final de la jerarquía. No tiene hijos. | `simple_graphics.py` -> `Circle`, `Square` |
| **Composite (Compuesto)** | El objeto que contiene hijos (hojas u otros compuestos). Implementa los métodos de la interfaz `Component` delegando en sus hijos. | `composite_graphic.py` -> `CompositeGraphic` |
| **Client (Cliente)** | Manipula los objetos de la composición a través de la interfaz `Component`. | `main.py` -> `client_code` |

---

## 3. Análisis del Código de Ejemplo

Nuestro ejemplo modela un sistema de dibujo donde podemos crear figuras simples y agruparlas en dibujos más complejos.

### a. El `Component`: `graphic.py`

- **`Graphic(ABC)`**: Es la interfaz común para todos los objetos.
    - Declara el método `draw()`, que será implementado por todos.
    - También incluye métodos para gestionar hijos como `add()` y `remove()`. En la clase base, estos métodos lanzan un `NotImplementedError`. Esto se conoce como una implementación "transparente": la interfaz es la misma para hojas y compuestos, pero las hojas no soportan operaciones de hijos.

### b. Los `Leaf`: `simple_graphics.py`

- **`Circle` y `Square`**: Son las hojas. Representan los objetos básicos.
    - Implementan el método `draw()` para dibujarse a sí mismos.
    - No sobrescriben `add()` ni `remove()`, por lo que si un cliente intenta añadir un hijo a un círculo, obtendrá un error, lo cual es correcto.

### c. El `Composite`: `composite_graphic.py`

- **`CompositeGraphic`**: Es el contenedor.
    1.  **Mantiene una lista de hijos**: Tiene un atributo `_children` para almacenar otros objetos `Graphic`.
    2.  **Implementa la gestión de hijos**: Sobrescribe `add()` y `remove()` para permitir que el cliente manipule su contenido.
    3.  **Delega la operación principal**: Su método `draw()` es la clave del patrón. Primero se dibuja a sí mismo (imprimiendo su nombre de contenedor) y luego itera sobre todos sus hijos, llamando al método `draw()` de cada uno. No le importa si un hijo es una hoja o otro compuesto; simplemente confía en que cada uno sabe cómo dibujarse.

### d. El `Client`: `main.py`

- El `client_code` construye una estructura de árbol compleja:
    - Crea hojas (`Circle`, `Square`).
    - Crea un compuesto (`sub_drawing`) y le añade hojas.
    - Crea un compuesto principal (`main_drawing`) y le añade el compuesto anterior y más hojas.
- La gran ventaja es que, para dibujar toda la escena, el cliente solo necesita hacer una llamada: `main_drawing.draw()`. La complejidad de recorrer el árbol y llamar a cada objeto individualmente está encapsulada en las clases del patrón.

---

## 4. Ventajas y Desventajas

### Ventajas

1.  **Simplifica el Código Cliente**: El cliente trata a las estructuras complejas y a los objetos individuales de la misma manera. No necesita condicionales para diferenciar.
2.  **Principio de Abierto/Cerrado (OCP)**: Es fácil añadir nuevos tipos de componentes (hojas o compuestos) sin cambiar el código cliente.
3.  **Flexibilidad y Escalabilidad**: Permite construir jerarquías de objetos de complejidad arbitraria.

### Desventajas

1.  **Puede ser "demasiado" general**: A veces, se quiere tratar a los compuestos y a las hojas de manera diferente. Con una interfaz común, es más difícil restringir las operaciones que solo tienen sentido para un tipo de objeto. Por ejemplo, no tiene sentido llamar a `get_children()` en una hoja.
2.  **Complejidad de la implementación**: La lógica para gestionar las relaciones padre-hijo puede añadir complejidad, especialmente en lenguajes de bajo nivel.

---

## 5. Composite vs. Decorator

| Patrón | Propósito Principal | Estructura |
| :--- | :--- | :--- |
| **Composite** | Tratar a un **grupo de objetos** de la misma manera que a un **objeto único**. | Se enfoca en la agregación de objetos (relaciones "tiene un"). La estructura es de árbol. |
| **Decorator** | **Añadir funcionalidades** a un objeto dinámicamente. | Se enfoca en envolver un objeto para extender su comportamiento sin alterar su interfaz. La estructura es como una "cebolla". |

### Analogía para Recordar

- **Composite (Ejército):**
  - Un ejército está compuesto por divisiones. Cada división está compuesta por brigadas, y cada brigada por soldados.
  - Un soldado es una "hoja". Una brigada y una división son "compuestos".
  - Cuando el general da la orden "avanzar", no se lo dice a cada soldado individualmente. Le da la orden a todo el ejército. La orden se propaga por la jerarquía: el ejército se la pasa a las divisiones, las divisiones a las brigadas, y las brigadas a los soldados. Todos reaccionan a la misma orden.

---

## 6. Cómo Ejecutar el Ejemplo

Para que las importaciones funcionen correctamente, ejecuta el código como un módulo desde el directorio raíz del proyecto.

1.  **Sitúate en la raíz del proyecto:**
    ```bash
    cd /ruta/a/tu/proyecto/DesignPatterns
    ```

2.  **Ejecuta el módulo `main`:**
    ```bash
    python3 -m src.design_patterns.structual_patterns.composite_pattern.main
    ```

La salida mostrará una estructura de árbol anidada, demostrando cómo la llamada a `draw()` en el objeto de más alto nivel se propaga a través de toda la jerarquía.
