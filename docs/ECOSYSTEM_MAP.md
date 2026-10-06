# 🗺️ Mapas del ecosistema

[← Abrir campus](CAMPUS.md) · [🛤️ Flujos nativos](NATIVE_LEARNING_FLOWS.md) · [📚 Atlas canónico](PROGRAM_ATLAS.md)

## Campus federado

![Campus federado con seis áreas](assets/campus-federado.svg)

Las áreas permiten orientarse; no sustituyen la estructura de cada repositorio. Algunos repositorios aparecen en más de un área porque su contenido cruza disciplinas.

## Arquitectura actual

```mermaid
flowchart TB
    GH[Cuenta pública<br/>68 repositorios observados] --> D[Descubrimiento verificable]
    D --> C[Campus Markdown<br/>6 áreas]
    D --> F[30 flujos nativos<br/>README revisado]
    D --> K[14 integraciones canónicas<br/>IDs y fichas]
    D --> O[Otros productos y herramientas<br/>sin clasificación educativa suficiente]

    C --> DOC[Documentación humana<br/>Markdown + SVG]
    F --> DOC
    K --> JSON[Índices técnicos JSON]
    DOC --> P[Portal público y offline]
    JSON --> P

    SRC[Repositorios fuente] -->|clases · labs · apps · fuentes| F
    SRC -->|procedencia| K
```

### Enlaces de la arquitectura

- [Campus humano](CAMPUS.md)
- [30 flujos nativos](NATIVE_LEARNING_FLOWS.md)
- [14 integraciones canónicas](PROGRAM_ATLAS.md)
- [68 repositorios observados](../catalog/REPOSITORY_DISCOVERY.md)
- [Arquitectura implementada](CURRENT_ARCHITECTURE.md)
- [Componentes propuestos, todavía no implementados](../PROPOSED_COMPONENTS.md)

## Áreas y repositorios revisados

```mermaid
flowchart LR
    CAMPUS[Brújula federada]
    CAMPUS --> SW[💻 Software]
    CAMPUS --> AI[🧠 Datos e IA]
    CAMPUS --> SYS[☁️ Cloud y seguridad]
    CAMPUS --> BIZ[📈 Empresa y finanzas]
    CAMPUS --> EDU[🎓 Educación]
    CAMPUS --> ART[🎨 Arte y oficios]

    SW --> SWE[Software Engineering]
    SW --> POLY[Polyglot]
    SW --> DB[Database Systems]
    SW --> GAME[GameDev]

    AI --> MATH[Matemática]
    AI --> DATA[Python Data Science]
    AI --> AIP[AI Evolution]
    AI --> NN[Neural Labs]

    SYS --> CLOUD[Multi-Cloud]
    SYS --> CYBER[Cybersecurity]
    SYS --> VM[QEMU/KVM]
    SYS --> PAY[Payments Lab]

    BIZ --> BUSINESS[Business Creation]
    BIZ --> FIN[Finance & Banking]
    BIZ --> MKT[Marketing]
    BIZ --> LEAD[Leadership]

    EDU --> SCHOOL[Trayectoria escolar]
    EDU --> PED[Pedagogía]
    EDU --> ASSESS[Psicometría]

    ART --> ARCH[Arquitectura]
    ART --> MACHINE[Maquinaria]
    ART --> MUSIC[Guitarra · Violín · Cueca]
```

Enlaces: [software](faculties/SOFTWARE_COMPUTING.md) · [datos e IA](faculties/DATA_AI_SCIENCE.md) · [cloud y seguridad](faculties/CLOUD_SYSTEMS_SECURITY.md) · [empresa y finanzas](faculties/BUSINESS_FINANCE_LEADERSHIP.md) · [educación](faculties/EDUCATION_ASSESSMENT.md) · [arte y oficios](faculties/ARTS_SPACE_TRADES.md).

## Formas reales de recorrer contenido

![Seis tipos de flujo](assets/tipos-de-flujo.svg)

```mermaid
flowchart LR
    E[Elegir repositorio] --> T{Flujo declarado}
    T --> S[Secuencia<br/>partes y clases]
    T --> R[Ruta<br/>rol o perfil]
    T --> N[Nivel<br/>curso o mundo]
    T --> M[Módulo<br/>especialidad]
    T --> L[Caso o laboratorio]
    T --> A[Academia en app]
    S --> V[Práctica y evidencia]
    R --> V
    N --> V
    M --> V
    L --> V
    A --> V
```

La tabla completa con entradas directas está en [mallas y flujos nativos](NATIVE_LEARNING_FLOWS.md).

## Relaciones entre repositorios

```mermaid
flowchart LR
    MATH[Computational Mathematics] -->|enlace publicado por AI| AI[AI Evolution]
    DATA[Python Data Science] -->|enlace publicado por AI| AI
    AI -->|ecosistema declarado| NN[Neural Network Labs]
    AI -->|ecosistema declarado| CLOUD[Multi-Cloud]
    AI -->|ecosistema declarado| CYBER[Cybersecurity]
    POLY[Polyglot] -->|enlaces de su README| DATA
    POLY -->|enlaces de su README| AI
    MKT[Marketing] -->|ecosistema declarado| DATA
    MKT -->|ecosistema declarado| AI
    CLOUD -->|ecosistema declarado| CYBER
```

Las flechas representan **enlaces observados en los README**, no prerrequisitos. El detalle y el alcance correcto están en [vínculos explícitos](NATIVE_LEARNING_FLOWS.md#-vínculos-entre-repositorios-que-sí-están-declarados).

## Escalera de evidencia

![Niveles de evidencia](assets/niveles-de-evidencia.svg)

```mermaid
flowchart LR
    A[1 · Metadato] --> B[2 · README]
    B --> C[3 · Índice]
    C --> D[4 · Unidad]
    D --> E[5 · Relación verificada]
```

Solo el nivel 5 permite afirmar una continuidad o equivalencia curricular entre repositorios. La mayoría de conexiones transversales actuales permanece en los niveles 2 o 3.

## Lugar de M-01…M-05

```mermaid
flowchart TB
    F[Flujos nativos de repositorios] --> NAV[Navegación principal]
    EXP[5 mallas editoriales iniciales] --> REVIEW[Área experimental y opcional]
    NAV --> PORTAL[Portal]
    REVIEW --> PORTAL
```

Las cinco mallas editoriales no definen el campus, no representan la totalidad del ecosistema y ninguna es inicio predeterminado. Se conservan en [curricula](../curricula/README.md) para revisar sus actividades puente y correspondencias externas.
