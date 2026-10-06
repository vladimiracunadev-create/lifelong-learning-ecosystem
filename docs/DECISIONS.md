# Decisiones de arquitectura — 0.1.0

## D-01 — Nombre y unidad central

**Decisión:** `lifelong-learning-ecosystem`, presentado como Ecosistema Integral de Aprendizaje a lo Largo de la Vida. La entidad principal es la trayectoria de aprendizaje.

**Razón:** el proyecto reúne disciplinas, contextos, apoyos y experiencias que cambian durante la vida. El nombre conserva espacio para ampliar programas.

**Consecuencia:** los datos distinguen programas, competencias y mallas; una persona puede combinar varias rutas.

## D-02 — Integración federada

**Decisión:** mantener un catálogo de repositorios independientes y fichas de correspondencia.

**Razón:** los programas poseen estructuras y objetivos propios. Las relaciones pueden mejorarse sin trasladar todas sus clases al maestro.

**Consecuencia:** se requiere mantener enlaces, fuentes y estados de integración. La primera entrega revisa principalmente README; la equivalencia por unidad sigue pendiente.

## D-03 — JSON y Markdown

**Decisión:** JSON para registros canónicos y Markdown para contenido explicativo.

**Razón:** permiten inspección directa, control de versiones y herramientas pequeñas de biblioteca estándar. El contrato se publica en DATA_CONTRACT.md y el validador comprueba su aplicación.

**Consecuencia:** los cambios en campos deben respetar versión y referencias. El portal es un derivado y no el lugar para editar registros.

## D-04 — Seis niveles por competencia

**Decisión:** utilizar seis descriptores de progresión, específicos para cada competencia.

**Razón:** describen cambios de acompañamiento, autonomía, complejidad y contribución. Son una convención editorial, no una escala validada ni una clasificación global de la persona.

**Consecuencia:** la evidencia se interpreta en contexto y puede revisarse. El nivel de un área no se propaga automáticamente a otra.

## D-05 — Tres estados de revisión y aprendizaje separados

**Decisión:** diferenciar disponibilidad del contenido, revisión de fuentes y evidencia del estudiante.

**Razón:** un archivo existente o un índice de clases no demuestra aprendizaje ni calidad educativa.

**Consecuencia:** las rutas muestran readiness y las fichas declaran el alcance de lectura.

## D-06 — Herramientas locales sin dependencias externas

**Decisión:** Python 3.11+ con biblioteca estándar, ejecución con uv o intérprete disponible.

**Razón:** simplificar lectura, edición y validación en Windows, macOS y Linux.

**Consecuencia:** los scripts priorizan operaciones acotadas. Un cambio que requiera una nueva biblioteca debe justificar su necesidad y sus requisitos.

## D-07 — Lector autocontenido

**Decisión:** generar index.html con datos y contenido embebidos, sin servicios externos.

**Razón:** permitir apertura al doble clic y consulta offline de lo entregado.

**Consecuencia:** los recursos de los programas enlazados requieren conexión o una copia propia. El lector se reconstruye después de editar fuentes.

## D-08 — Progreso privado

**Decisión:** ejemplos ficticios en el repositorio y planes reales en carpetas privadas.

**Razón:** el repositorio distribuye currículo, no historiales identificables. La participación de menores refuerza la necesidad de acompañamiento y una gestión adecuada de evidencias.

**Consecuencia:** private y exports se excluyen de Git. Esa exclusión es una ayuda técnica y debe comprobarse antes de compartir archivos.

## D-09 — IA como capacidad futura

**Decisión:** documentar su contrato y desarrollar primero un núcleo consultable y verificable.

**Razón:** las recomendaciones deben tener fuentes, supuestos y alternativas. El contenido no debe depender de un proveedor específico.

**Consecuencia:** esta versión no ejecuta modelos. Los filtros del lector operan sobre rutas curadas y no acreditan competencias.

## D-10 — Calidad por capas

**Decisión:** separar coherencia de archivos, revisión editorial, revisión especializada y evidencia de uso.

**Razón:** cada comprobación responde una pregunta distinta.

**Consecuencia:** quality conserva límites y siguientes acciones. El éxito técnico no se anuncia como validación pedagógica.

## Revisión de decisiones

Modificar una decisión requiere describir el problema observado, alternativas, efectos sobre datos y documentación, migración y verificación. Conservar el historial permite comprender por qué existe la estructura actual.
