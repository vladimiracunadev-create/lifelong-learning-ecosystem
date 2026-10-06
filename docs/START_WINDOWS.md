# Inicio en Windows

## Leer el proyecto

1. Descarga el ZIP.
2. En el Explorador de archivos, usa **Extraer todo**.
3. Abre la carpeta `lifelong-learning-ecosystem` que quedó extraída.
4. Haz doble clic en `index.html` o en `ABRIR_PORTAL.cmd`.

Se abrirá el navegador predeterminado. El lector incluye el catálogo, las competencias, mallas, apoyos, rúbricas y documentación de esta entrega. No requiere instalar un servidor, Node, Docker ni Python para leer.

Los enlaces hacia otros repositorios abren recursos externos. Para consultar sus clases sin conexión deberás disponer de una copia local de esos materiales. Esta entrega no descarga automáticamente repositorios ajenos.

## Editar

Puedes abrir la carpeta con tu editor habitual. Los archivos Markdown contienen la documentación. Los cinco archivos JSON descritos en [el contrato](DATA_CONTRACT.md) son los registros canónicos.

Después de cambiar esos archivos, reconstruye el lector. Modificar solo index.html produce un cambio que se perderá al volver a generarlo.

## Usar las herramientas

Las herramientas requieren Python 3.11 o superior. Si ya tienes uv y Python disponibles, abre una terminal dentro de la carpeta:

~~~powershell
uv run --offline python scripts/validate.py
uv run --offline python -m unittest discover -s tests -v
uv run --offline python scripts/build_portal.py
~~~

También puedes ejecutar directamente Python:

~~~powershell
py -3 scripts/validate.py
py -3 -m unittest discover -s tests -v
py -3 scripts/build_portal.py
~~~

El modo offline de uv presupone que hay un intérprete compatible disponible localmente. Si uv indica que debe descargar Python, utiliza el intérprete instalado o prepara el entorno mediante tu procedimiento habitual. Los scripts del proyecto solo utilizan biblioteca estándar.

`VALIDAR.cmd` y `RECONSTRUIR_PORTAL.cmd` buscan uv, después el lanzador py y finalmente python. Muestran los mensajes y mantienen abierta la ventana para poder leerlos.

## Exportar una malla

Desde la carpeta raíz:

~~~powershell
py -3 scripts/export_plan.py --route M-03 --output exports/mi-plan.md
~~~

La exportación crea una copia editable de la malla. La selección de una ruta no acredita sus competencias. Guarda tus evidencias y decisiones en un espacio privado.

## Preparar un repositorio Git

Este ZIP incluye el código y la documentación; puedes usar la carpeta extraída como base de un nuevo repositorio llamado **lifelong-learning-ecosystem**.

Antes de subir archivos, revisa que los ejemplos sigan siendo ficticios y que tus exportaciones estén fuera de los archivos versionados. El paquete excluye de Git las carpetas locales private y exports.

La creación y publicación remota no se realizaron como parte de esta entrega.

## Problemas habituales

| Situación | Acción |
| --- | --- |
| Se ve el contenido del ZIP pero los enlaces no funcionan | Extraer todo y abrir el archivo de la carpeta extraída |
| index.html no refleja una edición | Reconstruir y recargar la página |
| Python o uv no se reconocen | Leer el portal sin instalación; para las herramientas, usar un intérprete compatible instalado |
| Un enlace externo no abre | Comprobar conectividad y vigencia de la fuente |
| El validador informa un ID desconocido | Revisar el registro de origen y sus referencias |
| Una competencia figura en el plan pero no fue demostrada | Mantenerla pendiente y acordar la evidencia necesaria |

La verificación de esta entrega se realizó en el entorno indicado en [quality/STATUS.md](../quality/STATUS.md). Las instrucciones para Windows usan rutas y comandos compatibles, pero no equivalen a una prueba nativa en tu equipo.
