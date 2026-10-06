# Mapas del ecosistema

Este documento muestra cómo el superrepositorio conecta programas independientes sin absorberlos. Los JSON canónicos conservan el detalle; los diagramas explican la arquitectura y las transiciones editoriales de la versión 0.1.0.

## Mapa principal: de una meta a una especialidad

El recorrido no comienza eligiendo cientos de clases. Comienza con una meta, utiliza una malla para producir evidencia y abre después el programa especializado que aporta la profundidad necesaria.

```mermaid
flowchart LR
    G[Meta de aprendizaje] --> D[Diagnóstico y evidencia previa]
    D --> M{Elegir una malla}
    M --> M01[M-01<br/>bases y continuidad]
    M --> M02[M-02<br/>software]
    M --> M03[M-03<br/>reconversión]
    M --> M04[M-04<br/>proyecto interdisciplinario]
    M --> M05[M-05<br/>curiosidad y transmisión]
    M01 --> E[Evidencia integradora]
    M02 --> E
    M03 --> E
    M04 --> E
    M05 --> E
    E --> P[Profundizar en programas]
    P --> T[Transferir a otra situación]
    T --> N[Elegir continuidad, cambio o pausa]

    click M01 "../curricula/M-01-continuidad-escolar.md" "Abrir M-01"
    click M02 "../curricula/M-02-ingreso-especialidad-software.md" "Abrir M-02"
    click M03 "../curricula/M-03-reconversion-consultoria-tecnologica.md" "Abrir M-03"
    click M04 "../curricula/M-04-proyecto-comunitario-tecnologico.md" "Abrir M-04"
    click M05 "../curricula/M-05-memoria-espacio-cultural.md" "Abrir M-05"
```

Enlaces directos: [M-01](../curricula/M-01-continuidad-escolar.md) · [M-02](../curricula/M-02-ingreso-especialidad-software.md) · [M-03](../curricula/M-03-reconversion-consultoria-tecnologica.md) · [M-04](../curricula/M-04-proyecto-comunitario-tecnologico.md) · [M-05](../curricula/M-05-memoria-espacio-cultural.md).

## Red real entre mallas y repositorios

Cada línea representa una referencia existente en `curricula/mallas.json`. El laboratorio neuronal aparece separado porque está catalogado, pero todavía no forma parte de una malla.

```mermaid
flowchart TB
    M01[M-01<br/>Continuidad escolar]
    M02[M-02<br/>Ingreso a software]
    M03[M-03<br/>Reconversión]
    M04[M-04<br/>Proyecto comunitario]
    M05[M-05<br/>Interés y transmisión]

    SCHOOL[Trayectoria Escolar]
    MATH[Matemática Computacional]
    SOFTWARE[Ingeniería de Software]
    CYBER[Ciberseguridad]
    AI[Inteligencia Artificial]
    BUSINESS[Empresa]
    FINANCE[Finanzas]
    MARKETING[Marketing]
    LEADERSHIP[Liderazgo]
    ARCH[Arquitectura]
    DATA[Python y Datos]
    PEDAGOGY[Pedagogía]
    ASSESS[Psicometría y Evaluación]
    NEURAL[Neural Network Labs<br/>sin malla actual]

    M01 --> SCHOOL
    M01 --> MATH
    M02 --> SOFTWARE
    M02 --> CYBER
    M02 --> AI
    M03 --> BUSINESS
    M03 --> FINANCE
    M03 --> SOFTWARE
    M03 --> CYBER
    M03 --> MARKETING
    M03 --> LEADERSHIP
    M04 --> ARCH
    M04 --> SOFTWARE
    M04 --> CYBER
    M04 --> BUSINESS
    M04 --> FINANCE
    M04 --> DATA
    M04 --> LEADERSHIP
    M05 --> ARCH
    M05 --> SCHOOL
    M05 --> PEDAGOGY
    M05 --> ASSESS

    click SCHOOL "https://github.com/vladimiracunadev-create/chilean-school-learning-path" "Abrir Trayectoria Escolar"
    click MATH "https://github.com/vladimiracunadev-create/computational-mathematics-program" "Abrir Matemática Computacional"
    click SOFTWARE "https://github.com/vladimiracunadev-create/modern-software-engineering-program" "Abrir Ingeniería de Software"
    click CYBER "https://github.com/vladimiracunadev-create/modern-cybersecurity-program" "Abrir Ciberseguridad"
    click AI "https://github.com/vladimiracunadev-create/artificial-intelligence-evolution-program" "Abrir IA"
    click BUSINESS "https://github.com/vladimiracunadev-create/modern-business-creation-program" "Abrir Empresa"
    click FINANCE "https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program" "Abrir Finanzas"
    click MARKETING "https://github.com/vladimiracunadev-create/marketing-sales-growth-evolution-program" "Abrir Marketing"
    click LEADERSHIP "https://github.com/vladimiracunadev-create/executive-leadership-founder-program" "Abrir Liderazgo"
    click ARCH "https://github.com/vladimiracunadev-create/architecture-built-environment-learning-program" "Abrir Arquitectura"
    click DATA "https://github.com/vladimiracunadev-create/python-data-science-program" "Abrir Python y Datos"
    click PEDAGOGY "https://github.com/vladimiracunadev-create/education-pedagogy-learning-sciences-program" "Abrir Pedagogía"
    click ASSESS "https://github.com/vladimiracunadev-create/psychometrics-and-assessment-program" "Abrir Evaluación"
    click NEURAL "https://github.com/vladimiracunadev-create/neural-network-training-labs" "Abrir Neural Labs"
```

Consulta [el atlas de los 14 repositorios](PROGRAM_ATLAS.md) para leer su aporte, estado observado, límites y brechas.

## Capas de profundidad

```mermaid
flowchart TB
    L1[Orientación<br/>meta, contexto y punto de entrada]
    L2[Malla<br/>problema integrador de seis pasos]
    L3[Competencia<br/>resultado observable y prerrequisitos]
    L4[Programa especializado<br/>clases, unidades y práctica disciplinar]
    L5[Evidencia<br/>producto, explicación y variación]
    L6[Continuidad<br/>profundizar, cambiar, enseñar o pausar]
    L1 --> L2 --> L3 --> L4 --> L5 --> L6
```

Esta separación evita dos errores: tratar una lista de repositorios como ruta de aprendizaje y tratar una malla breve como sustituto de una especialidad completa.

## Arquitectura federada

```mermaid
flowchart LR
    P[Programas y laboratorios<br/>repositorios independientes] -->|fuentes y alcance revisado| I[Fichas de integración]
    I --> C[Catálogo canónico<br/>programas.json]
    C --> K[Competencias<br/>competencies.json]
    K --> M[Mallas<br/>mallas.json]
    S[Apoyos<br/>resources.json] --> M
    A[Rúbricas<br/>rubrics.json] --> M
    M --> R[Portal público y lector local<br/>index.html]
    D[Documentación y decisiones] --> R
    V[Validador y pruebas] -->|comprueban referencias,<br/>ciclos y vigencia| C
    V --> K
    V --> M
    V --> R
```

Los repositorios de origen mantienen su contenido, numeración, licencia y evolución. El superrepositorio registra procedencia, propone puentes y organiza recorridos transversales.

## Ciclo de una trayectoria

```mermaid
flowchart LR
    O[Definir propósito] --> E[Reconocer evidencia previa]
    E --> G[Elegir punto de entrada]
    G --> P[Practicar con apoyos]
    P --> V[Producir evidencia]
    V --> F[Recibir retroalimentación]
    F --> D{¿Cumple el criterio?}
    D -->|Aún no| P
    D -->|Sí| T[Transferir a otra situación]
    T --> N[Continuar, profundizar<br/>o cambiar de ruta]
    N --> O
```

La etapa vital orienta ejemplos y acompañamiento. El ingreso y el avance se justifican por competencias y evidencias pertinentes, no por edad.

## Continuidad entre las cinco mallas

Las flechas representan `next_routes`. Son opciones editoriales de continuidad y pueden formar ciclos; no son prerrequisitos obligatorios.

```mermaid
flowchart TD
    M01[M-01<br/>Continuidad escolar]
    M02[M-02<br/>Ingreso a software]
    M03[M-03<br/>Reconversión adulta]
    M04[M-04<br/>Proyecto comunitario]
    M05[M-05<br/>Interés y transmisión]

    M01 --> M02
    M01 --> M04
    M01 --> M05
    M02 --> M03
    M02 --> M04
    M02 --> M05
    M03 --> M02
    M03 --> M04
    M03 --> M05
    M04 --> M02
    M04 --> M03
    M04 --> M05
    M05 --> M01
    M05 --> M03
    M05 --> M04
```

| Malla | Punto de entrada | Programas conectados | Pasos | Continuidad declarada |
| --- | --- | ---: | ---: | --- |
| M-01 · Continuidad escolar | Sin competencia obligatoria | 2 | 6 | M-02, M-04, M-05 |
| M-02 · Ingreso a software | Lectura y herramientas digitales | 3 | 6 | M-03, M-04, M-05 |
| M-03 · Reconversión adulta | Comunicación y lectura | 6 | 6 | M-02, M-04, M-05 |
| M-04 · Proyecto comunitario | Comunicación y lectura | 7 | 6 | M-02, M-03, M-05 |
| M-05 · Interés y transmisión | Sin competencia obligatoria | 4 | 6 | M-01, M-03, M-04 |

## Lectura de los estados

- **Programa identificado:** existe un `owner/name` y una fuente observada.
- **Correspondencia candidata:** la evidencia disponible se limita principalmente al README o a un índice.
- **Correspondencia verificada por unidad:** requiere leer contenido específico, resultados, actividades y requisitos de la unidad.
- **Diseño inicial de malla:** contiene actividades, evidencias y criterios utilizables para revisión; aún no demuestra eficacia educativa.

Consulta el [contrato de datos](DATA_CONTRACT.md), la [política de integración](INTEGRATION_POLICY.md) y el [estado de entrega](../quality/STATUS.md) antes de interpretar o ampliar estos mapas.
