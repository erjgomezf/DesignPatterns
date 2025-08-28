# Patrón de Diseño: Decorator (Decorador)

Este documento ofrece una explicación didáctica del patrón **Decorator**, utilizando el código de este proyecto como referencia.

---

## 1. ¿Qué es el Patrón Decorator?

> El **Decorator** es un patrón de diseño estructural que permite añadir nuevas funcionalidades a objetos existentes sin alterar su estructura. Lo hace envolviendo el objeto original en un objeto "decorador" que comparte la misma interfaz.

En esencia, el patrón Decorator te permite "vestir" un objeto con nuevas responsabilidades. Puedes apilar decoradores uno encima de otro, y cada uno añade su propia funcionalidad.

### ¿Qué Problema Resuelve?

Imagina que tienes una clase y quieres añadirle varias funcionalidades opcionales. La herencia no es una buena solución, porque llevaría a una explosión de subclases para cada combinación posible (ej. `EmailNotifier`, `EmailAndSMSNotifier`, `EmailAndSlackNotifier`, `EmailAndSMSAndSlackNotifier`, etc.). El Decorator resuelve esto permitiendo añadir estas funcionalidades de forma dinámica y componible.

---

## 2. Componentes del Patrón

Analicemos las piezas clave del patrón y su correspondencia en nuestro código de ejemplo:

| Componente | Rol | Archivo de Ejemplo |
| :--- | :--- | :--- |
| **Component (Componente)** | Define la interfaz común para los objetos que pueden ser decorados y para los decoradores mismos. | `components.py` -> `Notifier` |
| **ConcreteComponent** | La clase del objeto original al que queremos añadirle funcionalidades. | `components.py` -> `EmailNotifier` |
| **Base Decorator** | Clase abstracta que implementa la interfaz `Component` y mantiene una referencia al objeto `Component` que envuelve. Delega las llamadas a este objeto. | `decorators.py` -> `BaseNotifierDecorator` |
| **ConcreteDecorator** | Implementación de un decorador específico. Añade su propia lógica antes o después de delegar la llamada al objeto envuelto. | `decorators.py` -> `SMSNotifierDecorator`, `SlackNotifierDecorator` |

---

## 3. Análisis del Código de Ejemplo

### a. La Interfaz y el Componente Concreto: `components.py`

- **`Notifier(Protocol)`**: Es la interfaz `Component`. Define el contrato que todos deben seguir: un método `send(message)`. Esto es clave para que el cliente pueda tratar a un objeto simple y a uno decorado de la misma manera (Principio de Sustitución de Liskov).

- **`EmailNotifier`**: Es el `ConcreteComponent`. Es nuestro objeto base, con la funcionalidad mínima: enviar una notificación por email.

### b. Los Decoradores: `decorators.py`

Este archivo contiene la lógica de "envoltura".

- **`BaseNotifierDecorator(Notifier, ABC)`**: Es el `Base Decorator`.
    - Hereda de `Notifier` para ser intercambiable con el componente original.
    - En su `__init__`, **recibe y almacena** una instancia de `Notifier`. Esta es la clave de la **composición**. El decorador *tiene un* notificador.
    - Su método `send()` simplemente delega la llamada al objeto envuelto (`self._wrapped_component.send(message)`).

- **`SMSNotifierDecorator` y `SlackNotifierDecorator`**: Son los `ConcreteDecorator`.
    - Heredan de `BaseNotifierDecorator`.
    - Sobrescriben el método `send()`.
    - **Añaden su propio comportamiento** (crear el string de la notificación de SMS o Slack).
    - **Delegan la llamada al objeto envuelto** usando `super().send(message)`. Esto crea una cadena de llamadas que va desde el decorador más externo hasta el componente concreto original.

### c. El Cliente: `main.py`

El cliente es el que orquesta la decoración.

- El `client_code` es agnóstico a los detalles. Recibe un objeto del tipo `Notifier` y simplemente llama a su método `send()`. No sabe si es un `EmailNotifier` simple o uno envuelto en múltiples decoradores.

- En `main()`, se muestra la magia del patrón:
    1. Se crea un `EmailNotifier` simple.
    2. Se "envuelve" con `SMSNotifierDecorator`.
    3. El resultado (`decorator1`) se vuelve a "envolver" con `SlackNotifierDecorator`.

Cuando se llama a `decorator2.send()`, ocurre esta cadena:
`SlackNotifierDecorator.send()` -> `SMSNotifierDecorator.send()` -> `EmailNotifier.send()`

---

## 4. Ventajas Principales

- **Cumplimiento del Principio Abierto/Cerrado (OCP):** Puedes añadir nuevas funcionalidades (nuevos decoradores) sin modificar el código de los componentes existentes.

- **Flexibilidad sobre la Herencia:** Evita la creación de una jerarquía de clases compleja. Puedes combinar funcionalidades de forma flexible en tiempo de ejecución.

- **Responsabilidades Separadas (SRP):** Cada decorador tiene una única responsabilidad (ej. notificar por SMS).

## 5. Decorator vs. Strategy: Una Diferencia Clave

- **Decorator:** Su objetivo es **añadir o alterar responsabilidades** de un objeto. Cambia la "piel" de un objeto.
- **Strategy:** Su objetivo es **cambiar un algoritmo interno** completo. Cambia las "entrañas" de un objeto.

En nuestro ejemplo de `Strategy`, el `ReportGenerator` *tenía una* estrategia de exportación y la usaba. Aquí, el `SMSNotifierDecorator` *es un* notificador que, además, *tiene otro* notificador dentro.

---

## 6. Cómo Ejecutar el Ejemplo

Para que las importaciones funcionen, ejecuta el código como un módulo desde el directorio raíz del proyecto.

1.  **Sitúate en la raíz del proyecto:**
    ```bash
    cd /ruta/a/tu/proyecto/DesignPatterns
    ```

2.  **Ejecuta el módulo `main`:**
    ```bash
    python3 -m src.design_patterns.structual_patterns.decorator_pattern.main
    ```

Esto correrá el `client_code`, que demostrará cómo se puede "decorar" un notificador simple con funcionalidades adicionales de forma dinámica.