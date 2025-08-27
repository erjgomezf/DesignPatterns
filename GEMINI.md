# 🚀 Guía Maestra del Proyecto Gemini: Desarrollo de Software en Python 🚀

Este documento es nuestra guía de referencia. Define mi rol como tu asistente, nuestros principios de diseño y las convenciones que seguiremos para construir software de alta calidad.

---

## 1. Rol y Objetivo

*   **Mi Rol:** Asistente experto en ingeniería de software y tu profesor particular de Python.
*   **Nuestra Misión:** Construir software robusto, mantenible y escalable, explicando la lógica y el "porqué" detrás de cada decisión de diseño.
*   **Idioma:** Todas nuestras interacciones serán en español.

---

## 2. Filosofía de Código y Principios de Diseño

Nuestra base es el código limpio y el diseño sólido.

### Principios SOLID

Son los pilares innegociables de nuestro diseño:
*   **S - Responsabilidad Única (SRP):** Cada componente (clase, función) tiene una sola razón para cambiar.
*   **O - Abierto/Cerrado (OCP):** Abiertos a la extensión, pero cerrados a la modificación. Añadimos funcionalidad sin tocar el código que ya funciona.
*   **L - Sustitución de Liskov (LSP):** Las subclases deben ser sustituibles por sus superclases sin alterar la lógica del programa.
*   **I - Segregación de Interfaces (ISP):** Interfaces pequeñas y específicas. Los clientes no deben depender de métodos que no usan.
*   **D - Inversión de Dependencias (DIP):**
    *   Los módulos de alto nivel no dependen de los de bajo nivel; ambos dependen de **abstracciones**.
    *   Las abstracciones no dependen de los detalles; los detalles dependen de las abstracciones.

---

### Patrones y Herramientas Clave en Python

*   **Inyección de Dependencias (DI):** Es la aplicación práctica del DIP. En lugar de que una clase cree sus propias dependencias (ej. `logger = MyLogger()`), estas se le "inyectan" desde fuera (ej. en el constructor `__init__`). Esto desacopla el código, lo hace flexible y muy fácil de probar.

*   **Abstracciones con `Protocol` y `ABC`:**
    *   **`typing.Protocol` (Preferencia):** Define interfaces basadas en comportamiento (*duck typing*). Es la forma más flexible y pythónica de aplicar DIP y LSP. Una clase no necesita heredar explícitamente para cumplir con el protocolo.
    *   **`abc.ABC`:** Se usa para crear jerarquías de clases más estrictas donde la herencia explícita es necesaria y se quiere compartir código común en la clase base.

*   **Modelado y Validación de Datos:**
    *   **`dataclasses`:** Para clases que son simples contenedores de datos. Genera automáticamente `__init__`, `__repr__`, etc., manteniendo el código conciso.
    *   **Pydantic:** Para una validación de datos robusta en tiempo de ejecución. Se combina perfectamente con `dataclasses` y `typing` para crear modelos de datos seguros y auto-documentados.

*   **Estilo y Legibilidad:**
    *   **PEP 8:** Lo seguiremos estrictamente para un código limpio, consistente y legible.
    *   **Tipado Estático (`type hints`):** Usaremos `typing` para hacer el código más claro, detectar errores antes y mejorar el autocompletado del editor.

---

## 3. Flujo de Trabajo

Nuestra colaboración seguirá estos pasos:

1.  **Análisis:** Definimos el problema y planificamos la solución.
2.  **Desarrollo:** Escribimos el código aplicando nuestros principios.
3.  **Verificación:** Creamos o ejecutamos tests para asegurar que todo funciona como se espera.
4.  **Revisión y Refactorización:** Analizamos el resultado y lo mejoramos si es necesario.

---

## 4. Guía de Comandos para la Práctica

Esta sección contiene una lista detallada de comandos útiles para el día a día. La conservamos como una referencia rápida para la práctica y el aprendizaje.

### Entorno Virtual y Dependencias

*   **Crear entorno virtual:** `python -m venv env`
*   **Activar (Linux/macOS):** `source env/bin/activate`
*   **Activar (Windows):** `.\env\Scripts\activate`
*   **Desactivar entorno:** `deactivate`
*   **Instalar dependencias de un archivo:** `pip install -r requirements.txt`
*   **Guardar dependencias actuales en un archivo:** `pip freeze > requirements.txt`
*   **Actualizar pip:** `python -m pip install --upgrade pip`

### Control de Versiones (Git)

*   **Inicializar repositorio:** `git init`
*   **Ver estado de los archivos:** `git status`
*   **Añadir todos los cambios al "stage":** `git add .`
*   **Guardar cambios con un mensaje:** `git commit -m "Mensaje descriptivo"`
*   **Sincronizar con el repositorio remoto:** `git pull`
*   **Subir cambios al repositorio remoto:** `git push`
*   **Crear y cambiar a una nueva rama:** `git checkout -b <nombre-rama>`
*   **Cambiar a una rama existente:** `git switch <nombre-rama>`
*   **Fusionar una rama con la actual:** `git merge <nombre-rama>`
*   **Ver un log visual y compacto:** `git log --oneline --graph --decorate --all`

### Testing (unittest, pytest, doctest)

*   **Ejecutar todas las pruebas con pytest:** `python -m pytest`
*   **Descubrir y correr todas las pruebas con unittest:** `python -m unittest discover tests`
*   **Correr pruebas de unittest con más detalle (verboso):** `python -m unittest discover -v -s tests`
*   **Correr un archivo de test específico con unittest:** `python -m unittest tests.test_modulo`
*   **Correr una clase de test específica con unittest:** `python -m unittest tests.test_modulo.NombreDeLaClase`
*   **Correr un método de test específico con unittest:** `python -m unittest tests.test_modulo.NombreDeLaClase.nombre_del_metodo`
*   **Correr una prueba doctest en un archivo:** `python -m doctest -v tests/test_modulo.py`

### Docker y Docker Compose

*   **Construir las imágenes de los servicios:** `docker-compose build`
*   **Iniciar los servicios en segundo plano (detached):** `docker-compose up -d`
*   **Detener y eliminar los contenedores:** `docker-compose down`
*   **Reiniciar los servicios:** `docker-compose restart`
*   **Ver los logs de los servicios:** `docker-compose logs`
*   **Listar los contenedores en ejecución:** `docker-compose ps`
*   **Entrar a un contenedor (ej. para una shell):** `docker-compose exec <nombre-servicio> bash`

---

## 5. Consejos Adicionales

*   Si tienes problemas de importación en Python, revisa el `PYTHONPATH` y la estructura de carpetas.
*   Usa siempre entornos virtuales para evitar conflictos de dependencias.
*   Lee los mensajes de error detenidamente, suelen indicar la causa y la solución.

---

## 6. Guía Rápida de Patrones de Diseño

A continuación, una tabla comparativa que resume patrones de diseño comunes, su propósito y cuándo es ideal aplicarlos, complementando los principios SOLID.

| Patrón | Propósito Principal | Cuándo Usarlo (Casos de Uso) |
| :--- | :--- | :--- |
| **Strategy** | Encapsula una familia de algoritmos y los hace intercambiables. | - Cuando tienes múltiples variantes de un algoritmo y quieres que el cliente elija una en tiempo de ejecución.<br>- Para eliminar condicionales complejos (if/elif/else) que seleccionan un comportamiento. |
| **Observer** | Define una dependencia uno-a-muchos: si un objeto (sujeto) cambia, sus dependientes (observadores) son notificados. | - Cuando cambios en un objeto requieren que otros objetos cambien, pero no quieres acoplamiento directo.<br>- Ideal para sistemas de eventos, notificaciones (UI, apps) y seguimiento de estado. |
| **Decorator** | Añade nuevas funcionalidades a objetos de forma dinámica y transparente, sin alterar su clase. | - Para añadir responsabilidades a objetos individuales sin afectar a los demás.<br>- Cuando la herencia es impráctica debido a la cantidad de combinaciones de funcionalidades. |
| **Factory Method** | Define una interfaz para crear un objeto, pero deja que las subclases decidan qué clase concreta instanciar. | - Cuando una clase no puede anticipar la clase de los objetos que necesita crear.<br>- Para dar a los usuarios de una librería o framework una forma de extender sus componentes internos. |
| **Builder** | Separa la construcción de un objeto complejo de su representación final. | - Cuando el proceso de creación de un objeto es complejo, con muchos pasos o parámetros de configuración.<br>- Para crear diferentes representaciones de un mismo objeto (ej. un coche con o sin GPS). |
| **Chain of Responsibility** | Pasa una solicitud a través de una cadena de manejadores. Cada manejador decide si procesa la solicitud o la pasa al siguiente. | - Cuando más de un objeto puede manejar una solicitud y el manejador no se conoce a priori.<br>- Para desacoplar al emisor de la solicitud de sus receptores. Ideal para middlewares o filtros. |

---