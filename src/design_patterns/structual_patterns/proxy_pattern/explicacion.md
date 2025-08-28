# Patrón de Diseño: Proxy

Este documento ofrece una explicación didáctica del patrón **Proxy**, utilizando el código de este proyecto como referencia.

---

## 1. ¿Qué es el Patrón Proxy?

> El **Proxy** es un patrón de diseño estructural que proporciona un **sustituto o intermediario** para otro objeto con el fin de controlar el acceso a este. El proxy tiene la misma interfaz que el objeto original, lo que le permite al cliente interactuar con él de manera transparente.

Imagina que tienes una tarjeta de crédito. La tarjeta no es el dinero en sí, sino un **proxy** para tu cuenta bancaria. Te permite acceder al dinero (el objeto real), pero también añade una capa de control: puedes tener límites de gasto, protección contra fraudes y un registro de transacciones. No interactúas directamente con el fajo de billetes en la bóveda del banco; usas el proxy.

### ¿Qué Problema Resuelve?

El patrón Proxy se utiliza para añadir una capa de indirección al acceso a un objeto. Esto es útil para:

- **Virtual Proxy (Inicialización Diferida)**: Retrasar la creación de un objeto que consume muchos recursos hasta que realmente se necesite.
- **Remote Proxy (Proxy Remoto)**: Representar un objeto que se encuentra en un espacio de direcciones diferente (ej. en otro servidor en la red).
- **Protection Proxy (Proxy de Protección)**: Controlar el acceso al objeto original, verificando si el cliente tiene los permisos necesarios.
- **Smart Proxy (Proxy Inteligente)**: Realizar acciones adicionales cuando se accede al objeto, como contar referencias (para liberar memoria) o implementar caching (como en nuestro ejemplo).

---

## 2. Componentes del Patrón

| Componente | Rol | Archivo de Ejemplo |
| :--- | :--- | :--- |
| **Subject (Asunto)** | La interfaz común tanto para el `RealSubject` como para el `Proxy`. | `database_service.py` -> `DatabaseService` |
| **RealSubject (Asunto Real)** | La clase que contiene la lógica de negocio principal y que a menudo consume muchos recursos. | `real_database_service.py` -> `RealDatabaseService` |
| **Proxy** | El intermediario que controla el acceso al `RealSubject`. Mantiene una referencia al `RealSubject` y puede gestionar su creación y eliminación. | `database_proxy.py` -> `DatabaseProxy` |
| **Client (Cliente)** | Interactúa con los objetos a través de la interfaz `Subject`, sin saber si está hablando con el objeto real o con un proxy. | `main.py` -> `client_code` |

---

## 3. Análisis del Código de Ejemplo

Nuestro ejemplo implementa un **Proxy Inteligente** que actúa como un **Proxy de Protección** y también proporciona **caching** para un servicio de base de datos costoso.

### a. El `Subject` y el `RealSubject`

- **`DatabaseService(ABC)`**: Es la interfaz `Subject`. Define el método `request_data()`, que es la única forma en que el cliente interactuará con el servicio.
- **`RealDatabaseService`**: Es el `RealSubject`. Su método `request_data()` simula una operación muy costosa (una pausa de 2 segundos) antes de devolver los datos. Queremos evitar llamar a este método innecesariamente.

### b. El `Proxy`

- **`DatabaseProxy`**: Es el corazón del patrón.
    1.  **Misma Interfaz**: Implementa la interfaz `DatabaseService`, por lo que es intercambiable con el `RealDatabaseService`.
    2.  **Referencia al RealSubject**: En su constructor, recibe una instancia del `RealDatabaseService`.
    3.  **Proxy de Protección**: El método `check_access()` simula una lógica de permisos. Antes de delegar la llamada, el proxy verifica si el usuario tiene el rol de "admin". Si no, deniega el acceso sin siquiera tocar el `RealSubject`.
    4.  **Caching (Proxy Inteligente)**: En `request_data()`, antes de delegar la llamada al objeto real, el proxy revisa su caché interna (`_cache`).
        - Si los datos para una consulta ya están en la caché, los devuelve inmediatamente, ahorrando el coste de la llamada a la base de datos.
        - Si no están en la caché, delega la llamada al `_real_service`, almacena el resultado en la caché para futuras peticiones y luego lo devuelve al cliente.

### c. El `Client`

- El `client_code` es agnóstico. Recibe un objeto de tipo `DatabaseService` y llama a `request_data()`.
- No sabe si está tratando con el objeto real o con el proxy. Esta transparencia es una de las mayores ventajas del patrón.
- En la demostración, vemos cómo el proxy primero deniega el acceso a un usuario no autorizado. Luego, para el usuario autorizado, la primera llamada es lenta (porque el proxy delega en el `RealSubject`), pero la segunda es instantánea (porque los datos provienen de la caché del proxy).

---

## 4. Ventajas y Desventajas

### Ventajas

1.  **Control sobre el Objeto Real**: Puedes gestionar el ciclo de vida del objeto real y realizar acciones antes o después de que se acceda a él sin que el cliente lo sepa.
2.  **Mejora del Rendimiento**: La inicialización diferida y el caching pueden mejorar significativamente el rendimiento de la aplicación.
3.  **Seguridad**: El proxy de protección centraliza el control de acceso en un solo lugar.
4.  **Principio de Abierto/Cerrado**: Puedes introducir nuevos proxies sin cambiar el `RealSubject` o el código cliente.

### Desventajas

1.  **Aumento de la Complejidad**: Introduce una nueva clase, lo que puede complicar el código si se abusa del patrón.
2.  **Respuestas Retrasadas**: El proxy puede introducir un pequeño retardo en la respuesta debido a la indirección.

---

## 5. Proxy vs. Decorator

Ambos patrones envuelven a un objeto, pero su intención es diferente.

| Patrón | Intención | Interfaz |
| :--- | :--- | :--- |
| **Proxy** | **Controlar el acceso** a un objeto. | Implementa la **misma interfaz** que el objeto real. El cliente no sabe que está usando un proxy. |
| **Decorator** | **Añadir funcionalidades** a un objeto. | Implementa la misma interfaz, pero su propósito es **apilar** responsabilidades. Puedes envolver un objeto con múltiples decoradores. |

En resumen: usa **Proxy** cuando quieras gestionar el ciclo de vida o el acceso a un objeto de forma transparente. Usa **Decorator** cuando quieras añadir comportamiento a un objeto sin afectar a otros objetos de la misma clase.

---

## 6. Cómo Ejecutar el Ejemplo

Para que las importaciones funcionen correctamente, ejecuta el código como un módulo desde el directorio raíz del proyecto.

1.  **Sitúate en la raíz del proyecto:**
    ```bash
    cd /ruta/a/tu/proyecto/DesignPatterns
    ```

2.  **Ejecuta el módulo `main`:**
    ```bash
    python3 -m src.design_patterns.structual_patterns.proxy_pattern.main
    ```

La salida demostrará claramente el control de acceso y el mecanismo de caching, mostrando cómo la segunda llamada a la misma consulta es instantánea.
