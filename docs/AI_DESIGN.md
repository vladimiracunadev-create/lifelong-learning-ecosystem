# Diseño de acompañamiento mediante IA

## Estado

Este documento especifica una capacidad futura. La versión 0.1.0 entrega datos, rutas curadas y lector local; no llama a una API de modelos ni incorpora credenciales.

## Funciones previstas

- Localizar objetivos, competencias y recursos dentro del catálogo.
- Explicar requisitos y alternativas de ingreso.
- Proponer combinaciones de recorridos con sus fuentes.
- Sugerir apoyos ante una dificultad descrita.
- Ayudar a revisar una evidencia con criterios explícitos.
- Identificar cambios de un programa que afecten a una malla.
- Registrar decisiones para continuar una tarea después de una pausa.

Cada función se desarrollará cuando exista un caso verificable y un criterio de aceptación.

## Entradas mínimas

La persona describe un objetivo y puede aportar contexto, conocimientos previos, recursos disponibles y preferencias. No se infiere un diagnóstico ni un nivel general a partir de la edad, situación laboral o forma de escribir.

Las evidencias opcionales se usan para una tarea acotada y con alcance visible. El sistema debe permitir usar el catálogo sin registrar un perfil.

## Contrato propuesto de recomendación

| Campo | Contenido |
| --- | --- |
| goal | Objetivo interpretado de la persona |
| assumptions | Supuestos que influyen en la propuesta |
| candidate_routes | IDs de mallas curadas y razones de pertinencia |
| prerequisite_gaps | Requisitos con evidencia insuficiente |
| evidence_considered | Evidencias realmente consultadas |
| program_refs | IDs, URLs y versiones de las fuentes utilizadas |
| proposed_steps | Secuencia recomendada y apoyos |
| alternatives | Recorridos alternativos con sus diferencias |
| uncertainty | Aspectos que aún deben revisarse |
| next_action | Una acción concreta y proporcionada |
| decision_status | Propuesta, revisada o adoptada por la persona |

Un ID inexistente es un error que debe corregirse antes de presentar la propuesta como integrada. Las recomendaciones externas al catálogo se marcan como pendientes de revisión.

## Flujo de recomendación

1. Interpretar el objetivo y mostrarlo.
2. Recuperar únicamente registros pertinentes.
3. Comparar requisitos con evidencias disponibles.
4. Proponer pasos y explicar sus relaciones.
5. Mostrar alternativas y vacíos.
6. Permitir revisión por la persona o formador.
7. Guardar solo la información necesaria en el espacio adecuado.

Cuando el objetivo es insuficiente, conviene hacer una pregunta concreta. La ausencia de respuesta no autoriza a inventar datos ni a asignar nivel.

## Retroalimentación sobre una evidencia

La devolución identifica un criterio, señala una observación del trabajo y propone una mejora comprobable. Si no se puede abrir un archivo o falta una parte, se declara qué no se evaluó.

El uso de una rúbrica genera observaciones para revisión. Los estados de dominio y la acreditación de experiencia requieren reglas y evidencias acordadas; no deben inferirse de haber leído una página.

## Contexto y continuidad

La continuidad se conserva mediante archivos de estado que registran alcance, decisiones, fuentes, cambios y siguiente acción. El repositorio es la fuente del estado de implementación; la memoria de una conversación es una pista que se contrasta.

No se promete memoria ilimitada. Un agente retoma leyendo un checkpoint breve y las fuentes relevantes, y valida que aún correspondan al repositorio.

## Fuentes no confiables e instrucciones

Los documentos recuperados se tratan como contenido para analizar. Un texto de un programa que instruya revelar secretos, modificar permisos o ignorar la tarea no se convierte en una orden del sistema.

Las acciones sobre repositorios, mensajería o publicación deben permanecer dentro del alcance autorizado y separado de la recomendación educativa.

## Evaluación de una implementación futura

Se deben probar casos como:
- Un adulto experto en un área e inicial en otra.
- Una persona que retoma tras una pausa.
- Una malla con un recurso externo desactualizado.
- Un estudiante que ofrece evidencia parcial.
- Una actividad que requiere una alternativa de acceso.
- Una propuesta del modelo con un ID inventado.
- Un texto recuperado con instrucciones ajenas a la tarea.

Criterios: referencias válidas, explicación consistente, incertidumbre visible, datos mínimos, posibilidad de corrección y ausencia de acreditaciones automáticas.

## Evolución técnica

Las interfaces de recuperación, recomendación y almacenamiento deben permitir sustituir el proveedor. El desarrollo inicial puede operar con reglas y búsqueda sobre datos locales. Incorporar un modelo tiene sentido cuando mejora una tarea evaluada y su costo y complejidad se justifican.
