# Integración: Ingeniería de Software Moderna

**ID estable:** `PRG-SOFTWARE` · **Revisión documental:** 2026-10-05

**Origen:** [vladimiracunadev-create/modern-software-engineering-program](https://github.com/vladimiracunadev-create/modern-software-engineering-program)

**Registro canónico:** [catalog/programs.json](../catalog/programs.json) · **Evidencia:** [registro de fuentes](../sources/evidence.json).

## Papel en el ecosistema

Especialización que conecta comprensión de problemas, diseño, construcción, comprobación y evolución de software.

Las siguientes decisiones de integración son una propuesta propia de `lifelong-learning-ecosystem`, elaborada a partir de la presentación del programa. Aún deben alinearse con unidades leídas y revisadas por personas.

**Destinatarios de esta conexión:** estudiantes de software, desarrolladores, profesionales que modernizan sistemas, responsables técnicos.

Las competencias de diseño, pruebas y operación expresan el papel propuesto del programa. Las unidades correspondientes deben revisarse una por una antes de incorporarlas como material listo. Una malla puede incluir una actividad original del maestro sin afirmar que el programa externo ya la desarrolla.

## Estado realmente observado

El README describe una arquitectura de 480 clases: SE-001–SE-012 desarrolladas; SE-013–SE-360 con material que requiere revisión cualitativa; SE-361–SE-480 con enseñanza completa aún por desarrollar. El catálogo mantiene estas diferencias y no cuenta 480 clases como terminadas.

**Alcance de la lectura:** Fragmento inicial del README (89 líneas capturadas) recuperado mediante conector GitHub; no equivale a lectura completa del repositorio.

**SHA del archivo fuente informado por GitHub:** `2b7a3a854f1713f152af9c31fb343280120855d8`. Identifica el contenido del README y no debe tratarse como un commit del repositorio completo.

**Revisión pedagógica:** El README exige revisión cualitativa del material en partes 01–29 y desarrollo de partes 30–39. La alineación con las competencias del maestro es una propuesta editorial. Requiere lectura de unidades, revisión pedagógica humana y evidencia de uso; no se verificó eficacia del aprendizaje.

## Puntos de entrada observados

Los enlaces relativos se resolvieron sobre la ubicación del README leído. Observar un enlace no comprueba que el destino exista hoy o que su contenido cumpla un estándar.

| Recurso | Verificación realizada |
| --- | --- |
| [README del programa](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/README.md) | Fragmento inicial leído |
| [Índice de clases](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/README.md) | Enlace observado; destino sin leer |
| [Rutas por rol](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/roles/README.md) | Enlace observado; destino sin leer |
| [Producto transversal](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/blueprints/reference-product/README.md) | Enlace observado; destino sin leer |
| [Estándar pedagógico](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/docs/PEDAGOGICAL-STANDARD.md) | Enlace observado; destino sin leer |
| [Roadmap](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/ROADMAP.md) | Enlace observado; destino sin leer |

## Selección de unidades para una malla

1. Elegir una decisión de ingeniería y un artefacto verificable: requisito, prototipo, prueba, diagnóstico o plan de operación.
2. Localizar la unidad en el índice y leer su estado editorial. SE-001–SE-012 son el punto de entrada con desarrollo declarado; cualquier otra selección conserva la revisión o desarrollo pendiente.
3. Contrastar objetivo, ejemplo, práctica y criterios. Para material incompleto, registrar la brecha y usar una actividad original claramente identificada hasta completar la enseñanza del origen.

Antes de activar una correspondencia, registrar el identificador original de la unidad, su URL exacta, la versión revisada, el resultado esperado, la evidencia exigida y cualquier adaptación. Aplicar el [procedimiento común](UNIT_SELECTION.md). Cuando un contenido no esté desarrollado, mantenerlo pendiente y declarar por separado la actividad original del maestro que permita continuar.

## Objetivos candidatos

- Convertir una necesidad en requisitos observables y distinguir restricciones de preferencias.
- Construir un programa pequeño y comprobar un caso habitual, un límite y un error.
- Explicar una decisión de operación o modernización considerando evidencia, costo y riesgo.

Estos objetivos orientan la selección; no afirman que cada clase externa ya los cubra. Las competencias candidatas son:

| Competencia del maestro | Capacidad a relacionar |
| --- | --- |
| `C-PROB-01` | Formular problemas |
| `C-PROJ-01` | Organizar y ejecutar proyectos |
| `C-SW-01` | Construir programas básicos |
| `C-SW-02` | Especificar y diseñar software |
| `C-SW-03` | Comprobar software |
| `C-SW-04` | Operar y evolucionar software |
| `C-DIG-02` | Cuidar información y accesos |
| `C-ETH-01` | Deliberar sobre responsabilidades |

## Dependencias y conexiones

C-PROB-01 y C-DIG-01 sostienen la entrada. PRG-CYBER contribuye a riesgos; PRG-BUSINESS y PRG-FINANCE ayudan a evaluar una solución en su contexto. La experiencia previa se reconoce mediante artefactos y explicación, no por años de cargo.

Los programas conectados aportan unidades seleccionadas; no son requisitos completos por defecto. Se puede reconocer una base mediante una tarea y explicación documentadas. La edad modifica el contexto y el acompañamiento, no sustituye esa evidencia.

## Actividad puente propuesta

Escribir tres criterios de aceptación de una necesidad cotidiana y comprobarlos sobre un prototipo de papel o código pequeño. Registrar un caso que parecía cubierto y falló, y revisar el requisito.

Esta actividad es original del maestro. Su evidencia mínima es un artefacto, la explicación de una decisión y una revisión después de recibir retroalimentación. No se atribuye a una clase externa no leída.

## Integrar cambios sin romper el origen

Preservar IDs SE, partes 00–39, estados reales y producto transversal. Las mallas del maestro no deben cambiar nombres ni promover estados externos sin evidencia y revisión.

Si cambia el README, revisar el alcance antes de actualizar su SHA. Si cambia una unidad seleccionada, revisar solamente las correspondencias afectadas. Conservar los IDs del maestro y documentar cambios de URL o nombre; no renombrar el repositorio externo desde este catálogo.

## Condiciones de reutilización

El README indica MIT. No se revisó el alcance del archivo LICENSE ni las condiciones de materiales de terceros. El maestro conserva enlaces y descripciones propias. Incorporar una copia de material externo exige verificar autoría, licencia y versión, y mantener la atribución y sus condiciones.
