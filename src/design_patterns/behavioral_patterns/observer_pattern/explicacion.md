# Patrón de Diseño: Observer (Observador)

Este documento ofrece una explicación didáctica del patrón **Observer**, utilizando el código de este proyecto como referencia.

---

## 1. ¿Qué es el Patrón Observer?

> El **Observer** es un patrón de diseño de comportamiento que define una dependencia de uno a muchos entre objetos, de modo que cuando un objeto (el "sujeto") cambia su estado, todos sus dependientes (los "observadores") son notificados y actualizados automáticamente.

En pocas palabras, permite que un objeto publique cambios en su estado y que otros objetos se suscriban para recibir esas notificaciones. Es la base de muchos sistemas de eventos.

### ¿Qué Problema Resuelve?

Imagina que tienes un objeto (ej. un `SensorDeTemperatura`) y varios otros objetos (ej. una `Pantalla`, un `Termostato`, una `AppMovil`) que necesitan reaccionar cuando la temperatura cambia. Sin el patrón Observer, el sensor tendría que conocer y llamar directamente a cada uno de esos objetos, creando un acoplamiento muy fuerte y difícil de mantener.

El patrón Observer invierte esta lógica: los objetos interesados se "suscriben" al sensor, y el sensor simplemente notifica a su lista de suscriptores sin necesidad de saber quiénes son concretamente.

---

## 2. Componentes del Patrón

| Componente | Rol | Archivo de Ejemplo |
| :--- | :--- | :--- |
| **Subject (Sujeto)** | Interfaz que define métodos para gestionar suscriptores (`attach`, `detach`) y para notificarles (`notify`). | `subjects.py` -> `Subject` |
| **ConcreteSubject** | Implementa la interfaz `Subject`. Mantiene el estado de interés y notifica a los observadores cuando este cambia. | `subjects.py` -> `WeatherStation` |
| **Observer (Observador)** | Interfaz que define el método de actualización (`update`) que el sujeto llamará para notificar un cambio. | `observers.py` -> `Observer` |
| **ConcreteObserver** | Implementa la interfaz `Observer`. Define la acción a tomar cuando es notificado. | `observers.py` -> `TemperatureDisplay`, `FanController` |

---

## 3. Análisis del Código de Ejemplo

### a. Las Interfaces y el Sujeto Concreto: `subjects.py`

- **`Subject(ABC)`**: Es la interfaz del `Sujeto`. Define el contrato para cualquier objeto que quiera ser observable: debe poder agregar, quitar y notificar observadores.
- **`WeatherStation(Subject)`**: Es el `ConcreteSubject`.
    - Mantiene una lista `_observers` y el estado importante (`_temperature`).
    - **`attach()` y `detach()`**: Métodos para gestionar la lista de suscriptores.
    - **`notify()`**: Recorre la lista de observadores y llama al método `update()` de cada uno, pasándose a sí mismo como argumento para que el observador pueda obtener el estado actualizado.
    - **`set_temperature()`**: Este es el método que modifica el estado. Lo más importante es que, después de cambiar la temperatura, **llama a `notify()`** para desencadenar las actualizaciones.

### b. Los Observadores: `observers.py`

- **`Observer(ABC)`**: Es la interfaz del `Observador`. Define un único método, `update()`, que será llamado por el sujeto.
    > La firma `update(self, subject: Subject)` es clave. El observador recibe una referencia al sujeto que lo notificó, lo que le permite consultar su estado actual.

- **`TemperatureDisplay` y `FanController`**: Son los `ConcreteObserver`.
    - Cada uno implementa `update()` con su propia lógica.
    - `TemperatureDisplay` simplemente imprime la nueva temperatura.
    - `FanController` tiene una lógica más compleja: comprueba si la temperatura supera un umbral para decidir si enciende o apaga un ventilador.
    - Ambos están **completamente desacoplados** entre sí y del `WeatherStation`. No saben nada de la implementación interna del sujeto, solo que pueden llamar a `subject.temperature`.

### c. El Cliente: `main.py`

El cliente configura el sistema:
1.  Crea la instancia del sujeto (`WeatherStation`).
2.  Crea las instancias de los observadores (`TemperatureDisplay`, `FanController`).
3.  **Suscribe** los observadores al sujeto usando el método `attach()`.
4.  Simula cambios de estado llamando a `weather_station.set_temperature()`. Cada llamada desencadena las notificaciones y se puede ver la reacción de cada observador en la consola.
5.  Demuestra cómo se puede `detach()` un observador para que deje de recibir notificaciones.

---

## 4. Ventajas Principales

- **Desacoplamiento (Loose Coupling):** El sujeto y los observadores no están fuertemente acoplados. El sujeto solo conoce la interfaz `Observer`, no las clases concretas. Los observadores pueden ser añadidos o eliminados en cualquier momento sin modificar al sujeto.
- **Principio Abierto/Cerrado (OCP):** Puedes introducir nuevos tipos de observadores en el sistema sin cambiar el código del sujeto.
- **Relaciones Dinámicas:** Las relaciones entre sujetos y observadores se pueden establecer y modificar en tiempo de ejecución.

---

## 5. Cómo Ejecutar el Ejemplo

Para que las importaciones funcionen, ejecuta el código como un módulo desde el directorio raíz del proyecto.

1.  **Sitúate en la raíz del proyecto:**
    ```bash
    cd /ruta/a/tu/proyecto/DesignPatterns
    ```

2.  **Ejecuta el módulo `main`:**
    ```bash
    python3 -m src.design_patterns.behavioral_patterns.observer_pattern.main
    ```

Esto correrá el `main()`, que demostrará cómo los cambios en la estación meteorológica notifican automáticamente a todos los dispositivos suscritos.