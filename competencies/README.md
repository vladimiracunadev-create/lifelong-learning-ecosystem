# Competencias y progresión

Este catálogo inicial contiene **36 competencias y 216 descriptores**. Es una propuesta editorial para conectar aprendizajes de distintas disciplinas; requiere revisión humana pedagógica y validación de sus usos. No constituye un estándar oficial, una prueba validada ni una acreditación profesional.

## Qué representa un registro

El archivo [competencies.json](competencies.json) es la fuente canónica. Cada competencia describe una capacidad, resultados observables, evidencias posibles, una tarea de transferencia y seis descriptores. Los programas referenciados son **candidatos de alineación editorial**: la relación no afirma que todas sus clases cubran el descriptor ni que cursarlos garantice dominio. La comprobación de unidades específicas se documenta en las integraciones del repositorio maestro.

Los registros asociados a `PRG-PEDAGOGY` orientan a quien diseña o acompaña el aprendizaje. Esa referencia no convierte el programa de pedagogía en material que un niño deba estudiar. Las actividades destinadas a niñas y niños requieren adaptación de lenguaje, materiales y acompañamiento. Un `program_ids` vacío indica contenido original del maestro pendiente de una conexión externa pertinente.

## Seis niveles que se describen por competencia

| Nivel | Lectura de trabajo |
| --- | --- |
| Exploración | Reconocer, experimentar, preguntar y expresar una observación con apoyos pertinentes. |
| Fundamentos | Comprender ideas y relaciones básicas y explicarlas en situaciones conocidas. |
| Aplicación acompañada | Usar una pauta o apoyo explícito para producir y revisar una evidencia. |
| Autonomía | Elegir y comprobar procedimientos en un contexto acotado sin depender de cada indicación. |
| Profundización | Contrastar alternativas, analizar condiciones y justificar decisiones de mayor complejidad. |
| Creación e investigación | Desarrollar una propuesta original o indagación, documentarla y revisar sus límites. |

La tabla orienta la lectura: **el descriptor específico de cada competencia decide qué se observa**. Los niveles no equivalen a edades, cursos, títulos ni valores de las rúbricas 0–3. Una persona puede dominar una competencia y explorar otra. La autonomía admite tecnología de apoyo, comunicación alternativa y ajustes de acceso: usar apoyos de accesibilidad no reduce por sí mismo el dominio.

## Cómo usarlo en una malla

1. Seleccionar el resultado que interesa y los descriptores pertinentes al contexto.
2. Revisar los prerrequisitos mediante una tarea corta. Se puede demostrar una base con aprendizaje previo, actividades puente o una evidencia existente.
3. Escoger una actividad que permita observar el resultado y acordar criterios antes de realizarla.
4. Registrar la evidencia y el apoyo utilizado. Diferenciar contenido consultado, actividad realizada y desempeño demostrado.
5. Proponer una variante para comprobar transferencia. Describir qué cambió y qué se conserva.
6. Conservar las incertidumbres y acordar una siguiente revisión cuando falte evidencia.

**Ejemplo:** para comparar presupuestos se necesita razonar con porcentajes y reconocer variabilidad. Una persona presenta una tabla correcta, pero omite los supuestos. Se registra la evidencia de cálculo, se pide explicitar los supuestos y se revisa una variante; no se etiqueta a la persona como incapaz ni se le asigna un nivel general por un solo producto.

## Dependencias y mantenimiento

[PRERREQUISITOS.md](PRERREQUISITOS.md) explica cada dependencia inicial. El grafo es acíclico: una flecha de requisito orienta una base conceptual de la progresión. Se revisa contra el descriptor y la tarea concretos; no bloquea automáticamente la exploración ni obliga a cursar un repositorio completo. La repetición deliberada y el retorno a un tema ocurren en las rutas de práctica; no se representan creando ciclos entre prerrequisitos.

Una modificación conserva los IDs existentes. Si cambia el significado sustantivo de una competencia, se documenta la migración y se revisan mallas, apoyos y rúbricas afectadas. Antes de ampliar el catálogo, comprobar que la nueva capacidad sea distinguible mediante evidencia y que no duplique otra con un nombre distinto.
