# Patrón de Diseño: Template Method (Método Plantilla)

El patrón Template Method es un patrón de comportamiento que define el esqueleto de un algoritmo en una operación, delegando algunos pasos a las subclases. Permite que las subclases redefinean ciertos pasos de un algoritmo sin cambiar la estructura del mismo.

## Propósito Principal
- Definir un algoritmo como una serie de pasos y permitir que las subclases proporcionen la implementación para uno o más de esos pasos.

## Componentes
1.  **Clase Abstracta (Abstract Class):**
    - Contiene el `template_method()`, que define el esqueleto del algoritmo.
    - Este método llama a otros métodos para realizar los pasos del algoritmo.
    - Algunos de estos métodos pueden ser abstractos (deben ser implementados por las subclases), mientras que otros pueden tener una implementación por defecto (hooks).

2.  **Clase Concreta (Concrete Class):**
    - Hereda de la Clase Abstracta.
    - Implementa los pasos abstractos requeridos por el `template_method()`.
    - Opcionalmente, puede anular los `hooks` (métodos con implementación por defecto) para personalizar el comportamiento.

## Caso de Uso
Imagina un proceso de procesamiento de datos que sigue los mismos pasos generales: `leer datos`, `procesar datos` y `guardar datos`. El `template_method` se asegura de que estos pasos se ejecuten en el orden correcto. Las subclases concretas pueden implementar cómo se leen los datos (desde un CSV, una API, una base de datos) y cómo se procesan, sin alterar la secuencia del algoritmo.
