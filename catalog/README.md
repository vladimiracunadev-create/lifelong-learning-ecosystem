# Catálogo de programas y apoyos

El catálogo permite localizar qué programa puede aportar a un objetivo y qué falta revisar antes de incorporarlo a una malla. La fuente canónica es [programs.json](programs.json); [pending.json](pending.json) conserva áreas conocidas cuya URL actual no se verificó.

**Revisión:** 2026-10-05. **Cobertura inicial:** 14 repositorios identificados. Se leyeron once fragmentos iniciales de README y tres README completos; esta base no es una auditoría de todas sus clases ni un inventario exhaustivo de la cuenta.

## Programas identificados

| ID estable | Programa | Papel propuesto | Integración |
| --- | --- | --- | --- |
| `PRG-SCHOOL` | [Trayectoria Escolar Chile](https://github.com/vladimiracunadev-create/chilean-school-learning-path) | programa | [Ficha](../integrations/prg-school.md) |
| `PRG-PEDAGOGY` | [Pedagogía, Docencia y Ciencias del Aprendizaje](https://github.com/vladimiracunadev-create/education-pedagogy-learning-sciences-program) | programa | [Ficha](../integrations/prg-pedagogy.md) |
| `PRG-MATH` | [Matemática Computacional](https://github.com/vladimiracunadev-create/computational-mathematics-program) | programa_y_herramienta | [Ficha](../integrations/prg-math.md) |
| `PRG-SOFTWARE` | [Ingeniería de Software Moderna](https://github.com/vladimiracunadev-create/modern-software-engineering-program) | programa | [Ficha](../integrations/prg-software.md) |
| `PRG-ARCH` | [Arquitectura, Construcción y Entorno Habitado](https://github.com/vladimiracunadev-create/architecture-built-environment-learning-program) | programa | [Ficha](../integrations/prg-arch.md) |
| `PRG-FINANCE` | [Finanzas y Evolución Bancaria](https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program) | programa_y_herramienta | [Ficha](../integrations/prg-finance.md) |
| `PRG-BUSINESS` | [Creación y Evolución de Empresas](https://github.com/vladimiracunadev-create/modern-business-creation-program) | programa | [Ficha](../integrations/prg-business.md) |
| `PRG-CYBER` | [Ciberseguridad Moderna](https://github.com/vladimiracunadev-create/modern-cybersecurity-program) | programa | [Ficha](../integrations/prg-cyber.md) |
| `PRG-AI` | [Evolución de la Inteligencia Artificial](https://github.com/vladimiracunadev-create/artificial-intelligence-evolution-program) | programa | [Ficha](../integrations/prg-ai.md) |
| `LAB-NEURAL` | [Laboratorios de Entrenamiento de Redes Neuronales](https://github.com/vladimiracunadev-create/neural-network-training-labs) | laboratorio | [Ficha](../integrations/lab-neural.md) |
| `PRG-ASSESS` | [Psicometría y Evaluación](https://github.com/vladimiracunadev-create/psychometrics-and-assessment-program) | programa_y_herramienta | [Ficha](../integrations/prg-assess.md) |
| `PRG-MARKETING` | [Marketing, Ventas y Crecimiento](https://github.com/vladimiracunadev-create/marketing-sales-growth-evolution-program) | programa_y_herramienta | [Ficha](../integrations/prg-marketing.md) |
| `PRG-LEADERSHIP` | [Liderazgo Ejecutivo y Creación de Empresas](https://github.com/vladimiracunadev-create/executive-leadership-founder-program) | programa_y_herramienta | [Ficha](../integrations/prg-leadership.md) |
| `PRG-DATA` | [Python y Ciencia de Datos](https://github.com/vladimiracunadev-create/python-data-science-program) | programa_y_herramienta | [Ficha](../integrations/prg-data.md) |

## Cómo interpretar los registros

- `review.status` describe la lectura documental realizada. `readme_revisado` no significa revisión de todas las clases.
- `review.scope` precisa si se leyó un fragmento o el documento completo.
- `declared_content_status` atribuye al origen sus cifras y estados. Un índice de clases planificadas no se cuenta como clases desarrolladas.
- `human_validation` conserva la revisión humana pendiente o no comprobada. Las pruebas de software no reemplazan esta revisión.
- `entry_points` indica qué recurso fue leído y qué enlace solo apareció en el README.
- `competency_ids`, públicos y papel son propuestas del maestro. La alineación por unidad requiere el procedimiento de [selección](../integrations/UNIT_SELECTION.md).

## Distinciones que deben conservarse

La trayectoria escolar declara desarrollo interno y mantiene pendiente la revisión humana. Ingeniería de software diferencia doce clases desarrolladas, material de trabajo y enseñanza aún pendiente. Psicometría distingue cuarenta clases planificadas de cinco escritas. En los otros programas, los recuentos publicados se mantienen como declaraciones del README; no se convierten automáticamente en material validado para toda persona.

Un repositorio puede cumplir dos funciones: enseñar una disciplina y ofrecer herramientas de práctica. El papel `programa_y_herramienta` no significa que sus aplicaciones se hayan instalado o probado en esta entrega.

## Registrar un nuevo programa

1. Confirmar el nombre y repositorio exactos; si falta, conservarlo en pendientes.
2. Leer el README e índice y registrar fecha, fuente y alcance de la lectura.
3. Distinguir contenido desarrollado, planificado, revisión y condiciones de uso.
4. Seleccionar unidades concretas, competencias candidatas y evidencias.
5. Crear la ficha de integración y validar referencias internas.
6. Mover el pendiente al catálogo conservando la trazabilidad de la decisión.

Consultar [Cobertura y brechas](COVERAGE_AND_GAPS.md) para priorizar ampliaciones.
