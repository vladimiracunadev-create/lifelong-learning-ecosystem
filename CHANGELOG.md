# Historial de cambios

## Sin publicar — 2026-10-06

### Añadido

- Campus federado en Markdown con seis áreas, análisis por repositorio y enlaces directos a rutas, índices, laboratorios, aplicaciones y portales reales.
- Inventario de 30 flujos nativos observados: secuencias, rutas por rol o perfil, niveles, módulos, casos, laboratorios y academias en aplicaciones.
- Nueve mapas SVG versionables: campus, tipos de flujo, niveles de evidencia y una cabecera específica para cada una de las seis áreas.
- Renderizado seguro de SVG locales dentro del portal autocontenido, con rechazo de contenido activo y cobertura de pruebas.
- Tres workflows con responsabilidades separadas: calidad multi-entorno, análisis CodeQL y publicación de GitHub Pages después de un gate exitoso.
- Dependabot para GitHub Actions, plantilla de pull request y política pública de seguridad.
- Mapas Mermaid de la arquitectura federada, el ciclo de una trayectoria y la continuidad entre mallas.
- Documentación de automatización, permisos, evidencia y protección recomendada de `main`.
- Arquitectura actual verificada con una matriz de componentes existentes y límites explícitos.
- Descubrimiento de los 68 repositorios públicos observados, separando integraciones canónicas, candidatos revisados, productos, presencia pública y forks.
- `PROPOSED_COMPONENTS.md` con problema, evidencia, alternativas, arquitectura, esfuerzo, beneficio, riesgo y prioridad para cada oportunidad futura.
- Explicación profunda del repositorio como brújula curricular federada, incluida la comparación limitada con una universidad.
- Guía concreta de cinco rutas con entradas, seis pasos, productos, programas y opciones de continuidad.
- Atlas de las 14 integraciones con aporte, estado observado, alcance de revisión, mallas, enlaces y brechas.
- Mapas visuales enlazados entre metas, mallas, competencias y repositorios especializados.

### Cambiado

- La navegación principal comienza por áreas y repositorios reales; M-01…M-05 pasan a una sección experimental, opcional y sin selección predeterminada.
- Markdown y SVG quedan definidos como fuente de contenido y análisis; JSON se limita a índices técnicos, relaciones y validación.
- Las conexiones entre repositorios distinguen enlaces declarados por las fuentes de prerrequisitos o continuidades todavía no verificados.
- La presentación pública define explícitamente el proyecto como superrepositorio federado y capa de integración, no como un programa adicional.
- El portal y la guía de desarrollo reflejan la publicación web y los nuevos gates automatizados.
- La huella de fuentes del portal normaliza saltos de línea para producir los mismos bytes en Windows y Linux.
- Las referencias a 14 programas ahora dicen 14 integraciones canónicas y dejan claro que el catálogo no es una lista cerrada.
- Las capacidades futuras de IA, búsqueda, recomendación, API o plataforma se identifican como propuestas y no como producto implementado.
- Las acciones de artefactos y Pages incorporan las cuatro actualizaciones propuestas por Dependabot, conservando pins SHA completos.
- La portada y el portal ofrecen acceso directo al propósito, las rutas, el atlas y los mapas, y distinguen programas, laboratorios, guías y aplicaciones externas.

## 0.1.0 — 2026-10-05

### Incorporado

- Identidad del repositorio maestro y visión de aprendizaje durante toda la vida.
- Contrato de datos y reglas para integrar programas independientes.
- Catálogo inicial de 14 repositorios con fuente y alcance de revisión.
- Registro de disciplinas y experiencias pendientes de identificar o auditar.
- 36 competencias con seis niveles descriptivos.
- Cinco mallas con actividades puente originales y continuidad.
- Diez recursos de apoyo y tres rúbricas editoriales.
- Orientaciones para primera infancia acompañada, reconocimiento previo, retorno al aprendizaje y accesibilidad.
- Lector local autocontenido, herramientas de validación y exportación.
- Prompt maestro íntegro e instrucciones de continuidad para agentes.

### Alcance

Las correspondencias exactas entre clases externas y competencias no se consideran auditadas en esta entrega. La revisión pedagógica especializada y los pilotajes están pendientes. El estado técnico real se documenta en quality/STATUS.md.
