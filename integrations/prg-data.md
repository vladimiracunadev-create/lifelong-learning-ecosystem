# Integración: Python y Ciencia de Datos

**ID estable:** `PRG-DATA` · **Revisión documental:** 2026-10-05

**Origen:** [vladimiracunadev-create/python-data-science-program](https://github.com/vladimiracunadev-create/python-data-science-program)

**Registro canónico:** [catalog/programs.json](../catalog/programs.json) · **Evidencia:** [registro de fuentes](../sources/evidence.json).

## Papel en el ecosistema

Programa con currículo y herramientas locales para pasar de preguntas y datos a análisis, experimentos y comunicación de resultados.

Las siguientes decisiones de integración son una propuesta propia de `lifelong-learning-ecosystem`, elaborada a partir de la presentación del programa. Aún deben alinearse con unidades leídas y revisadas por personas.

**Destinatarios de esta conexión:** estudiantes de Python, analistas, formadores técnicos, personas que retoman formación tecnológica.

El maestro referencia materiales de estudio. El README sitúa el laboratorio de ejecución en uso local y declara que carece de sandbox fuerte y autenticación integrada; no se publica como servicio multiusuario. Una aplicación disponible no demuestra que sus clases estén validadas pedagógicamente.

## Estado realmente observado

El README completo declara 232 clases y notebooks en nueve partes, aplicaciones y materiales derivados. También declara límites de su laboratorio local y distribución móvil debug. No se ejecutaron notebooks, aplicaciones, tests ni instaladores.

**Alcance de la lectura:** README completo recuperado mediante conector GitHub; análisis documental sin abrir sus unidades ni ejecutar herramientas.

**SHA del archivo fuente informado por GitHub:** `2cb1f9be12a4d665475720bebe9d9cb2e1ee00aa`. Identifica el contenido del README y no debe tratarse como un commit del repositorio completo.

**Revisión pedagógica:** La alineación con las competencias del maestro es una propuesta editorial. Requiere lectura de unidades, revisión pedagógica humana y evidencia de uso; no se verificó eficacia del aprendizaje.

## Puntos de entrada observados

Los enlaces relativos se resolvieron sobre la ubicación del README leído. Observar un enlace no comprueba que el destino exista hoy o que su contenido cumpla un estándar.

| Recurso | Verificación realizada |
| --- | --- |
| [README del programa](https://github.com/vladimiracunadev-create/python-data-science-program/blob/main/README.md) | Leído completo |
| [Índice de clases](https://github.com/vladimiracunadev-create/python-data-science-program/blob/main/classes/README.md) | Enlace observado; destino sin leer |
| [Prerrequisitos](https://github.com/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/README.md) | Enlace observado; destino sin leer |
| [Syllabus](https://github.com/vladimiracunadev-create/python-data-science-program/blob/main/docs/syllabus.md) | Enlace observado; destino sin leer |
| [Guía del alumno](https://github.com/vladimiracunadev-create/python-data-science-program/blob/main/docs/student-guide.md) | Enlace observado; destino sin leer |
| [Estadística inferencial](https://github.com/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-3-estadistica-inferencial/README.md) | Enlace observado; destino sin leer |
| [Ética y privacidad](https://github.com/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-7-etica-fairness-privacidad/README.md) | Enlace observado; destino sin leer |
| [Catálogo del producto](https://github.com/vladimiracunadev-create/python-data-science-program/blob/main/docs/CATALOGO_PRODUCTO.md) | Enlace observado; destino sin leer |
| [Seguridad](https://github.com/vladimiracunadev-create/python-data-science-program/blob/main/SECURITY.md) | Enlace observado; destino sin leer |

## Selección de unidades para una malla

1. Formular una pregunta que los datos puedan informar. Identificar columnas, unidades, procedencia y una posible limitación.
2. Comprobar requisitos de Python y estadística por una tarea breve y seleccionar la clase o notebook correspondiente. Separar comprensión de datos de problemas de instalación.
3. Leer y ejecutar el notebook elegido en un entorno adecuado; añadir una interpretación propia y una verificación de calidad de datos. Registrar qué parte del resultado cambia al alterar un supuesto.

Antes de activar una correspondencia, registrar el identificador original de la unidad, su URL exacta, la versión revisada, el resultado esperado, la evidencia exigida y cualquier adaptación. Aplicar el [procedimiento común](UNIT_SELECTION.md). Cuando un contenido no esté desarrollado, mantenerlo pendiente y declarar por separado la actividad original del maestro que permita continuar.

## Objetivos candidatos

- Leer un conjunto de datos sintético, identificar problemas y documentar una decisión de limpieza.
- Escribir un análisis reproducible sencillo y comunicar qué permite concluir.
- Separar descripción, predicción y explicación causal al presentar un resultado.

Estos objetivos orientan la selección; no afirman que cada clase externa ya los cubra. Las competencias candidatas son:

| Competencia del maestro | Capacidad a relacionar |
| --- | --- |
| `C-DATA-01` | Interpretar datos y variabilidad |
| `C-DIG-01` | Usar herramientas digitales |
| `C-SW-01` | Construir programas básicos |
| `C-AI-02` | Evaluar modelos con datos |
| `C-RES-02` | Diseñar una indagación |
| `C-ETH-01` | Deliberar sobre responsabilidades |

## Dependencias y conexiones

PRG-MATH aporta herramientas cuantitativas; C-DIG-01 y C-SW-01 sostienen la ejecución. PRG-AI y LAB-NEURAL especializan el modelado. Las actividades iniciales pueden comenzar con datos pequeños y una tabla antes de usar un entorno completo.

Los programas conectados aportan unidades seleccionadas; no son requisitos completos por defecto. Se puede reconocer una base mediante una tarea y explicación documentadas. La edad modifica el contexto y el acompañamiento, no sustituye esa evidencia.

## Actividad puente propuesta

Crear una tabla de diez observaciones ficticias con un dato faltante y un valor improbable. Calcular una medida, explicar cómo trataste ambos problemas y comprobar si la interpretación cambia.

Esta actividad es original del maestro. Su evidencia mínima es un artefacto, la explicación de una decisión y una revisión después de recibir retroalimentación. No se atribuye a una clase externa no leída.

## Integrar cambios sin romper el origen

Respetar la separación entre currículo, portal, app de escritorio, Android y laboratorio. El maestro enlaza la superficie apropiada para la persona; no distribuye binarios ni convierte el runner local en infraestructura del maestro.

Si cambia el README, revisar el alcance antes de actualizar su SHA. Si cambia una unidad seleccionada, revisar solamente las correspondencias afectadas. Conservar los IDs del maestro y documentar cambios de URL o nombre; no renombrar el repositorio externo desde este catálogo.

## Condiciones de reutilización

El README anuncia MIT. Verificar las licencias de cada dato, obra, biblioteca y material antes de reproducirlo o incorporarlo a una aplicación. El maestro conserva enlaces y descripciones propias. Incorporar una copia de material externo exige verificar autoría, licencia y versión, y mantener la atribución y sus condiciones.
