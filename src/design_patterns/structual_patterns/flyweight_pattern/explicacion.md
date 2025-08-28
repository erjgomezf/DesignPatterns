# Patrón de Diseño: Flyweight (Peso Ligero)

Este documento ofrece una explicación didáctica del patrón **Flyweight**, utilizando el código de este proyecto como referencia.

---

## 1. ¿Qué es el Patrón Flyweight?

> El **Flyweight** es un patrón de diseño estructural que permite que un gran número de objetos quepan en la memoria disponible al **compartir** las partes comunes de su estado entre múltiples objetos, en lugar de mantener todos los datos en cada objeto.

Imagina que estás desarrollando un videojuego de estrategia en tiempo real con miles de árboles. Cada árbol tiene un nombre, un color, una textura, y también coordenadas `x` e `y`. Si cada objeto `Arbol` almacenara toda esa información, consumirías una cantidad enorme de memoria. Sin embargo, la mayoría de los árboles son del mismo tipo (por ejemplo, miles de "Pinos").

El patrón Flyweight resuelve esto dividiendo el estado del objeto en dos partes:
- **Estado Intrínseco**: La información que es **común** a muchos objetos y no cambia (el nombre "Pino", el color "Verde", la textura). Esta información se almacena en un objeto Flyweight compartido.
- **Estado Extrínseco**: La información que es **única** para cada objeto y varía (las coordenadas `x`, `y`). Esta información se pasa al método del flyweight cuando se necesita.

---

## 2. Componentes del Patrón

| Componente | Rol | Archivo de Ejemplo |
| :--- | :--- | :--- |
| **Flyweight** | La interfaz o clase que contiene el estado intrínseco y compartido. | `tree_type.py` -> `TreeType` |
| **FlyweightFactory** | Una clase que crea y gestiona los objetos Flyweight, asegurando que se compartan. | `tree_factory.py` -> `TreeFactory` |
| **Context (Contexto)** | La clase que contiene el estado extrínseco y una referencia a un objeto Flyweight. | `tree.py` -> `Tree` |
| **Client (Cliente)** | Calcula o almacena el estado extrínseco y lo pasa a los métodos del Flyweight. | `main.py` -> `Forest` |

---

## 3. Análisis del Código de Ejemplo

Nuestro ejemplo simula la renderización de un bosque con muchos árboles, optimizando la memoria.

### a. El `Flyweight`: `tree_type.py`

- **`TreeType`**: Esta es nuestra clase Flyweight.
    - Almacena el **estado intrínseco**: `_name`, `_color`, `_texture`. Estos datos son los mismos para todos los árboles de un tipo particular.
    - Su método `draw()` acepta el **estado extrínseco** (`x`, `y`) como argumentos. No almacena las coordenadas, solo las usa para realizar la operación.

### b. El `FlyweightFactory`: `tree_factory.py`

- **`TreeFactory`**: Su única responsabilidad es gestionar el pool de flyweights.
    - Mantiene un diccionario (`_tree_types`) que actúa como una caché.
    - El método `get_tree_type()` es la clave. Cuando el cliente solicita un tipo de árbol, la fábrica:
        1.  Construye una clave única a partir del estado intrínseco (`name`, `color`, `texture`).
        2.  Comprueba si ya existe un flyweight con esa clave.
        3.  Si existe, lo devuelve. **No se crea un objeto nuevo.**
        4.  Si no existe, crea una nueva instancia de `TreeType`, la guarda en la caché y la devuelve.

### c. El `Context`: `tree.py`

- **`Tree`**: Esta es la clase de contexto.
    - Almacena el **estado extrínseco**: las coordenadas `_x` e `_y`, que son únicas para cada árbol.
    - Mantiene una referencia a un objeto `TreeType` (el flyweight).
    - Cuando se llama a su método `draw()`, delega la acción al flyweight, pasándole su propio estado extrínseco: `self._tree_type.draw(self._x, self._y)`.

### d. El `Client`: `main.py`

- La clase `Forest` actúa como el cliente.
    - Cuando `plant_tree()` es llamado, no crea un `TreeType` directamente. En su lugar, se lo pide a la `TreeFactory`.
    - La fábrica se asegura de que, aunque plantemos 10 o 1,000 árboles, si solo hay 3 tipos diferentes (Roble, Pino, Abedul), solo se crearán **3 objetos `TreeType`**. El resto serán referencias compartidas.
    - El resultado es que tenemos miles de objetos `Tree` (ligeros) y solo un puñado de objetos `TreeType` (más pesados), ahorrando una cantidad significativa de memoria.

---

## 4. Ventajas y Desventajas

### Ventajas

1.  **Ahorro de Memoria Masivo**: Puede reducir drásticamente el consumo de RAM si se tienen muchos objetos con estados compartidos.
2.  **Mejora del Rendimiento**: Al haber menos objetos, la gestión de la memoria y la recolección de basura pueden ser más eficientes.

### Desventajas

1.  **Complejidad del Código**: Introduce una capa adicional de complejidad al tener que separar el estado intrínseco del extrínseco y gestionar la fábrica.
2.  **Mayor Carga de CPU**: El estado extrínseco debe ser recalculado o pasado a los métodos del flyweight cada vez, lo que puede suponer una pequeña sobrecarga de CPU a cambio del ahorro de memoria.

---

## 5. ¿Cuándo Usarlo?

Usa el patrón Flyweight solo cuando:

1.  La aplicación necesita generar una **gran cantidad de objetos**.
2.  Los objetos tienen un estado que puede dividirse en una parte **intrínseca (compartida)** y una parte **extrínseca (única)**.
3.  El estado intrínseco es mucho más grande que el extrínseco.
4.  La identidad de los objetos no es importante para el cliente.

Un ejemplo clásico son los caracteres en un editor de texto. Cada letra (A, B, C) es un flyweight. Su fuente, tamaño y métricas son el estado intrínseco. Su posición en el documento es el estado extrínseco.

---

## 6. Cómo Ejecutar el Ejemplo

Para que las importaciones funcionen correctamente, ejecuta el código como un módulo desde el directorio raíz del proyecto.

1.  **Sitúate en la raíz del proyecto:**
    ```bash
    cd /ruta/a/tu/proyecto/DesignPatterns
    ```

2.  **Ejecuta el módulo `main`:**
    ```bash
    python3 -m src.design_patterns.structual_patterns.flyweight_pattern.main
    ```

La salida mostrará cómo se plantan 10 árboles, pero al final, el `TreeFactory` informa que solo se crearon 3 objetos `TreeType`, demostrando el ahorro de memoria.
