# Integración: Psicometría y Evaluación

**ID estable:** `PRG-ASSESS` · **Revisión documental:** 2026-10-05

**Origen:** [vladimiracunadev-create/psychometrics-and-assessment-program](https://github.com/vladimiracunadev-create/psychometrics-and-assessment-program)

**Registro canónico:** [catalog/programs.json](../catalog/programs.json) · **Evidencia:** [registro de fuentes](../sources/evidence.json).

## Papel en el ecosistema

Formación y herramientas para estudiar cómo se construyen, puntúan, revisan y limitan instrumentos de evaluación.

Las siguientes decisiones de integración son una propuesta propia de `lifelong-learning-ecosystem`, elaborada a partir de la presentación del programa. Aún deben alinearse con unidades leídas y revisadas por personas.

**Destinatarios de esta conexión:** personas que estudian evaluación, formadores, desarrolladores de instrumentos educativos.

Las rúbricas formativas del maestro describen desempeños observables. No deben transformarse en diagnósticos clínicos, baremos o certificaciones por enlazar este programa. Los planes de clases pendientes conservan ese estado.

## Estado realmente observado

El fragmento del README presenta una planificación de 40 clases en ocho partes y declara cinco clases escritas. También anuncia cinco instrumentos y 344 ítems; su presencia o sus pruebas de software no demuestran validación psicométrica para una población o uso.

**Alcance de la lectura:** Fragmento inicial del README (38 líneas capturadas) recuperado mediante conector GitHub; no equivale a lectura completa del repositorio.

**SHA del archivo fuente informado por GitHub:** `5e2f8f5ba3fcab7508f934cd6ebfa936b07d2032`. Identifica el contenido del README y no debe tratarse como un commit del repositorio completo.

**Revisión pedagógica:** La validez para usos y poblaciones concretos no se estableció mediante esta revisión. La alineación con las competencias del maestro es una propuesta editorial. Requiere lectura de unidades, revisión pedagógica humana y evidencia de uso; no se verificó eficacia del aprendizaje.

## Puntos de entrada observados

Los enlaces relativos se resolvieron sobre la ubicación del README leído. Observar un enlace no comprueba que el destino exista hoy o que su contenido cumpla un estándar.

| Recurso | Verificación realizada |
| --- | --- |
| [README del programa](https://github.com/vladimiracunadev-create/psychometrics-and-assessment-program/blob/main/README.md) | Fragmento inicial leído |
| [Plan curricular](https://github.com/vladimiracunadev-create/psychometrics-and-assessment-program/blob/main/curriculum.yaml) | Enlace observado; destino sin leer |
| [Clases](https://github.com/vladimiracunadev-create/psychometrics-and-assessment-program/tree/main/classes/) | Enlace observado; destino sin leer |
| [Instrumentos](https://github.com/vladimiracunadev-create/psychometrics-and-assessment-program/tree/main/instruments/) | Enlace observado; destino sin leer |
| [Validación y límites](https://github.com/vladimiracunadev-create/psychometrics-and-assessment-program/blob/main/docs/VALIDACION.md) | Enlace observado; destino sin leer |
| [Bibliografía](https://github.com/vladimiracunadev-create/psychometrics-and-assessment-program/blob/main/sources/BIBLIOGRAFIA.md) | Enlace observado; destino sin leer |
| [Arquitectura](https://github.com/vladimiracunadev-create/psychometrics-and-assessment-program/blob/main/docs/ARQUITECTURA.md) | Enlace observado; destino sin leer |

## Selección de unidades para una malla

1. Definir la decisión educativa que la evaluación debe informar y qué evidencia sería pertinente.
2. Leer primero la documentación de validación y los instrumentos candidatos. Registrar población, finalidad, procedimiento, procedencia y límites declarados.
3. Para aprendizaje de diseño, preferir ejemplos ficticios y comparar interpretaciones. No asignar un corte o equivalencia externa sin una justificación válida y revisada.

Antes de activar una correspondencia, registrar el identificador original de la unidad, su URL exacta, la versión revisada, el resultado esperado, la evidencia exigida y cualquier adaptación. Aplicar el [procedimiento común](UNIT_SELECTION.md). Cuando un contenido no esté desarrollado, mantenerlo pendiente y declarar por separado la actividad original del maestro que permita continuar.

## Objetivos candidatos

- Distinguir una tarea, un indicador y la interpretación que se hace de su resultado.
- Diseñar criterios observables y comprobar si dos revisores los entienden de manera consistente.
- Explicar una limitación de un instrumento y la evidencia que faltaría para un nuevo uso.

Estos objetivos orientan la selección; no afirman que cada clase externa ya los cubra. Las competencias candidatas son:

| Competencia del maestro | Capacidad a relacionar |
| --- | --- |
| `C-ASSESS-01` | Evaluar mediante evidencia |
| `C-DATA-01` | Interpretar datos y variabilidad |
| `C-RES-02` | Diseñar una indagación |
| `C-ETH-01` | Deliberar sobre responsabilidades |
| `C-TEACH-01` | Diseñar y acompañar aprendizaje |

## Dependencias y conexiones

C-DATA-01 y C-RES-02 sostienen la evaluación cuantitativa y la investigación. PRG-PEDAGOGY ayuda a situar la decisión en el proceso educativo. Una rúbrica sencilla puede usarse sin entrenamiento psicométrico avanzado, conservando límites claros.

Los programas conectados aportan unidades seleccionadas; no son requisitos completos por defecto. Se puede reconocer una base mediante una tarea y explicación documentadas. La edad modifica el contexto y el acompañamiento, no sustituye esa evidencia.

## Actividad puente propuesta

Evaluar dos producciones ficticias con una misma rúbrica; justificar cada decisión y detectar un descriptor ambiguo. Revisar el descriptor antes de usarlo en una nueva muestra.

Esta actividad es original del maestro. Su evidencia mínima es un artefacto, la explicación de una decisión y una revisión después de recibir retroalimentación. No se atribuye a una clase externa no leída.

## Integrar cambios sin romper el origen

Separar cantidad de instrumentos, cantidad de ítems, software ejecutable, clases escritas y evidencia de validez. Nunca actualizar un estado pedagógico por el resultado de tests de código.

Si cambia el README, revisar el alcance antes de actualizar su SHA. Si cambia una unidad seleccionada, revisar solamente las correspondencias afectadas. Conservar los IDs del maestro y documentar cambios de URL o nombre; no renombrar el repositorio externo desde este catálogo.

## Condiciones de reutilización

El README anuncia código MIT y documentación CC BY-NC-SA 4.0, con procedencia diversa de ítems. Revisar licencias y restricciones de cada instrumento. El maestro conserva enlaces y descripciones propias. Incorporar una copia de material externo exige verificar autoría, licencia y versión, y mantener la atribución y sus condiciones.
