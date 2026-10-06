# Componentes propuestos, no implementados

Fecha de análisis: **2026-10-05**.

Nada en este documento forma parte del producto actual. Cada propuesta parte de los límites comprobados en [la arquitectura actual](docs/CURRENT_ARCHITECTURE.md) y [el descubrimiento](catalog/REPOSITORY_DISCOVERY.md). La prioridad no autoriza su construcción.

## Criterios comunes

- Conservar JSON y Markdown legibles como fuente de verdad.
- Extender scripts y portal existentes antes de crear un servicio.
- No copiar cursos completos ni homogeneizar licencias o numeración.
- Exigir procedencia, alcance de lectura y estado de madurez en toda salida.

## Editor curricular

- **Problema:** editar JSON relacionados manualmente aumenta el riesgo de referencias inválidas.
- **Evidencia:** hoy los cambios pasan por archivos canónicos y un validador posterior.
- **Límite actual:** el validador detecta errores, pero no ofrece edición guiada.
- **Alternativas:** editor de texto con esquema JSON, plantillas y revisión por pull request.
- **Sin software nuevo:** sí; mejorar esquemas, ejemplos y mensajes del validador puede cubrir gran parte del problema.
- **Arquitectura propuesta:** interfaz local que escriba únicamente el contrato existente y muestre el diff antes de guardar.
- **Relación:** `catalog/`, `competencies/`, `curricula/`, `support/` y `assessment/`.
- **Esfuerzo:** medio.
- **Beneficio:** menos errores editoriales y revisión más clara.
- **Riesgos:** ocultar decisiones pedagógicas detrás de formularios o crear formatos paralelos.
- **Prioridad:** baja hasta observar fallos repetidos de edición.

## Visualizador de mallas

- **Problema:** el portal muestra recorridos, pero no permite explorar todas las dependencias como grafo interactivo.
- **Evidencia:** existen cinco mallas y relaciones validadas; la visualización actual es estática.
- **Límite actual:** navegación por secciones y detalles, sin análisis gráfico transversal.
- **Alternativas:** Mermaid generado, tablas de dependencias y exportaciones estáticas.
- **Sin software nuevo:** sí; primero ampliar diagramas generados en documentación.
- **Arquitectura propuesta:** vista local derivada de JSON, sin estado servidor ni datos personales.
- **Relación:** `curricula/curricula.json` y `competencies/competencies.json`.
- **Esfuerzo:** bajo a medio.
- **Beneficio:** detectar cuellos de botella y explicar continuidad.
- **Riesgos:** hacer parecer equivalentes relaciones con distinta evidencia.
- **Prioridad:** media, después de revisar la semántica de cada relación.

## Generador de rutas

- **Problema:** las cinco mallas son editoriales y no cubren todas las metas posibles.
- **Evidencia:** el portal solo filtra y presenta rutas existentes; `export_plan.py` exporta, no genera.
- **Límite actual:** no existe composición automática ni justificación calculada.
- **Alternativas:** plantillas manuales, entrevistas guiadas y copia editable de una malla.
- **Sin software nuevo:** sí; se pueden añadir mallas revisadas conforme aparezcan necesidades reales.
- **Arquitectura propuesta:** algoritmo determinista que proponga borradores y explique cada dependencia; revisión humana obligatoria.
- **Relación:** competencias, mallas, evidencias y apoyos.
- **Esfuerzo:** alto.
- **Beneficio:** ampliar combinaciones sin ocultar el razonamiento.
- **Riesgos:** recomendar rutas inadecuadas, convertir edad en dominio o presentar candidatos como equivalencias.
- **Prioridad:** baja hasta tener más correspondencias verificadas.

## Grafo de conocimiento

- **Problema:** las relaciones están distribuidas entre varios JSON y fichas.
- **Evidencia:** el maestro valida referencias, pero no mantiene una base de grafos ni consultas semánticas.
- **Límite actual:** “grafo” describe una forma de visualizar relaciones, no un componente operativo.
- **Alternativas:** índices derivados, Mermaid y consultas Python sobre JSON.
- **Sin software nuevo:** sí, para los volúmenes actuales.
- **Arquitectura propuesta:** proyección regenerable desde los JSON; nunca una segunda fuente de verdad.
- **Relación:** todos los registros canónicos y sus procedencias.
- **Esfuerzo:** medio.
- **Beneficio:** consultas transversales y detección de relaciones huérfanas.
- **Riesgos:** duplicación, ontología prematura y falsa precisión.
- **Prioridad:** baja.

## Motor de recomendaciones

- **Problema:** una persona debe interpretar por sí misma mallas, niveles y evidencias.
- **Evidencia:** no hay perfil computable ni recomendaciones dinámicas implementadas.
- **Límite actual:** filtros y orientaciones generales.
- **Alternativas:** guía de elección, tutor humano y formularios locales no persistentes.
- **Sin software nuevo:** parcialmente; mejorar preguntas y ejemplos puede resolver el caso inicial.
- **Arquitectura propuesta:** reglas explicables sobre datos locales, consentimiento y sin inferir diagnósticos.
- **Relación:** `pathways/`, competencias, apoyos y rúbricas.
- **Esfuerzo:** alto.
- **Beneficio:** orientar ingreso, retorno y próximos pasos.
- **Riesgos:** sesgo, privacidad, dependencia de datos incompletos y sobreconfianza.
- **Prioridad:** baja.

## Buscador transversal

- **Problema:** el portal no busca dentro de las clases externas.
- **Evidencia:** los documentos embebidos pertenecen al maestro; los cursos siguen en otros repositorios.
- **Límite actual:** navegación local y enlaces externos.
- **Alternativas:** búsqueda de GitHub, índices manuales y búsqueda del navegador.
- **Sin software nuevo:** sí para consultas ocasionales.
- **Arquitectura propuesta:** índice derivado de contenidos permitidos, con commit y licencia por documento.
- **Relación:** catálogo, integraciones y repositorios especializados.
- **Esfuerzo:** alto.
- **Beneficio:** localizar temas y evidencias entre programas.
- **Riesgos:** contenido obsoleto, licencias, costo de indexación y pérdida de contexto.
- **Prioridad:** media solo después de definir permisos y actualización.

## Analizador de programas

- **Problema:** comparar estados, estructuras y evidencia exige revisión repetida.
- **Evidencia:** este corte necesitó separar metadatos, README, estructura y afirmaciones declaradas.
- **Límite actual:** no existe extracción automática mantenida.
- **Alternativas:** checklist y ficha manual por repositorio.
- **Sin software nuevo:** sí para integraciones puntuales; es la alternativa recomendada ahora.
- **Arquitectura propuesta:** script de solo lectura que genere un borrador con procedencia, nunca una clasificación final.
- **Relación:** política de integración y catálogo.
- **Esfuerzo:** medio.
- **Beneficio:** auditorías comparables y detección de cambios.
- **Riesgos:** confundir patrones de archivos con calidad o estado real.
- **Prioridad:** media si el catálogo crece de forma sostenida.

## Sistema de evaluación

- **Problema:** las rúbricas se leen y aplican fuera del portal.
- **Evidencia:** hay tres rúbricas editoriales, pero no sesiones, calificaciones ni emisión de credenciales.
- **Límite actual:** documentación y datos, sin motor de evaluación.
- **Alternativas:** plantillas descargables, portafolio local y retroalimentación humana.
- **Sin software nuevo:** sí para pilotajes iniciales.
- **Arquitectura propuesta:** herramienta local opcional que separe evidencias privadas de criterios públicos.
- **Relación:** `assessment/`, `examples/` y exportaciones privadas.
- **Esfuerzo:** alto.
- **Beneficio:** trazabilidad de retroalimentación y reconocimiento previo.
- **Riesgos:** datos sensibles, uso de rúbricas no validadas como certificación y reducción de juicio experto.
- **Prioridad:** baja.

## Plataforma web dinámica

- **Problema:** el portal estático no ofrece cuentas, sincronización ni colaboración.
- **Evidencia:** `index.html` es autocontenido y Pages solo sirve archivos estáticos.
- **Límite actual:** lectura y navegación sin servidor.
- **Alternativas:** conservar el portal estático y usar archivos locales privados.
- **Sin software nuevo:** sí para el alcance público actual.
- **Arquitectura propuesta:** solo si aparece un caso validado; separar contenido público, identidad y evidencias privadas.
- **Relación:** podría consumir artefactos derivados del maestro, sin reemplazar los JSON.
- **Esfuerzo:** muy alto.
- **Beneficio:** colaboración y continuidad entre equipos.
- **Riesgos:** seguridad, privacidad, operación, accesibilidad y dependencia de proveedor.
- **Prioridad:** muy baja.

## CLI unificada

- **Problema:** hoy existen varios scripts con entradas separadas.
- **Evidencia:** validar, construir, exportar y empaquetar requieren comandos distintos.
- **Límite actual:** scripts funcionales, sin punto de entrada común.
- **Alternativas:** documentación, `Makefile` o script de tareas del sistema.
- **Sin software nuevo:** sí; documentar comandos sigue siendo suficiente.
- **Arquitectura propuesta:** envoltorio delgado sobre scripts existentes, sin nueva lógica de dominio.
- **Relación:** `scripts/`.
- **Esfuerzo:** bajo.
- **Beneficio:** descubribilidad y uso consistente.
- **Riesgos:** duplicar opciones y ocultar comandos reproducibles.
- **Prioridad:** baja.

## API pública

- **Problema:** consumidores externos no tienen consultas HTTP versionadas.
- **Evidencia:** los datos se distribuyen como archivos públicos y el portal no tiene backend.
- **Límite actual:** descarga directa de JSON y GitHub Raw.
- **Alternativas:** usar los archivos versionados, releases y Pages.
- **Sin software nuevo:** sí para consumo de solo lectura.
- **Arquitectura propuesta:** API generada o caché de solo lectura, con commit de procedencia.
- **Relación:** JSON canónicos.
- **Esfuerzo:** medio a alto.
- **Beneficio:** integración estable con clientes externos.
- **Riesgos:** operación, compatibilidad, abuso y crear dos contratos.
- **Prioridad:** muy baja.

## Agentes de IA

- **Problema:** revisar muchos repositorios y acompañar rutas puede consumir trabajo editorial.
- **Evidencia:** hay instrucciones para agentes de mantenimiento, pero no agentes que formen parte del producto.
- **Límite actual:** la automatización no decide integraciones ni rutas.
- **Alternativas:** prompts, checklists y revisión humana con herramientas generales.
- **Sin software nuevo:** sí; es la opción actual.
- **Arquitectura propuesta:** tareas acotadas, salidas citadas y aprobación humana antes de modificar datos canónicos.
- **Relación:** `AGENTS.md`, `prompts/` y flujos de revisión.
- **Esfuerzo:** alto.
- **Beneficio:** borradores y vigilancia de cambios.
- **Riesgos:** invención de componentes, referencias incorrectas, privacidad y cambios no autorizados.
- **Prioridad:** baja.

## Herramientas de mantenimiento adicionales

- **Problema:** el inventario externo puede cambiar después de cada corte.
- **Evidencia:** los scripts actuales validan el árbol local, pero no comparan la cuenta pública con el catálogo.
- **Límite actual:** descubrimiento editorial puntual.
- **Alternativas:** auditoría periódica manual con la API de GitHub.
- **Sin software nuevo:** sí mientras el ritmo de cambios sea manejable.
- **Arquitectura propuesta:** reporte de diferencias de solo lectura que muestre repositorios nuevos, archivados o renombrados; ninguna integración automática.
- **Relación:** `catalog/programs.json`, fichas y evidencia de revisión.
- **Esfuerzo:** bajo a medio.
- **Beneficio:** detectar drift sin alterar decisiones pedagógicas.
- **Riesgos:** tratar cambios de metadata como cambios curriculares o ejecutar consultas sin control de tasa.
- **Prioridad:** alta entre las propuestas, pero primero debe acordarse el formato del reporte.

## Orden recomendado si se autoriza trabajo futuro

1. Mantener la auditoría manual y verificar un candidato por vez.
2. Mejorar reportes de diferencias y visualizaciones derivadas.
3. Evaluar analizador y buscador solo con evidencia de carga real.
4. Posponer generación, recomendaciones, evaluación dinámica, API, plataforma y agentes hasta contar con correspondencias verificadas, necesidades de usuarios y reglas de privacidad.
