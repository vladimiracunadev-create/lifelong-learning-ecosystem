# Desarrollo y mantenimiento local

## Requisitos

El proyecto utiliza Python 3.11 o superior y biblioteca estándar. El lector se distribuye ya construido como HTML autocontenido. Las herramientas de Python no tienen dependencias externas.

Se recomienda utilizar uv cuando esté disponible, de acuerdo con la preferencia del proyecto. Los comandos directos con Python realizan las mismas tareas.

## Registros técnicos canónicos

| Archivo | Registro |
| --- | --- |
| catalog/programs.json | Integraciones canónicas de programas y laboratorios |
| competencies/competencies.json | Competencias y niveles |
| curricula/mallas.json | Mallas y pasos |
| support/resources.json | Recursos de apoyo |
| assessment/rubrics.json | Rúbricas y criterios |

El registro de áreas pendientes está en catalog/pending.json. Los documentos explican decisiones y actividades; el [contrato](DATA_CONTRACT.md) define los campos de intercambio.

## Comprobaciones

~~~bash
python scripts/validate.py
python -m unittest discover -s tests -v
python scripts/build_portal.py --check
~~~

El validador comprueba archivos, campos, referencias, rutas, enlaces internos y ciclos de prerrequisitos. No consulta Internet ni certifica calidad educativa. Las pruebas deben demostrar que detecta errores relevantes sin rechazar relaciones permitidas.

Para un informe estructurado:

~~~bash
python scripts/validate.py --json
~~~

Para validar una copia:

~~~bash
python scripts/validate.py --root /ruta/a/lifelong-learning-ecosystem
~~~

## Reconstruir el lector

~~~bash
python scripts/build_portal.py
~~~

El resultado debe ser determinístico para los mismos archivos de entrada. `--check` compara la salida actual con la que correspondería generar y ayuda a detectar derivados obsoletos.

El contenido se incorpora al HTML durante la generación. El lector no depende de fetch para abrir archivos JSON locales ni de bibliotecas externas.

Si Node.js ya está disponible, hay una comprobación opcional de las funciones del lector con un DOM simulado, sin paquetes adicionales:

~~~bash
node tests/check_portal_dom.cjs
~~~

Esta comprobación recorre secciones, vistas de detalle y documentos, y ejercita filtros y escape de contenido. No representa un navegador real, no verifica estilos ni sustituye la revisión visual. Node no es necesario para leer el portal ni para las herramientas Python.

## Exportar un recorrido

~~~bash
python scripts/export_plan.py --route M-03 --output exports/mi-plan.md
~~~

La exportación no modifica el currículo. Crea una copia de trabajo para documentar decisiones personales. No considera una competencia acreditada por aparecer seleccionada.

## Editar con coherencia

1. Identifica el registro y los documentos afectados.
2. Conserva el identificador cuando persista la misma entidad.
3. Cambia datos y documentación.
4. Revisa referencias entrantes, prerrequisitos y transiciones.
5. Ejecuta las comprobaciones relevantes.
6. Reconstruye el lector.
7. Registra qué cambió y por qué.

Una revisión de fuente externa debe conservar la fecha y el alcance. El SHA de contenido obtenido de GitHub identifica el archivo consultado; no debe confundirse con un SHA de commit de todo el repositorio.

## Control de versiones y automatización

La validación local permite corregir antes de subir cambios. GitHub Actions vuelve a ejecutar las comprobaciones en Linux y Windows, comprueba el portal con Node 24, construye un ZIP reproducible, analiza Python y JavaScript con CodeQL y publica el portal solo después de un gate de calidad exitoso en `main`.

Las acciones de terceros están fijadas a commits completos. Dependabot propone actualizaciones semanales; cada pull request debe conservar el pin y comprobar la versión declarada. Consulta [Automatización y publicación](AUTOMATION.md) para conocer los workflows, permisos y protección recomendada de la rama.

## Empaquetado

El ZIP debe contener una carpeta raíz con todo el proyecto, sin entornos virtuales, cachés, perfiles privados, exportaciones personales, credenciales ni archivos temporales de investigación.

El manifiesto registra tamaño y hash SHA-256 de los archivos incluidos, salvo el propio manifiesto para evitar autorreferencia. Después de extraer, se deben volver a ejecutar las comprobaciones principales.

Tras validar y comprobar la vigencia del lector, se puede crear un paquete reproducible:

~~~bash
python scripts/package_release.py --output dist/lifelong-learning-ecosystem-v0.1.0.zip
~~~

El comando genera MANIFEST.json y rechaza sobreescribir un ZIP existente. Excluye los entornos, caches y carpetas privadas indicados anteriormente; verifica la integridad del archivo creado.

## Límites de versión 0.1.0

Esta versión no incluye cuentas, sincronización remota de progreso, evaluación psicométrica validada ni ejecución de un modelo de IA. Incluye los contratos, criterios y diseño que permitirán desarrollar esas capacidades cuando se definan sus requisitos concretos.
