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

A continuación, se presentan tablas comparativas que resumen los patrones de diseño clave, agrupados por su categoría, para una referencia rápida.

### Patrones Creacionales
*Se centran en los mecanismos de creación de objetos, tratando de crear objetos de una manera adecuada a la situación.*

| Patrón | Propósito Principal | Cuándo Usarlo (Casos de Uso) |
| :--- | :--- | :--- |
| **Singleton** | Garantizar una única instancia de una clase. | Controlar el ciclo de vida y el acceso a un recurso único (ej. conexión a BD, gestor de configuración). |
| **Factory Method** | Delegar la creación de objetos a subclases. | Crear un objeto sin especificar la clase exacta, permitiendo que las subclases decidan. |
| **Abstract Factory** | Crear familias de objetos relacionados o dependientes. | Producir conjuntos de objetos que deben funcionar juntos (ej. UI para Windows y macOS). |
| **Builder** | Construir un objeto complejo paso a paso. | Separar la construcción de la representación final, permitiendo diferentes configuraciones. |
| **Prototype** | Crear nuevos objetos copiando un prototipo existente. | Clonar un objeto pre-configurado para evitar un proceso de creación costoso. |

### Patrones Estructurales
*Se centran en cómo las clases y los objetos se componen para formar estructuras más grandes y flexibles.*

| Patrón | Intención Principal | Foco | Analogía |
| :--- | :--- | :--- | :--- |
| **Adapter** | Convertir una interfaz en otra. | Hacer que dos cosas incompatibles funcionen juntas. | Traductor de idiomas. |
| **Bridge** | Desacoplar abstracción de implementación. | Dividir una jerarquía monolítica en dos independientes. | Interruptor de luz y aparato eléctrico. |
| **Composite** | Tratar a un grupo de objetos como a uno solo. | Construir jerarquías de parte-todo. | Ejército (soldados y divisiones). |
| **Decorator** | Añadir comportamiento a un objeto. | Envolver un objeto para darle nuevas "capas" de funcionalidad. | Ponerse ropa (chaqueta, bufanda). |
| **Facade** | Simplificar la interfaz de un subsistema. | Ocultar la complejidad interna. | Conserje de hotel. |
| **Flyweight** | Ahorrar memoria compartiendo estado. | Optimizar el uso de recursos para un gran número de objetos. | Caracteres en un editor de texto. |
| **Proxy** | Controlar el acceso a un objeto. | Actuar como un intermediario con poder. | Tarjeta de crédito. |

### Patrones de Comportamiento
*Se centran en los algoritmos y la asignación de responsabilidades entre objetos.*

| Patrón | Intención Principal | Foco | Analogía |
| :--- | :--- | :--- | :--- |
| **Strategy** | Encapsular algoritmos intercambiables. | Cómo un objeto realiza una tarea. | Elegir una ruta en un mapa (coche, bici, a pie). |
| **State** | Cambiar el comportamiento de un objeto según su estado. | Qué puede hacer un objeto en su estado actual. | Los botones de un reproductor de música (Play/Pause). |
| **Mediator** | Centralizar la comunicación entre objetos. | Cómo colabora un grupo de objetos. | Torre de control de un aeropuerto. |
| **Command** | Encapsular una acción en un objeto. | Convertir una operación en un objeto portable. | Un pedido en un restaurante. |
| **Observer** | Notificar a múltiples objetos sobre un cambio. | Mantener a los objetos sincronizados. | Suscripción a un canal de YouTube. |
| **Chain of Responsibility** | Pasar una solicitud por una cadena de posibles manejadores. | Desacoplar quién envía de quién recibe. | Línea de soporte técnico con varios niveles. |

---