# Patrón de Diseño: Adapter (Adaptador)

Este documento ofrece una explicación didáctica del patrón **Adapter**, utilizando el código de este proyecto como referencia.

---

## 1. ¿Qué es el Patrón Adapter?

> El **Adapter** es un patrón de diseño estructural que permite que objetos con interfaces incompatibles colaboren entre sí. Actúa como un traductor o un envoltorio (wrapper) entre dos objetos, convirtiendo la interfaz de uno para que sea compatible con la del otro.

Imagina que tienes un enchufe europeo pero estás en Estados Unidos. No puedes conectar tus dispositivos directamente. Necesitas un adaptador de corriente que se conecte al enchufe de la pared (la interfaz que quieres usar) y ofrezca una ranura para tu enchufe europeo (la interfaz que tienes). El patrón Adapter hace exactamente eso en el software.

### ¿Qué Problema Resuelve?

Resuelve el problema de la incompatibilidad de interfaces. Es especialmente útil cuando:

- Quieres usar una clase existente, pero su interfaz no coincide con la que necesitas.
- Quieres integrar un componente de terceros sin modificar su código fuente.
- Necesitas que varias subclases trabajen con una clase que tiene una interfaz "extraña" o inconsistente.

---

## 2. Componentes del Patrón

| Componente | Rol | Archivo de Ejemplo |
| :--- | :--- | :--- |
| **Target (Objetivo)** | La interfaz que el cliente espera o con la que trabaja. | `legacy_system.py` -> La firma de `display_json(data: Dict)` |
| **Adaptee (Adaptado)** | La clase existente con una interfaz incompatible que necesita ser adaptada. | `modern_service.py` -> `XMLData` |
| **Adapter (Adaptador)** | La clase que envuelve al `Adaptee` y implementa la interfaz `Target`. | `adapter.py` -> `XMLToJSONAdapter` |
| **Client (Cliente)** | La clase que interactúa con el `Adapter` a través de la interfaz `Target`. | `main.py` -> `client_code` |

---

## 3. Análisis del Código de Ejemplo

En nuestro escenario, tenemos un `ModernService` que produce datos en formato `XMLData`, pero nuestro `legacy_system` solo entiende diccionarios de Python (simulando JSON).

### a. El `Adaptee`: `modern_service.py`

- **`XMLData`**: Es la clase que queremos adaptar. Contiene datos en un formato de cadena XML. Su interfaz (`xml_content`) es incompatible con lo que el cliente espera.

### b. El `Target`: `legacy_system.py`

- **`display_json(data: Dict)`**: Esta función representa la interfaz `Target`. El cliente tiene una referencia a esta función y quiere usarla, pero solo acepta diccionarios.

### c. El `Adapter`: `adapter.py`

- **`XMLToJSONAdapter`**: Esta es la clase clave.
    1.  **Envuelve al `Adaptee`**: En su constructor (`__init__`), recibe una instancia de `XMLData`.
    2.  **Implementa la interfaz `Target`**: Proporciona un método `to_dict()`. Este método es el que el cliente usará.
    3.  **Realiza la "traducción"**: Dentro de `to_dict()`, el adaptador toma el contenido XML del objeto `XMLData`, lo parsea y lo transforma en un diccionario de Python. Esta es la lógica central del adaptador.

### d. El `Client`: `main.py`

- El `client_code` orquesta todo:
    1.  Llama al `ModernService` y obtiene un objeto `XMLData`.
    2.  Se da cuenta de que no puede pasar este objeto directamente al `legacy_system`.
    3.  Crea una instancia de `XMLToJSONAdapter`, pasándole el objeto `XMLData`.
    4.  Llama al método `to_dict()` del adaptador para obtener una representación compatible (un diccionario).
    5.  Finalmente, pasa este diccionario al `legacy_system`, que ahora puede procesarlo correctamente.

El cliente queda desacoplado del `Adaptee`. Solo necesita conocer el `Adapter`.

---

## 4. Ventajas y Desventajas

### Ventajas

1.  **Principio de Responsabilidad Única (SRP)**: Separa la lógica de conversión de datos de las clases de negocio. El servicio moderno no necesita saber sobre el sistema antiguo, y viceversa.
2.  **Principio de Abierto/Cerrado (OCP)**: Puedes introducir nuevos adaptadores para integrar nuevas clases sin modificar el código cliente existente.
3.  **Reutilización de Código**: Permite reutilizar clases existentes que de otro modo serían incompatibles.

### Desventajas

1.  **Aumento de la Complejidad**: Introduce una nueva clase (el adaptador) en el sistema, lo que puede añadir una capa de indirección y complejidad si el sistema ya es muy enrevesado.

---

## 5. Adapter vs. Otros Patrones

| Patrón | Enfoque | Cuándo Usarlo |
| :--- | :--- | :--- |
| **Adapter** | **Convierte** una interfaz existente en otra que el cliente espera. | Para hacer que clases con interfaces incompatibles trabajen juntas. |
| **Bridge** | **Desacopla** una abstracción de su implementación para que ambas puedan evolucionar independientemente. | Cuando quieres evitar una explosión de subclases y permitir cambiar la implementación en tiempo de ejecución. |
| **Decorator** | **Añade** responsabilidades a un objeto dinámicamente sin alterar su interfaz. | Para extender la funcionalidad de un objeto sin usar la herencia. |
| **Facade** | **Simplifica** la interfaz de un subsistema complejo. | Para proporcionar un punto de entrada simple a un conjunto de clases. |

### Analogía para Recordar

- **Adapter (Traductor Universal):**
  - Estás en una reunión con alguien que solo habla japonés (`Adaptee`), pero tú solo entiendes español (`Target`).
  - Contratas a un traductor (`Adapter`).
  - Le hablas al traductor en español. Él se da la vuelta, le habla a la otra persona en japonés, escucha la respuesta en japonés y te la traduce de vuelta a español.
  - El traductor adapta la comunicación para que dos sistemas incompatibles puedan colaborar.

---

## 6. Cómo Ejecutar el Ejemplo

Para que las importaciones funcionen correctamente, ejecuta el código como un módulo desde el directorio raíz del proyecto.

1.  **Sitúate en la raíz del proyecto:**
    ```bash
    cd /ruta/a/tu/proyecto/DesignPatterns
    ```

2.  **Ejecuta el módulo `main`:**
    ```bash
    python3 -m src.design_patterns.structual_patterns.adapter_pattern.main
    ```

La salida mostrará cómo el servicio moderno obtiene los datos, cómo el adaptador los convierte y, finalmente, cómo el sistema antiguo los muestra en el formato JSON esperado.
