# Explicación Detallada del Patrón de Diseño Strategy

Este documento explica el código de ejemplo del patrón Strategy, diseñado para ser didáctico y fácil de entender.

## ¿Cuál es el objetivo del patrón Strategy?

El objetivo es permitirte definir una familia de algoritmos (o "estrategias"), poner cada uno en una clase separada y hacer que sus objetos sean intercambiables. Esto permite que el algoritmo que se usa pueda cambiar dinámicamente, sin que el código que lo utiliza (el "contexto") se vea afectado.

---

## Análisis del Código

Analicemos el código archivo por archivo para entender cómo se logra este objetivo.

### 1. `strategies.py`: El Corazón del Patrón

Este archivo define las "estrategias" intercambiables. Piensa en ellas como diferentes herramientas para hacer un mismo tipo de trabajo (en este caso, "exportar datos").

#### El Contrato: `ExportStrategy(Protocol)`

```python
from typing import Protocol, List, Dict, Any

class ExportStrategy(Protocol):
    def export(self, data: List[Dict[str, Any]]) -> str:
        ...
```

*   **`ExportStrategy`** es un **Protocolo**. No es una clase que haga algo, sino un **contrato** o una plantilla.
*   Define que cualquier objeto que se considere una "Estrategia de Exportación" **debe** tener un método llamado `export`.
*   Este es el pilar del **Principio de Inversión de Dependencias (DIP)**: nuestro código dependerá de esta "abstracción" y no de una implementación concreta.

#### Las Estrategias Concretas

```python
class JsonExportStrategy:
    def export(self, data: List[Dict[str, Any]]) -> str:
        # ... lógica para crear un JSON ...

class CsvExportStrategy:
    def export(self, data: List[Dict[str, Any]]) -> str:
        # ... lógica para crear un CSV ...

class HtmlExportStrategy:
    def export(self, data: List[Dict[str, Any]]) -> str:
        # ... lógica para crear una tabla HTML ...
```

*   Estas son las **estrategias concretas**. Cada una es una clase independiente que cumple con el contrato `ExportStrategy`.
*   Cada clase tiene una **única responsabilidad** (Principio de Responsabilidad Única - SRP): `JsonExportStrategy` solo sabe de JSON, `CsvExportStrategy` solo sabe de CSV, etc.

---

### 2. `context.py`: El Orquestador Ignorante

Este archivo define la clase que *utilizará* las estrategias. La llamamos "Contexto". La clave es que esta clase es "ignorante" de los detalles de cada estrategia.

```python
from .strategies import ExportStrategy

class ReportGenerator:
    def __init__(self, strategy: ExportStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: ExportStrategy):
        self._strategy = strategy

    def generate_report(self, data: List[Dict[str, Any]]) -> str:
        report = self._strategy.export(data)
        return report
```

*   **`__init__(self, strategy: ExportStrategy)`**: Aquí vemos la **Inyección de Dependencias (DI)**. El `ReportGenerator` no crea su propia estrategia, sino que la recibe desde fuera. Fíjate que el tipo esperado es `ExportStrategy`, la abstracción.
*   **`set_strategy(...)`**: Permite cambiar la herramienta (la estrategia) en cualquier momento, incluso después de que el `ReportGenerator` ya ha sido creado.
*   **`generate_report(...)`**: ¡Esta es la delegación! El `ReportGenerator` no sabe cómo se formatea el reporte. Simplemente le dice a la estrategia que tiene actualmente: "Toma estos datos y haz tu trabajo" (`self._strategy.export(data)`).

---

### 3. `main.py`: El Cliente que Toma las Decisiones

Este es el punto de entrada, el "cliente" que ensambla y dirige todo. Es el único que conoce todas las piezas y es responsable de:
1.  Crear las estrategias concretas.
2.  Crear el contexto (`ReportGenerator`).
3.  **Inyectar** la estrategia inicial en el contexto.
4.  Decidir cuándo cambiar de estrategia usando `set_strategy`.

---

## Cómo Ejecutar el Ejemplo

Para que las importaciones relativas (ej. `from .context ...`) funcionen correctamente, debes ejecutar el código como un módulo desde la carpeta raíz del proyecto.

**1. Posiciónate en la Raíz del Proyecto**

Abre tu terminal y asegúrate de estar en el directorio principal del proyecto.

```bash
cd /home/programar/Documentos/DesignPatterns
```

**2. Ejecuta el Módulo**

Usa el siguiente comando. La bandera `-m` le indica a Python que trate el archivo como parte de un paquete.

```bash
python3 -m src.solid_principles.patron_strategy.main
```

Esto ejecutará el script `main.py` y verás la demostración del patrón Strategy en tu consola.
