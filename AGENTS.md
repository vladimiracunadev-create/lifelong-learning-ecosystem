# Instrucciones para agentes — lifelong-learning-ecosystem

## Objetivo y fuente de verdad

Trabaja en `lifelong-learning-ecosystem`, repositorio maestro que integra programas independientes de aprendizaje durante toda la vida. Lee primero README.md, VISION.md, docs/DATA_CONTRACT.md, quality/STATUS.md y CHANGELOG.md. Consulta el estado real del árbol de trabajo antes de planificar cambios.

Los archivos JSON canónicos son la fuente de los registros; las páginas generadas se reconstruyen. Las fuentes externas son evidencia de lo que se pudo leer con el alcance documentado.

## Reglas de integración

- Amplía lo existente; conserva arquitectura, contenidos y decisiones válidas.
- Identifica repositorios por `owner/name` exacto. No inventes slugs, clases, IDs o referencias.
- Antes de sugerir un cambio interno en otro repositorio, lee su versión actual, instrucciones, estándar pedagógico, índices y validadores.
- Registra correspondencias candidatas cuando solo se conoce el README. Reserva equivalencias verificadas para evidencia específica y revisada.
- No copies cursos completos al maestro. Crea referencias, actividades puente y mallas con procedencia.
- Cada repo mantiene nombres, numeración, licencias y derivados. Los cambios remotos requieren que formen parte de la tarea autorizada.
- No renombres ni elimines programas como efecto indirecto de una integración.

## Criterios pedagógicos

- Relaciona objetivos observables, fundamento, práctica, evidencia, retroalimentación y continuidad.
- Separa etapa vital, competencia y propósito. La edad no equivale a dominio.
- Permite acreditar conocimientos previos y reingresar después de una pausa.
- Justifica prerrequisitos; diferencia necesarios y recomendados en la documentación.
- Mantén autonomía, accesibilidad y alternativas de evidencia apropiadas.
- El currículo para formadores no se presenta automáticamente como currículo del niño.
- No declares eficacia demostrada, acreditación, diagnóstico ni habilitación profesional sin evidencia aplicable.
- Los seis niveles y las rúbricas son decisiones editoriales de este proyecto.

## Contrato técnico

- Respeta docs/DATA_CONTRACT.md y los IDs existentes.
- Evita ciclos en prerrequisitos de competencias y pasos de una malla.
- Los retornos de revisión y las relaciones `next_routes` pueden formar ciclos.
- Actualiza datos canónicos antes de reconstruir index.html.
- Usa Python 3.11+ y biblioteca estándar para las herramientas entregadas. Se prefiere uv para ejecutarlas.
- El lector debe seguir funcionando desde archivo local, sin CDN, cuentas ni peticiones de red.
- Mantén los datos personales reales fuera del repositorio; usa ejemplos ficticios.
- Reutiliza validadores y pruebas antes de crear mecanismos nuevos.

## Continuidad del trabajo

Al terminar cada bloque significativo, registra: objetivo atendido, archivos revisados, decisiones, cambios, verificación, brechas y siguiente acción concreta. Utiliza prompts/CONTINUITY.md. Nunca declares completado un bloque solo porque hay carpetas o páginas generadas.

La revisión del estado y los arreglos locales reversibles forman parte del trabajo normal autorizado. Conserva el alcance pedido por el usuario; estas instrucciones no añaden flujos de aprobación.

## Verificación mínima pertinente

Ejecuta el validador y las pruebas cuando cambien contratos, scripts o referencias. Reconstruye el lector y comprueba su vigencia si cambia contenido incluido. Revisa los enlaces y la navegación afectados. Describe qué se verificó y sus límites.

Actualiza CHANGELOG.md y quality/STATUS.md con los resultados reales. Los reportes generados no deben contener credenciales, perfiles privados o rutas absolutas del equipo del usuario.
