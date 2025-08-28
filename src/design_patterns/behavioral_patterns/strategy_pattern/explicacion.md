# Patrón de Diseño: Strategy (Estrategia)

Este documento ofrece una explicación didáctica del patrón **Strategy**, utilizando el código de este proyecto como referencia.

---

## 1. ¿Qué es el Patrón Strategy?

> El **Strategy** es un patrón de diseño de comportamiento que te permite definir una familia de algoritmos, colocar cada uno de ellos en una clase separada y hacer sus objetos intercambiables.

Imagina que tienes que ir de un punto A a un punto B. Puedes ir en coche, en bicicleta o caminando. Cada una es una "estrategia" de viaje diferente. El patrón Strategy te permite elegir qué estrategia usar en tiempo de ejecución. En lugar de tener un método gigante con `if (modo == 'coche') ... elif (modo == 'bici') ...`, tienes objetos separados para cada estrategia.

### ¿Qué Problema Resuelve?

- **Elimina condicionales complejos**: Reemplaza largas cadenas de `if-elif-else` que seleccionan variantes de un mismo algoritmo.
- **Cumple el Principio de Abierto/Cerrado (OCP)**: Puedes introducir nuevas estrategias sin modificar el código del objeto que las utiliza (el "contexto").
- **Flexibilidad**: Permite al cliente elegir el algoritmo que se va a usar en tiempo de ejecución.

---

## 2. Componentes del Patrón

| Componente | Rol | Archivo de Ejemplo |
| :--- | :--- | :--- |
| **Strategy (Estrategia)** | La interfaz común a todos los algoritmos soportados. | `export_strategy.py` -> `ExportStrategy` |
| **ConcreteStrategy** | Implementa un algoritmo específico siguiendo la interfaz `Strategy`. | `concrete_strategies.py` -> `JSONExportStrategy`, `CSVExportStrategy` |
| **Context (Contexto)** | La clase que utiliza una estrategia. Mantiene una referencia a un objeto `Strategy` y se comunica con él a través de su interfaz. | `report_generator.py` -> `ReportGenerator` |

---

## 3. Análisis del Código de Ejemplo

Nuestro ejemplo implementa un generador de reportes que puede exportar datos en diferentes formatos (JSON, CSV) usando distintas estrategias.

### a. La Interfaz `Strategy` y las Estrategias Concretas

- **`ExportStrategy(Protocol)`**: Define la interfaz. Cualquier estrategia de exportación debe tener un método `export(data)`.
- **`JSONExportStrategy` y `CSVExportStrategy`**: Son las `ConcreteStrategy`. Cada una implementa el método `export` con la lógica específica para generar su formato.

### b. El `Context`

- **`ReportGenerator`**: Es el `Context`.
    1.  **No conoce los detalles**: No sabe cómo se genera un JSON o un CSV. Su única responsabilidad es gestionar los datos y delegar la tarea de exportación.
    2.  **Mantiene una referencia a la estrategia**: Tiene un atributo `_strategy` que almacena el objeto de la estrategia actual.
    3.  **Permite cambiar la estrategia**: El método `set_strategy()` permite al cliente cambiar la estrategia en cualquier momento.
    4.  **Delega la ejecución**: El método `generate_report()` simplemente llama a `self._strategy.export()`.

### c. El `Client`: `main.py`

- El `client_code` crea una instancia del `ReportGenerator`.
- Luego, crea una instancia de la estrategia deseada (`JSONExportStrategy` o `CSVExportStrategy`) y la establece en el generador.
- Finalmente, llama a `generate_report()`, y el generador utiliza la estrategia que se le haya configurado en ese momento.

---

## 4. Ventajas y Desventajas

### Ventajas

1.  **Intercambio de algoritmos en tiempo de ejecución**: Puedes cambiar la forma en que un objeto realiza una tarea.
2.  **Aislamiento de la lógica**: La lógica de cada algoritmo está en su propia clase, cumpliendo con el Principio de Responsabilidad Única (SRP).
3.  **Extensibilidad**: Añadir un nuevo formato de exportación es tan simple como crear una nueva clase de estrategia.

### Desventajas

1.  **Aumento del número de clases**: Si solo tienes un par de algoritmos que rara vez cambian, el patrón puede ser excesivo.

---

## 5. Strategy vs. State

| Patrón | Intención | ¿Quién dirige el cambio? |
| :--- | :--- | :--- |
| **Strategy** | Encapsular algoritmos intercambiables para una tarea. | El **cliente** suele decidir qué estrategia usar. |
| **State** | Permitir que un objeto cambie su comportamiento cuando su estado interno cambia. | El **contexto** o los propios **estados** deciden la transición al siguiente estado. |

---

## 6. Cómo Ejecutar el Ejemplo

Para que las importaciones funcionen correctamente, ejecuta el código como un módulo desde el directorio raíz del proyecto.

1.  **Sitúate en la raíz del proyecto:**
    ```bash
    cd /ruta/a/tu/proyecto/DesignPatterns
    ```

2.  **Ejecuta el módulo `main`:**
    ```bash
    python3 -m src.design_patterns.behavioral_patterns.strategy_pattern.main
    ```
