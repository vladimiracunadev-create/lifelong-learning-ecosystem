# Portal local del ecosistema

El archivo `index.html`, en la raíz del repositorio, es un lector autocontenido en español. Extrae el ZIP completo y ábrelo con doble clic en un navegador de Windows, macOS o Linux. No necesitas instalar Python para leerlo.

## Qué permite

- Explorar las cinco mallas y leer sus pasos, actividades, evidencias, criterios, apoyos y continuidad.
- Filtrar las rutas curadas por contexto de vida y palabras del objetivo. El filtro explica las coincidencias y no diagnostica conocimientos.
- Consultar programas identificados, el alcance de su revisión y sus puntos de entrada.
- Revisar las competencias, sus prerrequisitos y sus seis niveles de dominio.
- Abrir los apoyos y las rúbricas completos.
- Buscar y leer la documentación Markdown incluida sin instalar un editor.
- Aumentar el tamaño del texto e imprimir la vista actual.

Los contenidos y el lector están embebidos en `index.html`: no hay `fetch()`, CDN, servidor, instalación de paquetes ni conexiones de fondo. Los enlaces a GitHub y otras fuentes externas necesitan internet cuando decides abrirlos. Los archivos fuente conservan su ubicación relativa dentro del ZIP.

## Alcance de la primera versión

Las mallas son diseños iniciales con actividades originales. Los programas externos se referencian con su estado y alcance de revisión; una lectura de README no acredita la disponibilidad o eficacia de todas sus clases. El portal conserva estas diferencias y muestra los prerrequisitos propuestos.

El portal no guarda cuentas, perfiles, historiales ni evidencias personales. Las selecciones y los filtros viven en la sesión de la página. No calcula automáticamente el dominio de una competencia ni emite certificaciones. El constructor excluye las carpetas `private/` y `exports/`, además de las carpetas ocultas y de dependencias, para evitar incorporar planes y trabajos personales al HTML distribuido.

## Regenerar después de editar

Con Python 3.11 o posterior, desde la raíz del proyecto:

```bash
python scripts/build_portal.py
python scripts/build_portal.py --check
```

El primer comando genera `index.html` a partir de los cinco JSON canónicos, el catálogo pendiente si existe, la documentación Markdown y `portal/template.html`. El segundo compara la salida con una reconstrucción determinística y termina con código 1 si falta o está desactualizada. Un error de entradas o lectura termina con código 2 y conserva la salida anterior.

No se insertan fechas de construcción variables. La huella de fuentes cambia cuando cambian los datos, documentos, generador o plantilla. Conviene ejecutar la validación integral del repositorio antes de reconstruir el portal; el generador comprueba sus entradas necesarias, pero no sustituye esa validación.

## Archivos y mantenimiento

| Archivo | Responsabilidad |
| --- | --- |
| `portal/template.html` | HTML, estilos y JavaScript del lector. |
| `scripts/build_portal.py` | Lectura, comprobación de entradas y generación. |
| `index.html` | Salida derivada lista para abrir. |

Los cambios de contenido se realizan en los datos o documentos de origen. No edites a mano el HTML generado: la siguiente construcción lo reemplaza.

## Accesibilidad y lectura

La navegación utiliza enlaces y controles nativos, foco visible, etiquetas de formulario y un enlace para saltar al contenido. El diseño se adapta a pantallas pequeñas. Las tablas se desplazan horizontalmente cuando lo necesitan. La impresión elimina la navegación y despliega los detalles de la vista seleccionada.

El lector Markdown admite encabezados, párrafos, listas, citas, enlaces, tablas y bloques de código. El HTML de los documentos se muestra escapado; las imágenes se ofrecen como enlaces y no se descargan automáticamente. Los diagramas Mermaid se muestran como código fuente en esta edición offline.
