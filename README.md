# Lifelong Learning Ecosystem

## Ecosistema Integral de Aprendizaje a lo Largo de la Vida

[![Calidad](https://github.com/vladimiracunadev-create/lifelong-learning-ecosystem/actions/workflows/quality.yml/badge.svg)](https://github.com/vladimiracunadev-create/lifelong-learning-ecosystem/actions/workflows/quality.yml)
[![Seguridad](https://github.com/vladimiracunadev-create/lifelong-learning-ecosystem/actions/workflows/security.yml/badge.svg)](https://github.com/vladimiracunadev-create/lifelong-learning-ecosystem/actions/workflows/security.yml)
[![Portal público](https://img.shields.io/badge/portal-GitHub%20Pages-1f6b49)](https://vladimiracunadev-create.github.io/lifelong-learning-ecosystem/)
[![Licencia de código](https://img.shields.io/badge/código-MIT-2d3748)](LICENSE)

**Superrepositorio de Vladimir Acuña para conectar programas independientes, competencias, mallas de estudio, apoyos y criterios de evidencia desde la infancia y durante toda la vida.**

Esta es la capa de integración del ecosistema. Cada programa conserva su repositorio, identidad, numeración, licencia y profundidad disciplinar; el maestro registra procedencia, hace visibles las relaciones y construye recorridos que atraviesan varios programas. No duplica cursos completos ni se presenta como un programa adicional.

Una persona puede entrar en cualquier momento, reconocer lo que ya sabe, definir lo que desea alcanzar y construir un recorrido coherente entre distintas fuentes. Las mallas articulan objetivos observables, fundamento, práctica, evidencia, retroalimentación y continuidad.

**Versión inicial: 0.1.0 · Fecha de revisión de fuentes: 5 de octubre de 2026 · Idioma: español.**

## Explorar

1. Abre el [portal público](https://vladimiracunadev-create.github.io/lifelong-learning-ecosystem/) o descarga el repositorio para usarlo sin conexión.
2. En una copia local, abre [index.html](index.html). En Windows también puedes ejecutar [ABRIR_PORTAL.cmd](ABRIR_PORTAL.cmd).
3. Explora las 14 integraciones canónicas, las competencias, las cinco mallas, los apoyos y las rúbricas.
4. Consulta la [arquitectura actual verificada](docs/CURRENT_ARCHITECTURE.md), el [descubrimiento de repositorios](catalog/REPOSITORY_DISCOVERY.md) y [cómo elegir y retomar un recorrido](pathways/README.md).
5. Para continuar el desarrollo con un agente, utiliza el archivo íntegro [PROMPT_MAESTRO.md](PROMPT_MAESTRO.md).

El lector local contiene los datos y documentación de esta entrega. Las clases de los programas enlazados permanecen en sus repositorios y requieren conexión para consultarlas si no se han descargado previamente.

## Mapa rápido

```mermaid
flowchart LR
    U[68 repositorios públicos observados] --> D[Descubrimiento y clasificación]
    D --> P[14 integraciones canónicas]
    P --> I[Integración con procedencia]
    I --> C[36 competencias]
    C --> M[5 mallas · 30 pasos]
    A[10 apoyos] --> M
    R[3 rúbricas] --> M
    M --> L[Portal público y lector local]
```

El [mapa completo](docs/ECOSYSTEM_MAP.md) explica la arquitectura federada, el ciclo de aprendizaje y la continuidad exacta entre las cinco mallas.

## Qué contiene esta versión

| Componente | Entrega |
| --- | --- |
| Integraciones canónicas | Catálogo inicial de 14 repositorios con fuente y alcance de revisión; no es una lista cerrada de la cuenta |
| Descubrimiento | Corte documentado de 68 repositorios públicos: programas, laboratorios, productos, presencia pública y 4 forks separados |
| Competencias | 36 competencias con seis niveles descriptivos y relaciones de prerrequisitos |
| Mallas | Cinco recorridos con actividades puente originales, diagnóstico, evidencia y continuidad |
| Apoyos | Diez guías para lectura, escritura, matemática, estudio, idiomas, fuentes, accesibilidad, laboratorios, portafolio e IA |
| Evaluación | Tres rúbricas editoriales, reconocimiento previo y orientaciones de retroalimentación |
| Integración | Fichas por repositorio y reglas para seleccionar unidades respetando su estructura |
| Herramientas | Validador local, exportación de mallas, constructor del lector y empaquetado reproducible |
| Automatización | Calidad multi-entorno, CodeQL, actualización de acciones y publicación en GitHub Pages |
| Continuidad | Prompt maestro completo, instrucciones de agentes, decisiones y hoja de ruta |

Los conteos y resultados técnicos se registran en [el estado de entrega](quality/STATUS.md) y en el manifiesto de archivos. El catálogo es un inventario inicial; las áreas pendientes se registran explícitamente en [catalog/pending.json](catalog/pending.json).

## Los cinco recorridos

| ID | Propósito |
| --- | --- |
| M-01 | Conectar la formación escolar con intereses y especialidades |
| M-02 | Ingresar a una especialidad reconociendo conocimientos previos |
| M-03 | Preparar una reconversión durante la vida adulta |
| M-04 | Desarrollar un proyecto interdisciplinario |
| M-05 | Aprender por interés personal y transmitir experiencia |

Las mallas completas están en [curricula](curricula/README.md). Su secuencia se expresa por dependencias de conocimiento. Las edades no acreditan competencias, y los calendarios personales se pueden ajustar sin cambiar los resultados esperados.

## Arquitectura

El maestro mantiene un catálogo común, competencias, mallas y correspondencias con los programas. Cada repositorio especializado sigue siendo la fuente de sus clases, prácticas y documentación.

Consulta la [arquitectura implementada](docs/CURRENT_ARCHITECTURE.md), los [diagramas de arquitectura y continuidad](docs/ECOSYSTEM_MAP.md), la [automatización de calidad y publicación](docs/AUTOMATION.md) y los [componentes propuestos, todavía no implementados](PROPOSED_COMPONENTS.md).

| Área | Responsabilidad |
| --- | --- |
| [catalog](catalog/README.md) | Integraciones canónicas, descubrimiento externo, declaraciones y alcance de revisión |
| [competencies](competencies/README.md) | Capacidades, progresión, evidencias y prerrequisitos |
| [curricula](curricula/README.md) | Mallas integradoras y actividades propias del maestro |
| [pathways](pathways/README.md) | Selección, ingreso, retorno y adaptación del recorrido |
| [assessment](assessment/README.md) | Evaluación, rúbricas y reconocimiento de experiencia |
| [support](support/README.md) | Apoyos a dificultades o necesidades concretas |
| [integrations](integrations/README.md) | Correspondencias con programas independientes |
| [sources](sources/README.md) | Fuentes y trazabilidad de las decisiones |
| [quality](quality/README.md) | Coherencia, revisión, brechas y estado |
| [docs](docs/README.md) | Diseño, uso local y evolución del proyecto |
| [examples](examples/README.md) | Ejemplos ficticios y portafolio local |
| [prompts](prompts/README.md) | Continuidad con agentes y registro de avances |

## Tres ejes de personalización

- **Etapa y contexto:** primera infancia acompañada, escolaridad, formación especializada, trabajo, reconversión, intereses personales y transmisión de experiencia.
- **Dominio por competencia:** exploración, fundamentos, aplicación acompañada, autonomía, profundización, creación e investigación.
- **Propósito:** comprender, crear, trabajar, investigar, emprender, convivir, enseñar o participar.

Una misma persona puede tener niveles diferentes en áreas distintas. Las decisiones de ingreso se basan en evidencias pertinentes y se revisan cuando aparece nueva información.

## Estado pedagógico

Las actividades puente, mallas, descriptores y rúbricas de esta entrega son propuestas editoriales desarrolladas y utilizables para revisión y pilotaje. Su eficacia no ha sido validada en una población de estudiantes.

La revisión inicial de las integraciones canónicas se apoya principalmente en README y enlaces observados. Una segunda inspección documentó otros repositorios reales sin asignarles automáticamente IDs ni equivalencias. La correspondencia exacta de cada clase con cada competencia requiere una auditoría posterior por unidades. Cada ficha distingue la declaración del programa, el alcance de la lectura y la revisión humana pendiente.

El [contrato de datos](docs/DATA_CONTRACT.md) separa estos estados. Un resultado técnico correcto comprueba coherencia de los archivos; la valoración del aprendizaje necesita evidencia y criterio educativo.

## Validar y reconstruir

Se requiere Python 3.11 o superior para las herramientas. Leer el portal no requiere Python.

Con uv, si ya está instalado:

~~~bash
uv run --offline python scripts/validate.py
uv run --offline python -m unittest discover -s tests -v
uv run --offline python scripts/build_portal.py --check
~~~

Con Python disponible en el equipo:

~~~bash
python scripts/validate.py
python -m unittest discover -s tests -v
python scripts/build_portal.py --check
~~~

Para regenerar el lector tras cambios:

~~~bash
python scripts/build_portal.py
~~~

En Windows se puede usar `py -3` en lugar de `python`. Consulta [el inicio en Windows](docs/START_WINDOWS.md) y [las instrucciones técnicas](docs/DEVELOPMENT.md).

## Continuar sin romper los programas

Antes de modificar un repositorio conectado, el agente debe leer sus instrucciones y fuentes actuales. Las decisiones sobre clases, numeración, licencias, estructura y derivados se realizan en ese programa y se documentan. La consulta del catálogo no autoriza modificaciones remotas.

El maestro incorpora actividades puente, equivalencias candidatas y mallas, y deja registro de su procedencia. Véase [AGENTS.md](AGENTS.md), [el prompt maestro](PROMPT_MAESTRO.md) y [la política de integración](docs/INTEGRATION_POLICY.md).

## Datos personales y licencias

El repositorio distribuido contiene ejemplos ficticios. Los planes y evidencias reales deben guardarse en una carpeta local privada; se incluyen exclusiones para `private/` y `exports/`.

Código original: [MIT](LICENSE). Contenido curricular original: [CC BY-NC-SA 4.0](LICENSE-CONTENT.md). Los programas y recursos enlazados conservan sus propias licencias.

## Fundamento y decisiones

La visión toma como referencia el aprendizaje durante toda la vida y las rutas flexibles descritos por UNESCO. El modelo de seis niveles, las mallas y las rúbricas concretas son decisiones propias de este proyecto, registradas para revisión.

- [Visión](VISION.md)
- [Diseño pedagógico](docs/PEDAGOGICAL_MODEL.md)
- [Decisiones de arquitectura](docs/DECISIONS.md)
- [Hoja de ruta](ROADMAP.md)
- [Historial](CHANGELOG.md)
