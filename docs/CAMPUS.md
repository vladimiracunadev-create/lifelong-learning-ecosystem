# 🧭 Campus federado de aprendizaje

![Mapa del campus federado](assets/campus-federado.svg)

Este repositorio existe para **orientar dentro de los programas, laboratorios y aplicaciones educativas que ya existen** en la cuenta pública [`vladimiracunadev-create`](https://github.com/vladimiracunadev-create). No reemplaza sus clases ni transforma toda relación temática en un prerrequisito. Su trabajo es mostrar qué hay, cómo se recorre en su fuente, qué vínculos declara y qué falta revisar.

La comparación con un campus ayuda a navegar:

- cada **repositorio especializado** conserva sus clases, laboratorios, apps, fuentes, licencia y forma de avance;
- cada **área** reúne repositorios que comparten un campo, sin afirmar equivalencia entre ellos;
- cada **flujo nativo** reproduce una secuencia, ruta, nivel, módulo, caso o academia que el propio repositorio declara;
- una **conexión federada** solo se presenta como verificada cuando se han revisado objetivos, prerrequisitos, práctica y transferencia en unidades concretas.

No es una universidad acreditada y no entrega matrícula, créditos, títulos ni habilitación profesional.

## 🚪 Cómo entrar

| Si buscas… | Empieza aquí | Qué encontrarás |
| --- | --- | --- |
| un área completa | una de las seis áreas de abajo | programas, laboratorios, apps y entradas directas |
| una secuencia ya definida | [flujos nativos](NATIVE_LEARNING_FLOWS.md) | rutas que existen dentro de 30 repositorios revisados |
| clases y profundidad disciplinar | el repositorio fuente | su índice, partes, módulos, prácticas y evaluación |
| una conexión entre repositorios | [vínculos explícitos](NATIVE_LEARNING_FLOWS.md#-vínculos-entre-repositorios-que-sí-están-declarados) | enlaces publicados por los propios programas, con su alcance |
| criterios para aceptar una relación | [niveles de evidencia](#-cómo-se-acepta-una-conexión) | diferencia entre metadato, README, índice, unidad y relación verificada |
| los cinco diseños editoriales iniciales | [mallas experimentales](../curricula/README.md) | propuestas del maestro; ninguna es el inicio predeterminado |

## 🏫 Áreas del campus

### 💻 [Software y computación](faculties/SOFTWARE_COMPUTING.md)

Ingeniería de software, lenguajes, frameworks, bases de datos, videojuegos y resolución de problemas de sistemas. Incluye secuencias de **74 a 480 clases**, rutas por rol y laboratorios ejecutables.

Repositorios principales: [`modern-software-engineering-program`](https://github.com/vladimiracunadev-create/modern-software-engineering-program), [`polyglot-programming-labs`](https://github.com/vladimiracunadev-create/polyglot-programming-labs), [`framework-ecosystems-labs`](https://github.com/vladimiracunadev-create/framework-ecosystems-labs), [`database-systems-labs`](https://github.com/vladimiracunadev-create/database-systems-labs), [`modern-gamedev-program`](https://github.com/vladimiracunadev-create/modern-gamedev-program) y [`problem-driven-systems-lab`](https://github.com/vladimiracunadev-create/problem-driven-systems-lab).

### 🧠 [Datos, inteligencia artificial y ciencia](faculties/DATA_AI_SCIENCE.md)

Matemática, Python y datos, evolución de la IA, entrenamiento de redes neuronales y un laboratorio científico de genómica. Los flujos incluyen partes secuenciales, papers, notebooks y módulos con prerrequisitos declarados.

Repositorios principales: [`computational-mathematics-program`](https://github.com/vladimiracunadev-create/computational-mathematics-program), [`python-data-science-program`](https://github.com/vladimiracunadev-create/python-data-science-program), [`artificial-intelligence-evolution-program`](https://github.com/vladimiracunadev-create/artificial-intelligence-evolution-program), [`neural-network-training-labs`](https://github.com/vladimiracunadev-create/neural-network-training-labs) y [`human-genome-labs`](https://github.com/vladimiracunadev-create/human-genome-labs).

### ☁️ [Cloud, sistemas y seguridad](faculties/CLOUD_SYSTEMS_SECURITY.md)

Infraestructura multicloud, ciberseguridad, virtualización, contenedores, proyectos AWS, aislamiento y pagos. Aquí conviven programas extensos, laboratorios progresivos y casos independientes; no comparten una secuencia única.

Repositorios principales: [`multi-cloud-engineering-program`](https://github.com/vladimiracunadev-create/multi-cloud-engineering-program), [`modern-cybersecurity-program`](https://github.com/vladimiracunadev-create/modern-cybersecurity-program), [`qemu-kvm-labs`](https://github.com/vladimiracunadev-create/qemu-kvm-labs), [`docker-labs`](https://github.com/vladimiracunadev-create/docker-labs), [`proyectos-aws`](https://github.com/vladimiracunadev-create/proyectos-aws), [`sandbox-labs`](https://github.com/vladimiracunadev-create/sandbox-labs) y [`universal-payments-engineering-lab`](https://github.com/vladimiracunadev-create/universal-payments-engineering-lab).

### 📈 [Empresa, finanzas y liderazgo](faculties/BUSINESS_FINANCE_LEADERSHIP.md)

Creación y operación de empresas, finanzas y banca, marketing y ventas, dirección, blockchain y pagos. Varias fuentes publican rutas por rol y casos integradores; otras ofrecen una academia dentro de la aplicación.

Repositorios principales: [`modern-business-creation-program`](https://github.com/vladimiracunadev-create/modern-business-creation-program), [`empresa-operativa-chile`](https://github.com/vladimiracunadev-create/empresa-operativa-chile), [`finance-and-banking-evolution-program`](https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program), [`marketing-sales-growth-evolution-program`](https://github.com/vladimiracunadev-create/marketing-sales-growth-evolution-program), [`executive-leadership-founder-program`](https://github.com/vladimiracunadev-create/executive-leadership-founder-program), [`blockchain-learning-path`](https://github.com/vladimiracunadev-create/blockchain-learning-path) y [`universal-payments-engineering-lab`](https://github.com/vladimiracunadev-create/universal-payments-engineering-lab).

### 🎓 [Escuela, pedagogía y evaluación](faculties/EDUCATION_ASSESSMENT.md)

Trayectoria escolar chilena de 1.º básico a 4.º medio, formación pedagógica con rutas por rol y psicometría con estado desigual entre instrumentos, laboratorios y clases.

Repositorios principales: [`chilean-school-learning-path`](https://github.com/vladimiracunadev-create/chilean-school-learning-path), [`education-pedagogy-learning-sciences-program`](https://github.com/vladimiracunadev-create/education-pedagogy-learning-sciences-program) y [`psychometrics-and-assessment-program`](https://github.com/vladimiracunadev-create/psychometrics-and-assessment-program).

### 🎨 [Arte, espacio y oficios](faculties/ARTS_SPACE_TRADES.md)

Arquitectura y entorno construido, operación de maquinaria, guitarra, violín y cueca. Los flujos van desde 680 clases y 12 rutas hasta experiencias breves guiadas por mundos, niveles y habilidades.

Repositorios principales: [`architecture-built-environment-learning-program`](https://github.com/vladimiracunadev-create/architecture-built-environment-learning-program), [`machine-operator-program`](https://github.com/vladimiracunadev-create/machine-operator-program), [`guitarra-adventure`](https://github.com/vladimiracunadev-create/guitarra-adventure), [`violin-adventure`](https://github.com/vladimiracunadev-create/violin-adventure) y [`panuelo-al-viento-cueca-app`](https://github.com/vladimiracunadev-create/panuelo-al-viento-cueca-app).

## 🛤️ Qué significa “malla” en este ecosistema

![Tipos de flujo existentes](assets/tipos-de-flujo.svg)

La cuenta no usa una sola forma de organizar el aprendizaje. En la revisión de 30 README aparecen seis estructuras reales:

1. **Secuencia:** partes y clases numeradas que la fuente pide recorrer en orden.
2. **Ruta:** selección por rol, perfil, objetivo o especialidad dentro de un programa.
3. **Nivel:** curso escolar, mundo, semana o habilidad con progresión propia.
4. **Módulo:** agrupación temática con prerrequisitos o resultados declarados.
5. **Caso o laboratorio:** problema ejecutable que produce evidencia; puede ser progresivo o independiente.
6. **Academia en una app:** contenido, práctica y progreso dentro de una aplicación local u offline.

Por eso este maestro presenta primero los **flujos nativos**. Las cinco mallas `M-01`…`M-05` son diseños editoriales iniciales del maestro y no resumen todo el ecosistema. Permanecen disponibles para revisión, sin elegir M-01 ni otra como punto de partida automático.

## 🔎 Cómo se acepta una conexión

![Escalera de evidencia para conectar repositorios](assets/niveles-de-evidencia.svg)

| Nivel | Evidencia leída | Qué puede afirmarse |
| --- | --- | --- |
| 1 · metadato | nombre y descripción pública | el repositorio existe y declara un tema |
| 2 · README | portada y enlaces principales | alcance, estado y flujo declarado en la portada |
| 3 · índice | currículo, rutas, partes o módulos | estructura interna y puntos de entrada observados |
| 4 · unidad | clase, práctica, laboratorio y criterios | correspondencia candidata con resultados concretos |
| 5 · relación verificada | unidades de ambos lados y transferencia | prerrequisito o continuidad defendible y revisada |

La revisión actual llega a README en los 30 repositorios del [mapa de flujos](NATIVE_LEARNING_FLOWS.md), a índices en una parte de ellos y a unidad solo en integraciones puntuales. Por eso los vínculos temáticos se muestran como navegación y no como equivalencias académicas.

## 📌 Alcance actual

- **68 repositorios públicos observados:** 64 propios y 4 forks, según la API pública de GitHub el 6 de octubre de 2026.
- **30 README educativos revisados** en este bloque para identificar su flujo nativo.
- **14 integraciones canónicas** con IDs técnicos, competencias y fichas ya incorporadas.
- **16 repositorios educativos adicionales** documentados sin asignarles automáticamente un ID canónico.
- **5 mallas editoriales iniciales** conservadas como experimentales y opcionales.

El inventario completo, incluidos productos y repositorios revisados solo por metadatos, está en [descubrimiento de repositorios](../catalog/REPOSITORY_DISCOVERY.md). El detalle de los 14 registros canónicos está en el [atlas](PROGRAM_ATLAS.md).
