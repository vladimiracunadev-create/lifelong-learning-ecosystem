# Contrato de datos — versión 1.0

Este contrato describe los **registros técnicos estructurados** del repositorio maestro. Los archivos JSON son UTF-8, usan `schema_version: "1.0"` y son canónicos únicamente para IDs, relaciones, estados y campos que valida el software. **No son el formato de autoría del contenido educativo.**

Las explicaciones, análisis de repositorios, rutas, mallas legibles, actividades, gráficos y decisiones pedagógicas se escriben en Markdown y SVG. El portal combina esos documentos con los índices técnicos; no genera el contenido educativo a partir de JSON ni debe obligar a programarlo dentro de esos archivos. La versión editorial del proyecto comienza en `0.1.0`.

## Principios

- Markdown es la fuente legible del contenido y del análisis; JSON actúa como índice técnico y contrato de relaciones.
- Una persona debe poder comprender los programas y sus rutas desde los documentos sin leer JSON.
- El maestro referencia programas independientes y mantiene sus propias mallas, actividades puente y reglas de integración.
- Una revisión de README demuestra lo que declara ese documento; no certifica el desarrollo o eficacia de todas sus clases.
- Cada identificador es único y estable. Los cambios de nombre conservan el identificador y registran la migración.
- Las referencias entre registros deben existir. Los prerrequisitos entre competencias y entre pasos de una malla no pueden contener ciclos.
- Los ciclos de revisión del aprendizaje y las recomendaciones de continuidad entre mallas sí pueden existir.
- Los perfiles de ejemplo son ficticios. Los datos personales reales quedan fuera del repositorio distribuido.
- Los estados de contenido, revisión pedagógica, compatibilidad y evidencia de aprendizaje se registran por separado.

## Archivos canónicos

### `catalog/programs.json`

Objeto con `schema_version`, `reviewed_on` (YYYY-MM-DD), `scope_note` y `programs` (lista). Cada programa:

- `id`, `name`, `repository` (`owner/name`), `url`, `description`.
- `role`: `programa`, `laboratorio`, `herramienta` o `programa_y_herramienta`.
- `domains`, `audiences`: listas de textos.
- `review`: objeto con `status` (`readme_revisado`, `indice_revisado` o `pendiente`), `reviewed_on`, `source_url`, `content_sha`, `scope`, `declared_content_status`, `human_validation`.
- `entry_points`: lista de objetos `{label, url, verification}`. El URL debe haber sido observado en una fuente; `verification` distingue enlace observado y recurso leído.
- `competency_ids`: lista de identificadores del catálogo de competencias.
- `license_note`, `integration_doc`: texto y ruta relativa existente.

Solo se incluyen aquí repositorios identificados. Los programas conocidos por conversación pero sin repositorio actual verificado van a `catalog/pending.json`, con `schema_version` y `items`: `{id, topic, known_context, reason_pending, next_action}`. No se inventan slugs ni URLs.

### `competencies/competencies.json`

Objeto con `schema_version`, `levels` y `competencies`. `levels` es la lista ordenada:

`exploracion`, `fundamentos`, `aplicacion_acompanada`, `autonomia`, `profundizacion`, `creacion_investigacion`.

Cada competencia: `id`, `title`, `domain`, `description`, `prerequisites` (IDs), `outcomes` (lista), `evidence` (lista), `program_ids` (IDs), `transfer_task`, `review_status` (`propuesta_editorial`), `level_descriptors` (objeto con las seis claves de nivel y un descriptor específico por nivel).

En esta versión, `prerequisites` expresa relaciones de progresión que deben revisarse contra el descriptor y la tarea seleccionados. No contiene un nivel mínimo exigible y no se debe utilizar como bloqueo automático de exploración. Las mallas concretan sus requisitos de ingreso y los pasos requeridos según las actividades reales. Una futura automatización de acceso necesitará representar y revisar explícitamente requisito, nivel y tarea antes de aplicarlos.

### `support/resources.json`

Objeto con `schema_version` y `resources`. Cada recurso: `id`, `title`, `purpose`, `trigger`, `activities` (lista), `success_criteria` (lista), `program_ids`, `competency_ids`, `doc_path` (ruta existente), `status` (`guia_inicial`).

### `assessment/rubrics.json`

Objeto con `schema_version`, `scale` (lista de objetos `{value, label}` con valores 0–3), `rubrics` (lista). Cada rúbrica: `id`, `title`, `purpose`, `criteria` (lista de objetos `{id, title, descriptors}`; `descriptors` tiene claves `0`, `1`, `2`, `3`), `decision_rule`, `limitations`, `doc_path`. Los descriptores son observables; no existen cortes psicométricos inventados.

### `curricula/mallas.json`

Objeto con `schema_version` y `curricula`. Cada malla:

- `id`, `title`, `purpose`, `audience` (lista), `life_contexts` (lista), `entry_profile` (texto).
- `entry_competencies`, `competency_ids`, `program_ids`, `support_ids`: listas de IDs.
- `diagnostic` (lista de tareas de entrada), `objectives` (lista de resultados).
- `steps`: lista de objetos `{id, title, outcomes, competency_ids, program_ids, support_ids, requires, activities, evidence, acceptance_criteria, alternatives, availability}`. `requires` contiene IDs de pasos de la misma malla. Las demás listas son textos o IDs según su nombre. `availability` describe las actividades originales incluidas y el alcance de la alineación externa.
- `assessment`: objeto `{rubric_id, evidence, criteria}`.
- `next_routes` (IDs de otras mallas o lista vacía), `status` (`diseno_inicial`), `content_readiness` (texto honesto), `doc_path` (ruta existente).

Cinco mallas: `M-01` continuidad escolar; `M-02` ingreso a especialidad con conocimientos previos; `M-03` reconversión adulta; `M-04` proyecto interdisciplinario; `M-05` interés personal y transmisión de experiencia.

## Identificadores compartidos

Programas inicialmente previstos y sujetos a lectura de sus fuentes:

| ID | Repositorio bajo `vladimiracunadev-create` |
| --- | --- |
| PRG-SCHOOL | chilean-school-learning-path |
| PRG-PEDAGOGY | education-pedagogy-learning-sciences-program |
| PRG-MATH | computational-mathematics-program |
| PRG-SOFTWARE | modern-software-engineering-program |
| PRG-ARCH | architecture-built-environment-learning-program |
| PRG-FINANCE | finance-and-banking-evolution-program |
| PRG-BUSINESS | modern-business-creation-program |
| PRG-CYBER | modern-cybersecurity-program |
| PRG-AI | artificial-intelligence-evolution-program |
| LAB-NEURAL | neural-network-training-labs |
| PRG-ASSESS | psychometrics-and-assessment-program |
| PRG-MARKETING | marketing-sales-growth-evolution-program |
| PRG-LEADERSHIP | executive-leadership-founder-program |
| PRG-DATA | python-data-science-program |

Competencias previstas (36):

| ID | Núcleo |
| --- | --- |
| C-LEARN-01 | Formular objetivos |
| C-LEARN-02 | Planificar y sostener la práctica |
| C-LEARN-03 | Analizar errores y ajustar |
| C-LEARN-04 | Autoevaluar y transferir |
| C-LIT-01 | Comprender y contrastar textos |
| C-LIT-02 | Argumentar y escribir |
| C-COM-01 | Escuchar y comunicar oralmente |
| C-NUM-01 | Razonar con cantidades |
| C-NUM-02 | Proporciones y porcentajes |
| C-NUM-03 | Modelar relaciones matemáticas |
| C-DATA-01 | Interpretar datos y variabilidad |
| C-DIG-01 | Usar herramientas digitales |
| C-DIG-02 | Cuidar información y accesos |
| C-RES-01 | Buscar y evaluar fuentes |
| C-RES-02 | Diseñar una indagación |
| C-ETH-01 | Deliberar sobre responsabilidades |
| C-CREATE-01 | Crear y revisar una expresión artística |
| C-PROB-01 | Formular problemas |
| C-PROJ-01 | Organizar y ejecutar proyectos |
| C-COLLAB-01 | Colaborar y resolver desacuerdos |
| C-SW-01 | Construir programas básicos |
| C-SW-02 | Especificar y diseñar software |
| C-SW-03 | Comprobar software |
| C-SW-04 | Operar y evolucionar software |
| C-AI-01 | Comprender y evaluar usos de IA |
| C-AI-02 | Evaluar modelos con datos |
| C-CYB-01 | Analizar y reducir riesgos digitales |
| C-FIN-01 | Elaborar y revisar presupuestos |
| C-FIN-02 | Comparar alternativas económicas |
| C-BIZ-01 | Diseñar una propuesta de valor |
| C-BIZ-02 | Organizar una operación |
| C-ARCH-01 | Observar y representar espacios habitados |
| C-TEACH-01 | Diseñar y acompañar aprendizaje |
| C-ASSESS-01 | Evaluar mediante evidencia |
| C-WELL-01 | Organizar hábitos y condiciones de aprendizaje |
| C-CIV-01 | Participar en iniciativas de la comunidad |

Apoyos: `SUP-READ`, `SUP-WRITE`, `SUP-MATH`, `SUP-STUDY`, `SUP-LANG`, `SUP-RESEARCH`, `SUP-ACCESS`, `SUP-LAB`, `SUP-PORTFOLIO`, `SUP-AI`.

Rúbricas: `RUB-CORE` (evidencia de aprendizaje), `RUB-PROJECT` (proyecto integrador), `RUB-TEACH` (transmisión de experiencia).

Contextos vitales para filtros: `primera_infancia`, `basica`, `media`, `formacion_especializada`, `vida_laboral`, `reconversion`, `aprendizaje_personal`, `transmision_experiencia`. Son orientaciones, no barreras de edad.

## Validación y evolución

La comprobación local valida estructura, referencias, unicidad, URLs bien formadas, rutas internas y ausencia de ciclos en prerrequisitos. No realiza peticiones de red, no certifica calidad pedagógica y no equivale a una auditoría externa. Las fuentes externas registran el alcance de lo leído.

Los cambios incompatibles de contrato incrementan la versión y requieren un plan de migración. El portal es un derivado regenerable: se actualiza primero la fuente correspondiente —Markdown/SVG para contenido y JSON para registros— y después se reconstruye.
