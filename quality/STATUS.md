# Estado de entrega — 0.1.0

Fecha de cierre: 2026-10-05.

## Entrega disponible

Superrepositorio federado inicial con **14 integraciones canónicas**, **36 competencias y 216 descriptores**, **cinco mallas con 30 pasos**, **diez apoyos**, **tres rúbricas con 16 criterios**, **14 fichas de integración**, guía de primera infancia con **seis experiencias acompañadas**, **92 documentos Markdown** en el árbol, prompt maestro íntegro y herramientas locales.

El lector index.html incorpora el catálogo, las mallas, los apoyos, las rúbricas y documentación. Las clases externas siguen en sus repositorios. Un corte adicional observó 68 repositorios públicos —64 propios y 4 forks— y documentó candidatos sin incorporarlos automáticamente al contrato canónico. Hay cuatro registros pendientes para derecho, psicología, libros y continuidad infantil completa.

## Verificaciones técnicas realizadas

| Comprobación | Resultado |
| --- | --- |
| Suite Python | 40 pruebas correctas |
| Datos y referencias | Seis JSON registrados; IDs, tipos, descriptores y relaciones coherentes |
| Prerrequisitos | Sin ciclos prohibidos; continuidad entre mallas permitida |
| Enlaces | Rutas locales, fragmentos y navegación declarada del lector verificados |
| Lector | Generación determinística y comprobación de vigencia |
| JavaScript | Sintaxis comprobada con Node |
| DOM simulado | Siete secciones, 68 vistas de detalle, 91 documentos embebidos, filtros, tablas, listas y escape de contenido |
| Datos personales | private y exports excluidos de la generación y de la validación documental |
| Exportación | M-03 exportada por CLI, con resultados personales sin evaluar |
| Paquete | El empaquetador genera un ZIP con manifiesto SHA-256 y verifica su integridad y la copia extraída; el hash final se registra fuera del propio paquete para evitar autorreferencia |
| Automatización | Tres workflows: calidad multi-entorno, CodeQL y Pages después de calidad; acciones fijadas a SHAs completos |
| Arquitectura pública | Maestro, catálogo canónico, candidatos y propuestas futuras separados por evidencia y madurez |
| Guía de aprendizaje | Propósito institucional, cinco rutas detalladas, atlas de 14 integraciones y mapas con enlaces directos |

Ejecución local fresca: **Windows · Python 3.12.9 · Node 24.11.1**. Las pruebas usan biblioteca estándar de Python. La comprobación de DOM usa Node y está incluida en tests/check_portal_dom.cjs. La evidencia remota se registra en [RELEASE_EVIDENCE.md](RELEASE_EVIDENCE.md); no se considera verde hasta observar el resultado final asociado al commit publicado.

La auditoría publicada en `b4f207f3e8a0374909d5a4c01c37065a230ed008` terminó con Calidad, CodeQL y Pages correctos. Después de integrar las actualizaciones automáticas no quedaron pull requests abiertos ni ramas remotas distintas de `main`.

El informe estructurado de validación se conserva en [validation.json](validation.json). El manifiesto de archivos se encuentra en MANIFEST.json, en la raíz del paquete.

## Límites de verificación de interfaz

No se realizó todavía una prueba visual del commit publicado en un navegador real. El navegador automatizable disponible no admite abrir archivos locales. La ejecución nativa en Windows, la comprobación de sintaxis y el DOM simulado permiten revisar el código y los contenidos recorridos, pero no certifican el renderizado visual ni todos los eventos de un navegador.

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
