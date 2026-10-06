# Descubrimiento verificable de repositorios

Fecha de corte: **2026-10-05** · cuenta: `vladimiracunadev-create`.

Este registro amplía el inventario sin alterar los JSON canónicos. La API pública de GitHub mostró **68 repositorios públicos**, incluidos **4 forks**. Se revisaron metadatos de toda la superficie y, para los candidatos de aprendizaje que siguen, el README y la estructura raíz observables. No se auditaron todas sus clases ni se ejecutaron sus aplicaciones.

## Estados usados

| Marca | Significado en este análisis |
| --- | --- |
| EXISTENTE | Hay contenido implementado y verificable que puede describirse dentro de su alcance observado |
| EN DESARROLLO | El repositorio existe, pero su propio estado o su cobertura observada declara partes pendientes |
| EXPERIMENTAL | El repositorio identifica explícitamente el alcance como experimental |
| PLANIFICADO | Hay una decisión registrada, sin implementación comprobada |
| PROPUESTO | Se estudia una posibilidad en `PROPOSED_COMPONENTS.md` |
| IDEA | Mención sin análisis suficiente; no forma parte de la arquitectura |

`EXISTENTE` no significa eficacia educativa comprobada, producción certificada ni cobertura total.

## Integraciones canónicas actuales

Los siguientes 14 repositorios ya están registrados en `catalog/programs.json`: `architecture-built-environment-learning-program`, `artificial-intelligence-evolution-program`, `chilean-school-learning-path`, `computational-mathematics-program`, `education-pedagogy-learning-sciences-program`, `executive-leadership-founder-program`, `finance-and-banking-evolution-program`, `marketing-sales-growth-evolution-program`, `modern-business-creation-program`, `modern-cybersecurity-program`, `modern-software-engineering-program`, `neural-network-training-labs`, `psychometrics-and-assessment-program` y `python-data-science-program`.

La pertenencia al catálogo confirma una integración editorial existente, no que cada curso esté completo. El estado detallado y el alcance de lectura se conservan en cada entrada canónica y en su ficha de `integrations/`.

## Candidatos revisados: programas y currículos

| Repositorio exacto | Estado del alcance observado | Dominio · disciplina · subdisciplina | Propósito, nivel y profundidad | Público y prerrequisitos | Competencias, contenido, proyectos y evaluación observados | Relación posible, todavía no aprobada |
| --- | --- | --- | --- | --- | --- | --- |
| `vladimiracunadev-create/blockchain-learning-path` | EXISTENTE | tecnología · blockchain · Bitcoin, Ethereum, Solidity, custodia y forensics | currículo secuencial de 66 clases y 91 prácticas; de fundamentos a decisiones de producción | personas con interés técnico; el README remite a fundamentos y trabajo local/testnet | clases, prácticas, laboratorios, proyecto Andes Quest y criterios de aceptación; 356 pruebas declaradas | software, ciberseguridad, finanzas y sistemas distribuidos |
| `vladimiracunadev-create/database-systems-labs` | EXISTENTE | computación · bases de datos · modelado, motores, distribución, operación y recuperación | programa de 74 clases, 15 partes y 230 h declaradas | aprendizaje técnico; prerrequisitos exactos no establecidos en esta revisión | currículo, clases, laboratorios, proyectos, evaluaciones y comparación de 27 motores declarada | software, datos, cloud y sistemas |
| `vladimiracunadev-create/framework-ecosystems-labs` | EN DESARROLLO | software · frameworks · backend, frontend, datos y seguridad | 149 clases previstas; 70 declaradas construidas | personas que comparan ecosistemas; requisitos por clase no revisados | contratos comparables, labs, proyectos y evaluaciones; 397 casos CI declarados | ingeniería de software y programación políglota |
| `vladimiracunadev-create/machine-operator-program` | EXISTENTE | operación · maquinaria · sistemas, mandos, física, seguridad y simulación | 41 módulos, 451 clases y 502 h 15 min declaradas | futuros operadores y personas interesadas; requisitos legales o profesionales no establecidos | manuales, simuladores, vehículos y evaluación descritos; no habilita operación profesional por esta revisión | física, seguridad, operación y aprendizaje técnico |
| `vladimiracunadev-create/modern-gamedev-program` | EXISTENTE | software creativo · videojuegos · 2D/3D, motores, gameplay, backend y producción | 352 clases en 22 partes declaradas, desde fundamentos a nivel profesional | estudiantes de desarrollo de videojuegos; prerrequisitos por parte no revisados | clases, labs, rutas y autoevaluaciones; el README distingue CI de labs y código de clase no ejecutado | software, arte, matemática e IA |
| `vladimiracunadev-create/multi-cloud-engineering-program` | EXISTENTE | infraestructura · cloud · AWS, Azure, GCP, Kubernetes, Terraform, SRE y FinOps | 288 clases, 24 partes y 1.288 h declaradas | ingeniería cloud; prerrequisitos exactos no establecidos en esta revisión | 288 labs, capstones, proyectos, evaluaciones y evidencia JSON declarados | software, ciberseguridad, finanzas y operación |
| `vladimiracunadev-create/polyglot-programming-labs` | EXISTENTE | programación · lenguajes · comparación moderna e histórica | 176 clases en 12 partes; profundidad comparativa declarada | estudiantes y desarrolladores; requisitos por ruta no revisados | implementaciones, fichas, aplicaciones y CI; el README distingue lenguajes con distinta cobertura | software, bases de datos y fundamentos computacionales |

## Candidatos revisados: experiencias, laboratorios y productos educativos

| Repositorio exacto | Estado | Tipo y alcance observado | Clasificación pedagógica mínima | Relación posible |
| --- | --- | --- | --- | --- |
| `vladimiracunadev-create/universal-payments-engineering-lab` | EXISTENTE | laboratorio autoexplicativo de 28 familias de pagos, demo local, ledger, conciliación y seguridad | práctica de ingeniería financiera; nivel y prerrequisitos no establecidos | finanzas, software y seguridad |
| `vladimiracunadev-create/problem-driven-systems-lab` | EXISTENTE | 20 casos Docker-first de rendimiento, observabilidad, resiliencia y arquitectura | laboratorio basado en problemas; no se presenta como currículo secuencial | software, cloud y operación |
| `vladimiracunadev-create/docker-labs` | EXISTENTE | laboratorio personal de Docker/Compose en varios stacks | práctica técnica; evaluación y progresión no establecidas | software y cloud |
| `vladimiracunadev-create/qemu-kvm-labs` | EXISTENTE | 12 laboratorios de QEMU, KVM, libvirt y cloud-init | práctica de virtualización; evaluación no establecida | sistemas y cloud |
| `vladimiracunadev-create/proyectos-aws` | EN DESARROLLO | proyectos personales AWS en evolución | aprendizaje caso a caso; cobertura y evaluación no establecidas | cloud |
| `vladimiracunadev-create/human-genome-labs` | EXISTENTE | núcleo científico TypeScript, formatos genómicos, CLI, PWA y juego; madurez explícita por módulo | laboratorio científico; no se infiere un programa secuencial | ciencia, datos y software |
| `vladimiracunadev-create/guitarra-adventure` | EXISTENTE | app educativa offline con 24 lecciones en 6 mundos | iniciación musical desde 10 años declarada; práctica guiada | artes y aprendizaje por interés |
| `vladimiracunadev-create/violin-adventure` | EXISTENTE | app educativa offline con 24 lecciones en 6 mundos | iniciación musical desde 10 años declarada; práctica guiada | artes y aprendizaje por interés |
| `vladimiracunadev-create/panuelo-al-viento-cueca-app` | EXISTENTE | academia interactiva local-first con 24 clases y práctica por habilidades | cueca desde 10 años declarada; nivel posterior no establecido | artes, cultura y movimiento |
| `vladimiracunadev-create/empresa-operativa-chile` | EXISTENTE | producto con app, academia, currículo, labs y fuentes oficiales | aprendizaje aplicado a operación empresarial chilena; no sustituye asesoría profesional | negocios, finanzas y ciudadanía |
| `vladimiracunadev-create/aws-desktop-studio` | EN DESARROLLO | prototipo funcional con 15 integraciones de inventario y 20 tutoriales declarados | apoyo técnico, no currículo verificado | cloud y operación |
| `vladimiracunadev-create/sandbox-labs` | EXPERIMENTAL | 36 casos de aislamiento técnico y mercado de capitales simulado | laboratorio educativo explícitamente experimental | ciberseguridad, sistemas y finanzas |

## Superficie existente revisada solo por metadatos

Los repositorios restantes son reales, pero esta auditoría no leyó suficiente contenido interno para clasificarlos como programas. Se conservan por tipo observable y no se conectan a mallas:

- **Herramientas y productos:** `agentic-plugins-toolkit`, `ai-dataset-foundry`, `automa-pc`, `chofyai-studio`, `claude-skills-toolkit`, `codex-skills-toolkit`, `commerce-operating-system`, `decentraland-social-arcade`, `gabysql`, `langgraph-realworld`, `mcp-ollama-local`, `microsistemas`, `operational-ai-agents`, `pdf-reader-windows-android`, `rhino-suite`, `social-bot-scheduler`, `unikernel-labs`, `universal-code-scanner`, `video-transcript-studio`, `wsl-labs` y la familia `rootcause-*`.
- **Presencia pública:** `vladimiracunadev-create` y `vladimiracunadev-create.github.io`.
- **Forks excluidos de la arquitectura propia:** `Anthropic-Cybersecurity-Skills`, `erpnext`, `OpenExecutive` y `security-audit-skill`.

Esta agrupación no afirma que los productos carezcan de material educativo. Indica que no fueron revisados como currículo en este corte.

## Comparación y vacíos comprobados

1. El catálogo canónico cubre 14 integraciones, mientras la cuenta contiene otros programas y laboratorios verificables.
2. Los repositorios usan esquemas, niveles, nombres y estados diferentes; no hay un contrato transversal compartido.
3. Varios candidatos publican conteos y evaluaciones, pero el maestro no los valida ni normaliza.
4. Los prerrequisitos, públicos y niveles no siempre están explícitos en el README; esos campos quedan como “no establecidos”.
5. No existe un proceso implementado que vuelva a descubrir cambios y proponga diferencias con evidencia.

## Siguiente paso de integración

Seleccionar un solo candidato, fijar su commit, leer instrucciones, currículo, estado, índices, validadores y una muestra representativa de unidades; después redactar una ficha y proponer correspondencias candidatas. La asignación de un ID canónico y la modificación de los JSON deben ocurrir solo en ese bloque posterior.
