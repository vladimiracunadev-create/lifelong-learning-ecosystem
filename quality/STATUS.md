# Estado de entrega — 0.1.0

Fecha de revisión local: 2026-10-06.

## Entrega disponible

Campus federado con **seis áreas documentadas**, **30 flujos nativos revisados**, **tres mapas SVG**, **14 integraciones canónicas**, **36 competencias y 216 descriptores**, **cinco mallas editoriales experimentales con 30 pasos**, **diez apoyos**, **tres rúbricas con 16 criterios**, **14 fichas de integración**, guía de primera infancia con **seis experiencias acompañadas**, **99 documentos Markdown** embebidos y herramientas locales.

El lector index.html abre por el campus y los flujos reales; incorpora los tres SVG de forma autocontenida, además del catálogo, las mallas editoriales, los apoyos, las rúbricas y la documentación. Las clases externas siguen en sus repositorios. La API pública confirmó 68 repositorios —64 propios y 4 forks—; los candidatos no reciben automáticamente un ID canónico. Hay cuatro registros pendientes para derecho, psicología, libros y continuidad infantil completa.

## Verificaciones técnicas realizadas

| Comprobación | Resultado |
| --- | --- |
| Suite Python | 41 pruebas correctas |
| Datos y referencias | Seis JSON registrados; IDs, tipos, descriptores y relaciones coherentes |
| Prerrequisitos | Sin ciclos prohibidos; continuidad entre mallas permitida |
| Enlaces | Rutas locales, fragmentos y navegación declarada del lector verificados |
| Enlaces de aprendizaje | 52 rutas directas a índices, clases, módulos, laboratorios y currículos confirmadas mediante la API de GitHub |
| Lector | Generación determinística y comprobación de vigencia |
| JavaScript | Sintaxis comprobada con Node |
| DOM simulado | Siete secciones, 68 vistas de detalle, 99 documentos embebidos, campus, SVG local seguro, tablas, listas y escape de contenido |
| Datos personales | private y exports excluidos de la generación y de la validación documental |
| Exportación | M-03 exportada por CLI, con resultados personales sin evaluar |
| Paquete | El empaquetador genera un ZIP con manifiesto SHA-256 y verifica su integridad y la copia extraída; el hash final se registra fuera del propio paquete para evitar autorreferencia |
| Automatización | Tres workflows: calidad multi-entorno, CodeQL y Pages después de calidad; acciones fijadas a SHAs completos |
| Arquitectura pública | Maestro, catálogo canónico, candidatos y propuestas futuras separados por evidencia y madurez |
| Guía de aprendizaje | Campus de seis áreas, 30 flujos nativos, atlas de 14 integraciones y mapas con enlaces directos |

Ejecución local fresca: **Windows · Python 3.12.9 · Node 24.11.1**. Las pruebas usan biblioteca estándar de Python. La comprobación de DOM usa Node y está incluida en tests/check_portal_dom.cjs. La evidencia remota se registra en [RELEASE_EVIDENCE.md](RELEASE_EVIDENCE.md); no se considera verde hasta observar el resultado final asociado al commit publicado.

La auditoría publicada en `b4f207f3e8a0374909d5a4c01c37065a230ed008` terminó con Calidad, CodeQL y Pages correctos. Después de integrar las actualizaciones automáticas no quedaron pull requests abiertos ni ramas remotas distintas de `main`.

El informe estructurado de validación se conserva en [validation.json](validation.json). El manifiesto de archivos se encuentra en MANIFEST.json, en la raíz del paquete.

## Límites de verificación de interfaz

Se realizó una revisión visual local en el navegador integrado: la portada, la navegación móvil y el SVG del campus se mostraron correctamente, sin errores de consola. Esta revisión no recorre todos los tamaños de pantalla ni todas las interacciones del portal publicado.

El lector está diseñado para abrirse mediante index.html desde la carpeta extraída. Las instrucciones y lanzadores de Windows están incluidos; su ejecución se debe comprobar en el equipo de destino.

## Alcance educativo

Las actividades puente, mallas, descriptores y rúbricas están desarrollados como propuestas editoriales. Las correspondencias externas son candidatas basadas principalmente en README y enlaces observados. Se leyeron fragmentos iniciales de once README y versiones completas de otros tres, con fuentes y SHA registrados.

No se ha auditado cada clase ni realizado un pilotaje con participantes. Los niveles y rúbricas no son instrumentos psicométricos validados ni otorgan una acreditación oficial.

La revisión editorial y aritmética, incluidas sus correcciones, está documentada en [REVIEW_NOTES.md](REVIEW_NOTES.md).

## Pendientes de evolución

- Identificar repositorios actuales de derecho, psicología y libros.
- Auditar y ampliar experiencias de primera infancia dirigidas al niño.
- Seleccionar unidades externas y verificar su correspondencia con una malla.
- Realizar revisión especializada y pilotajes de uso.
- Evaluar por separado cualquier componente propuesto; ninguno se considera implementado por aparecer en un plan.

Estas tareas amplían el alcance de la versión inicial y se organizan en ROADMAP.md. La revisión actual conserva la diferencia entre contenido original disponible, alineación candidata y evidencia educativa todavía pendiente.
