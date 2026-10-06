# M-02 — Entrada a ingeniería de software reconociendo conocimientos previos

**Estado: diseño inicial.** Actividades originales de esta malla disponibles; integración externa y validación pedagógica pendientes.

Reconocer experiencia demostrable y construir una ruta hacia diseño, construcción, comprobación y evolución de software mediante un pequeño catálogo local.

## Entrada, propósito y reconocimiento

Se explora la capacidad de leer una especificación y manejar archivos. Las competencias iniciales son orientativas y admiten apoyo. La experiencia previa permite omitir práctica redundante cuando una demostración cubre el resultado y una variación.

**Dirigida a:** Personas autodidactas; Estudiantes que ingresan a una especialidad; Personas con experiencia técnica que desean ordenar sus fundamentos.

**Objetivos observables**

- Reconocer fortalezas y vacíos con evidencias específicas.
- Convertir una necesidad acotada en reglas y criterios comprobables.
- Construir un programa local coherente con sus reglas.
- Comprobar casos relevantes y explicar errores.
- Preparar instrucciones de uso, recuperación y una modificación controlada.
- Valorar una propuesta de IA contrastándola con reglas y pruebas.

**Diagnóstico de entrada**

- Explica un producto técnico propio o autorizado, o resuelve el caso ficticio del documento. Distingue qué hiciste tú y qué hicieron otras personas o herramientas.
- Lee la regla de préstamo y propón un caso válido, uno inválido y una condición que siempre deba mantenerse.
- Ejecuta un programa sencillo o demuestra cómo inspeccionarías entradas, resultados y errores. Si hace falta, inicia con SUP-LAB.
- Modifica un ejemplo pequeño para una condición nueva y explica el cambio sin apoyarte únicamente en la familiaridad con la herramienta.

Conserva evidencias previas pertinentes y permite una demostración con una variación del caso. Registra por competencia qué se reconoce, con qué apoyo y qué queda pendiente. La edad, una credencial o terminar una lectura no sustituyen la evidencia. Puedes ajustar el medio, la profundidad y las pausas sin imponer un calendario común.

## Caso original: Colección

El producto de práctica es un catálogo **local**, con datos ficticios. El documento proporciona la especificación; tú construyes la solución. No se entrega aquí una aplicación Colección ya programada. Puedes utilizar un lenguaje conocido; el objetivo de cada paso determina la evidencia que necesitas producir.

### Datos iniciales y reglas

| Identificador | Título | Estado |
| --- | --- | --- |
| B01 | Norte | disponible |
| B02 | Puentes | prestado |

Cada registro tiene un identificador único, un título no vacío después de quitar espacios exteriores y un estado: `disponible` o `prestado`. Crear un registro con identificador repetido debe rechazarse. Un libro disponible puede prestarse; uno prestado puede devolverse. No se presta de nuevo un libro ya prestado. Una operación con identificador inexistente debe mostrar un resultado comprensible y conservar la colección. No se requieren usuarios, nombres, cuentas, pagos ni conexión a Internet.

Realiza las operaciones siguientes **en orden** sobre los datos iniciales:

| Operación | Resultado esperado |
| --- | --- |
| Prestar B01 | B01 queda prestado. |
| Prestar B01 otra vez | Se rechaza; ambos registros conservan su estado. |
| Devolver B02 | B02 queda disponible. |
| Devolver B99 | Se informa que no existe; la colección permanece igual. |
| Crear B01 con cualquier título | Se rechaza el duplicado; no se reemplaza el registro existente. |

Además, prueba un título compuesto únicamente por espacios. Explica cómo verificas el estado completo antes y después de un rechazo: ver un mensaje de error por sí solo no demuestra que los datos hayan quedado intactos.

### Propuesta ficticia de IA para revisar

«Para simplificar el préstamo, cambia siempre el estado del identificador recibido a prestado. Si no existe, crea automáticamente el libro con título vacío».

Compara esta propuesta con los invariantes. Señala qué pruebas revelarían los problemas y redacta una corrección razonada. La actividad puede completarse sin usar un servicio de IA. Si utilizas uno, conserva qué recibiste, qué comprobaste y qué decidiste cambiar.

Para reconocer experiencia previa, aporta una demostración equivalente y resuelve una variación. Haber utilizado un lenguaje durante años puede orientar la entrada, pero las decisiones sobre lo ya demostrado se toman con las evidencias correspondientes. En una práctica solo con pseudocódigo, la construcción ejecutable queda pendiente.

## Secuencia de trabajo

Los pasos expresan dependencias de aprendizaje, no semanas ni horas obligatorias. Si ya demuestras un resultado, conserva esa evidencia y aborda la diferencia que falta. Los apoyos se consultan en [el catálogo de recursos](../support/resources.json).

### 1. Reconocer experiencia y elegir la profundidad — M-02-S1

**Resultado:** Separar experiencia declarada, demostrada y pendiente.

**Haz lo siguiente:**

- Construye una tabla: competencia, evidencia, aporte propio, ayuda utilizada y vacío observado. Usa un ejemplo ficticio si no puedes compartir trabajo previo.
- Demuestra una decisión de diseño y resuelve una variación breve. Registra qué pasos puedes abordar directamente y cuáles necesitan práctica.
- Acuerda un producto final pequeño: catálogo local con operaciones de préstamo y devolución, ejecutable en tu entorno.

**Entrega:** Mapa de entrada con evidencias y decisión de recorrido.

**Comprueba:** Cada reconocimiento cita una evidencia observable y su alcance. No se confunde antigüedad laboral, certificado o lectura con demostración de todas las competencias.

**Alternativas y reconocimiento:** Entrevista técnica oral acompañada de una demostración. Una persona principiante recorre todos los pasos con apoyos; una experimentada aporta evidencia equivalente de cada resultado.

**Vínculos:** competencias C-LEARN-01, C-LEARN-04, C-DIG-01; programas candidatos PRG-SOFTWARE; apoyos SUP-STUDY, SUP-PORTFOLIO, SUP-ACCESS.

### 2. Especificar comportamientos e invariantes — M-02-S2

**Resultado:** Definir entradas, resultados y estados válidos.

**Haz lo siguiente:**

- Lee la especificación Colección del documento y escribe ejemplos para cada operación.
- Dibuja los estados disponible y prestado, sus transiciones válidas y lo que debe pasar ante un identificador ausente.
- Define mensajes útiles y explica qué significa que una operación rechazada no modifique la colección.

**Entrega:** Especificación breve, tabla de ejemplos e invariantes.

**Comprueba:** Los casos cubren creación, préstamo, devolución y rechazo de identificadores duplicados. Se distinguen reglas del dominio y decisiones de interfaz.

**Alternativas y reconocimiento:** Modelar con tarjetas antes de programar. Quien ya domina el caso amplía la especificación con búsqueda, sin añadir cuentas personales o redes de forma automática.

**Vínculos:** competencias C-PROB-01, C-LIT-01, C-SW-02; programas candidatos PRG-SOFTWARE; apoyos SUP-READ, SUP-WRITE, SUP-LANG.

### 3. Construir una primera versión local — M-02-S3

**Resultado:** Implementar las reglas y hacer visible su funcionamiento.

**Haz lo siguiente:**

- Elige un lenguaje disponible; si usas Python, utiliza uv cuando esté disponible y mantén dependencias justificadas.
- Implementa primero una operación y comprueba su resultado; añade las demás conservando una representación clara del estado.
- Carga únicamente los datos ficticios B01 y B02. Ofrece una forma de consultar la colección y mensajes de error comprensibles.

**Entrega:** Programa ejecutable, datos ficticios e instrucciones mínimas para iniciarlo.

**Comprueba:** Las operaciones válidas producen el estado esperado. El código expresa las reglas de forma localizable y acepta entradas controladas.

**Alternativas y reconocimiento:** El pseudocódigo sirve de preparación, pero no demuestra por sí mismo construcción de software ejecutable. Si no hay entorno local, usa un entorno accesible disponible o registra la construcción como pendiente; no declares una implementación inexistente.

**Vínculos:** competencias C-SW-01, C-SW-02, C-DIG-01; programas candidatos PRG-SOFTWARE; apoyos SUP-LAB, SUP-LANG, SUP-ACCESS.

### 4. Comprobar cambios de estado y rechazos — M-02-S4

**Resultado:** Diseñar pruebas que puedan detectar una implementación incorrecta.

**Haz lo siguiente:**

- Ejecuta la secuencia de cinco operaciones y resultados esperados del documento.
- Añade una prueba con título vacío y otra con un identificador ausente; comprueba también que la colección queda intacta tras un rechazo.
- Introduce temporalmente un error controlado en una copia y verifica que una prueba falla por la razón esperada. Corrige y vuelve a ejecutar.

**Entrega:** Casos con resultado esperado y observado; registro de un fallo detectado y corregido.

**Comprueba:** Al menos una prueba verifica una regla del dominio y otra la conservación de estado ante rechazo. La evidencia muestra que una prueba detecta un error, además de mostrar ejecuciones exitosas.

**Alternativas y reconocimiento:** Usar pruebas manuales reproducibles como entrada; automatizarlas cuando ese sea el objetivo. Se evalúa el razonamiento y la cobertura pertinente, sin imponer una cifra artificial de pruebas.

**Vínculos:** competencias C-SW-03, C-LEARN-03; programas candidatos PRG-SOFTWARE; apoyos SUP-LAB, SUP-STUDY.

### 5. Operar, proteger y cambiar con control — M-02-S5

**Resultado:** Preparar uso reproducible y una evolución que preserve reglas.

**Haz lo siguiente:**

- Documenta inicio, datos de ejemplo, limitaciones y cómo restablecer la colección ficticia. Si añades persistencia, verifica guardado y recuperación.
- Identifica dos riesgos pertinentes al alcance local, como sobrescribir el archivo o aceptar datos inválidos, y comprueba un control para cada uno.
- Añade una búsqueda por título o evalúa una propuesta hipotética de IA para esa mejora. Contrasta la propuesta con las reglas y repite las pruebas pertinentes.

**Entrega:** Guía de operación, cambio explicado y comprobación de recuperación o restablecimiento.

**Comprueba:** Otra persona puede reproducir el caso usando la guía. El cambio conserva invariantes y los riesgos descritos corresponden al producto real. Las aportaciones de IA, si se utilizan, se revisan y se identifican.

**Alternativas y reconocimiento:** La revisión de una propuesta de IA puede hacerse con una respuesta ficticia incluida o escrita por el acompañante, sin cuenta de un proveedor. Si el producto no guarda datos, explicar ese alcance y demostrar reinicio con datos iniciales.

**Vínculos:** competencias C-SW-04, C-DIG-02, C-CYB-01, C-AI-01; programas candidatos PRG-SOFTWARE, PRG-CYBER, PRG-AI; apoyos SUP-LAB, SUP-AI, SUP-WRITE.

### 6. Transferir y seleccionar la siguiente especialización — M-02-S6

**Resultado:** Explicar decisiones y aplicar lo aprendido a un dominio próximo.

**Haz lo siguiente:**

- Presenta el programa, una decisión y una limitación mediante productos reproducibles.
- Cambia el contexto a préstamo de herramientas: identifica las reglas reutilizables y propone una nueva, sin implementarla si está fuera de alcance.
- Elige profundización en datos, seguridad, arquitectura de software o proyecto comunitario según las evidencias y requisitos pendientes.

**Entrega:** Portafolio técnico, análisis de transferencia y decisión de continuidad.

**Comprueba:** Se explica qué evidencia respalda cada competencia y en qué alcance. La nueva regla se expresa como comportamiento comprobable y se identifican los conocimientos que faltan.

**Alternativas y reconocimiento:** Demostración oral con código accesible, documento o grabación local autorizada. Reconocer evidencia equivalente y pedir práctica solo para la diferencia no demostrada.

**Vínculos:** competencias C-LEARN-04, C-LIT-02, C-SW-02, C-SW-03; programas candidatos PRG-SOFTWARE; apoyos SUP-PORTFOLIO, SUP-WRITE.

## Evaluación y portafolio

Utiliza **RUB-PROJECT**, disponible en [las rúbricas compartidas](../assessment/rubrics.json). No promedies dimensiones para ocultar una evidencia pendiente. Interpreta los descriptores dentro del alcance y las condiciones de esta actividad; estas rúbricas no han sido validadas como pruebas psicométricas.

**Evidencias que conservar:** Especificación e invariantes; Código y datos ficticios; Pruebas pertinentes; Guía de operación; Cambio y transferencia.

**Criterios para revisar la entrega:**

- Correspondencia entre necesidad, reglas y funcionamiento.
- Pruebas que detectan fallos y preservación del estado.
- Reproducibilidad, límites del producto y atribución del trabajo propio.
- Transferencia justificada y reconocimiento de lo pendiente.

Para cada evidencia, anota: versión, autoría, ayudas, resultado observado, límite y siguiente decisión. Marca una actividad no realizada como pendiente. Si se eligió una alternativa sin herramienta digital, sin software ejecutable o sin participante, no reconozcas automáticamente las competencias que requerían esas evidencias.

## Integración, disponibilidad y continuidad

**Programas de origen candidatos:** PRG-SOFTWARE, PRG-CYBER, PRG-AI. Sus repositorios, fuentes y alcance de revisión se consultan en [el catálogo](../catalog/programs.json). La vinculación de esta malla es una propuesta por área: requiere verificar unidades y actividades antes de afirmar equivalencias precisas o recomendar una clase concreta.

Caso original completo como especificación de práctica; el estudiante construye su solución. No se incluye ni se afirma una aplicación Colección implementada. La selección exacta de clases externas está pendiente.

**Continuidades sugeridas:** M-03, M-04, M-05. Elige una según el nuevo objetivo y sus conocimientos de entrada; no es obligatorio recorrer todas. Consulta [cómo elegir y retomar](../pathways/elegir-y-retomar.md).

**Fuente de contenido:** este documento Markdown. [mallas.json](mallas.json) y [competencies.json](../competencies/competencies.json) son índices técnicos de IDs y relaciones. Los casos y materiales son originales del repositorio maestro; no son copias de clases externas.
