# Patrón de Diseño: Factory Method (Método de Fábrica)

Este documento ofrece una explicación didáctica del patrón **Factory Method**, utilizando el código de este proyecto como referencia.

---

## 1. ¿Qué es el Patrón Factory Method?

> El **Factory Method** es un patrón de diseño creacional que propone una interfaz para crear objetos en una superclase, pero delega la decisión de qué tipo de objeto crear a las subclases.

En esencia, permite que una clase delegue la instanciación a sus hijas, desacoplando el código cliente de las clases de productos concretos.

### ¿Qué Problema Resuelve?

Resuelve el acoplamiento directo entre el código cliente y las clases concretas que necesita instanciar. El cliente solo necesita conocer la interfaz abstracta del producto y del creador, promoviendo un diseño más flexible y extensible.

---

## 2. Componentes del Patrón

Analicemos las piezas clave del patrón y su correspondencia en nuestro código de ejemplo:

| Componente | Rol | Archivo de Ejemplo |
| :--- | :--- | :--- |
| **Product (Producto)** | Define la interfaz común para todos los objetos que la fábrica puede crear. | `transport.py` -> `Transport` |
| **ConcreteProduct** | Implementación concreta de la interfaz `Product`. Son los objetos reales. | `transport.py` -> `Truck`, `Ship` |
| **Creator (Creador)** | Declara el *Factory Method* (`create_transport`), que devuelve un objeto `Product`. | `logistics.py` -> `Logistics` |
| **ConcreteCreator** | Sobrescribe el *Factory Method* para devolver una instancia de un `ConcreteProduct` específico. | `logistics.py` -> `RoadLogistics`, `SeaLogistics` |

---

## 3. Análisis del Código de Ejemplo

### a. Los Productos: `transport.py`

- **`Transport(Protocol)`**: Actúa como la interfaz `Product`. Define el contrato que todos los transportes deben cumplir: un método `deliver()`.
- **`Truck` y `Ship`**: Son los `ConcreteProduct`. Cada uno implementa `deliver()` con su propia lógica (ej. "entregando por tierra en un camión").

### b. Los Creadores: `logistics.py`

- **`Logistics(ABC)`**: Es el `Creator` abstracto.
    - Define el **Factory Method** abstracto: `@abstractmethod def create_transport(self) -> Transport:`. Esto obliga a las subclases a decidir qué objeto crear.
    - Contiene lógica de negocio (`plan_delivery`) que opera sobre la interfaz `Transport`. Es importante notar que `plan_delivery` no sabe si trabaja con un `Truck` o un `Ship`, solo con un `Transport`.

- **`RoadLogistics` y `SeaLogistics`**: Son los `ConcreteCreator`.
    - Cada uno implementa `create_transport` y devuelve un producto concreto diferente: `Truck()` o `Ship()`. Aquí reside la decisión de instanciación.

### c. El Cliente: `main.py`

- El `client_code` es agnóstico a los detalles. Recibe una abstracción (`Logistics`) y llama a su lógica de negocio (`plan_delivery`).
- No sabe qué tipo de logística se usa ni qué transporte se crea. Está **totalmente desacoplado** de las implementaciones concretas.

---

## 4. Ventaja Principal: Cumplimiento del Principio Abierto/Cerrado (OCP)

La fortaleza del Factory Method es que **desacopla el código cliente de las clases concretas**.

> El `client_code` en `main.py` solo conoce la abstracción `Logistics`. No tiene idea de que existen `Truck` o `Ship`. Delega la responsabilidad de la creación a la subclase que se le proporciona (`RoadLogistics` o `SeaLogistics`).

Esto es una implementación perfecta del **Principio de Abierto/Cerrado**:
- **Abierto a la extensión:** Si necesitamos añadir transporte por tren, creamos `Train` y `TrainLogistics`.
- **Cerrado a la modificación:** No es necesario cambiar ni una línea del `client_code` o de la clase base `Logistics`. La lógica existente sigue funcionando sin alteraciones.

---

## 5. Factory Method vs. Strategy: Una Diferencia Clave

Aunque ambos patrones aumentan la flexibilidad, su propósito es distinto.

| Característica | Factory Method (Método de Fábrica) | Strategy (Estrategia) |
| :--- | :--- | :--- |
| **Propósito** | **Creacional**: ¿**CÓMO** se crea un objeto? | **De Comportamiento**: ¿**CÓMO** un objeto hace algo? |
| **Enfoque** | Delega la instanciación a subclases. | Permite intercambiar algoritmos en un objeto existente. |
| **Estructura** | Basado en **herencia**. | Basado en **composición** y delegación. |
| **Flexibilidad** | La decisión se toma al instanciar la fábrica. Una `RoadLogistics` *siempre* creará un `Truck`. | El algoritmo se puede cambiar en tiempo de ejecución en el mismo objeto de contexto. |

### Analogía para Recordar

- **Factory Method (Franquicia de Restaurantes):**
  - Una franquicia "Burger World" (`Logistics`) tiene sucursales. La de Texas (`RoadLogistics`) *siempre* hace una "BBQ Burger" (`Truck`). La de Hawái (`SeaLogistics`) *siempre* hace una "Aloha Burger" (`Ship`).
  - Como cliente, eliges la sucursal, y esa sucursal decide el producto. No puedes pedirle a la sucursal de Texas que te haga una Aloha Burger.

- **Strategy (Chef con Varios Libros de Cocina):**
  - Un Chef (`Contexto`) tiene un método "preparar plato".
  - A su lado, tiene libros de cocina: "Cocina Italiana", "Francesa", "Japonesa" (`Estrategias`).
  - Hoy, el *mismo chef* usa el libro de cocina italiana. Mañana, ese *mismo chef* puede usar el libro de cocina japonesa para preparar un plato totalmente diferente. El comportamiento es intercambiable.

---

## 6. Cómo Ejecutar el Ejemplo

Para que las importaciones funcionen, ejecuta el código como un módulo desde el directorio raíz del proyecto.

1.  **Sitúate en la raíz del proyecto:**
    ```bash
    cd /ruta/a/tu/proyecto/DesignPatterns
    ```

2.  **Ejecuta el módulo `main`:**
    ```bash
    python3 -m src.solid_principles.pattern.factory_pattern.main
    ```

Esto correrá el `client_code`, que demostrará cómo puede operar con diferentes fábricas para obtener distintos resultados sin cambiar su propia lógica.
