# Auditoría de evidencia de publicación · 2026-10-05

## Identidad

- Repositorio público: `vladimiracunadev-create/lifelong-learning-ecosystem`.
- Rama objetivo: `main`.
- Producto: superrepositorio federado y portal autocontenido, versión 0.1.0.
- Entorno local fresco: Windows, Python 3.12.9 y Node 24.11.1.

El primer commit publicado fue `dea81af5b0ec4740afb9ed787e73676f3cdefd79`. Su ejecución de Calidad detectó una huella del portal dependiente de CRLF/LF en Windows. La corrección `b4b657edac8e2868bf454805800b3cf793137a48` normaliza las fuentes, añade una prueba de regresión y terminó verde en Calidad, Seguridad y Pages.

La auditoría de arquitectura y repositorios reales se publicó como `b4f207f3e8a0374909d5a4c01c37065a230ed008`. También terminó verde en Calidad, Seguridad y Pages. Las cuatro actualizaciones de Actions propuestas por Dependabot se incorporaron en ese commit; sus PR se cerraron y sus ramas se eliminaron.

## Matriz de afirmaciones

| Plataforma/artefacto | Afirmación | Fuente canónica | Nivel de evidencia | Resultado | Referencia |
| --- | --- | --- | --- | --- | --- |
| Datos | Los registros y referencias son coherentes | JSON y `scripts/validate.py` | Ejecución local fresca | Correcto | `quality/validation.json` |
| Python | La suite protege contrato, rutas, privacidad, SVG, exportación y huellas entre plataformas | `tests/` | Ejecución local fresca | 41/41 correctas | `python -m unittest discover -s tests -v` |
| Portal | El derivado coincide con sus fuentes | `portal/template.html`, datos y docs | Ejecución local fresca | Vigente | `python scripts/build_portal.py --check` |
| Portal | Secciones, detalles, campus, SVG local y escape funcionan en DOM controlado | `tests/check_portal_dom.cjs` | Ejecución local fresca | Correcto | 7 secciones, 68 detalles, 99 documentos |
| GitHub Actions | Los workflows tienen sintaxis y referencias válidas | `.github/workflows/` | Resultado remoto comprobado | GitHub aceptó y ejecutó los tres workflows | Enlaces de ejecución en la sección remota |
| Portal público | Pages sirve el commit corregido | Workflow `Portal público` | Resultado remoto comprobado | Correcto | https://vladimiracunadev-create.github.io/lifelong-learning-ecosystem/ |

## Gates ejecutados

| Comando | Entorno | Resultado | Duración | Evidencia |
| --- | --- | --- | --- | --- |
| `python scripts/validate.py --json` | Windows · Python 3.12.9 | Correcto | < 10 s | 6 JSON, 14 integraciones, 36 competencias, 5 mallas |
| `python -m unittest discover -s tests -v` | Windows · Python 3.12.9 | Correcto | < 10 s | 41 pruebas |
| `python scripts/build_portal.py --check` | Windows · Python 3.12.9 | Correcto | < 10 s | La cifra de documentos y bytes se actualiza en cada corte |
| `node tests/check_portal_dom.cjs` | Windows · Node 24.11.1 | Correcto | < 10 s | 7 secciones, 68 detalles, 99 documentos, campus y SVG local seguros |

## Artefactos inspeccionados

| Artefacto | Procedencia/commit | Versión | Propiedades verificadas | Resultado |
| --- | --- | --- | --- | --- |
| `index.html` | Árbol local previo al commit público | 0.1.0 | Autocontenido, determinístico, tres SVG embebidos y sin fetch de datos | Correcto; tamaño registrado por el constructor en cada corte |
| ZIP local preliminar | Árbol local previo al commit público | 0.1.0 | Manifiesto SHA-256 e integridad de copia extraída | Correcto; el artefacto del commit final lo construirá CI |

## Resultados remotos

- [Calidad del primer commit](https://github.com/vladimiracunadev-create/lifelong-learning-ecosystem/actions/runs/37403748247): fallo en Windows por huella de saltos de línea; evidencia negativa utilizada para la corrección.
- [Seguridad del primer commit](https://github.com/vladimiracunadev-create/lifelong-learning-ecosystem/actions/runs/37403748254): ejecución iniciada para Python y JavaScript.
- [Pages posterior al primer gate](https://github.com/vladimiracunadev-create/lifelong-learning-ecosystem/actions/runs/37403793396): omitido correctamente porque Calidad no terminó verde.
- [Calidad de la corrección](https://github.com/vladimiracunadev-create/lifelong-learning-ecosystem/actions/runs/37404161735): correcta en la matriz configurada.
- [Seguridad de la corrección](https://github.com/vladimiracunadev-create/lifelong-learning-ecosystem/actions/runs/37404161751): CodeQL correcto para Python y JavaScript/TypeScript.
- [Pages de la corrección](https://github.com/vladimiracunadev-create/lifelong-learning-ecosystem/actions/runs/37404202163): correcto después de habilitar el sitio público con despliegue por workflow.
- [Calidad de la auditoría](https://github.com/vladimiracunadev-create/lifelong-learning-ecosystem/actions/runs/37405593947): correcta en Python 3.11 y 3.14 sobre Ubuntu, Python 3.12 sobre Windows, DOM Node 24 y paquete reproducible.
- [Seguridad de la auditoría](https://github.com/vladimiracunadev-create/lifelong-learning-ecosystem/actions/runs/37405593992): CodeQL correcto para Python y JavaScript/TypeScript.
- [Pages de la auditoría](https://github.com/vladimiracunadev-create/lifelong-learning-ecosystem/actions/runs/37405639483): publicación correcta del portal.

## Incidencias

| Severidad | Hallazgo | Impacto | Evidencia | Acción siguiente |
| --- | --- | --- | --- | --- |
| Alta | La primera ejecución detectó una huella distinta en Windows | El portal válido en Linux se consideraba desactualizado en Windows | La huella usaba bytes CRLF/LF sin normalizar | Normalizar fuentes de texto y cubrir ambos finales de línea con una prueba |
| Media | La revisión visual local no cubre todos los tamaños e interacciones | Puede existir una regresión fuera de la portada y el documento inspeccionado | Se revisaron portada móvil, navegación, SVG del campus y consola sin errores | Revisar también el portal publicado después de Pages |
| Media | `actionlint` no pudo ejecutarse localmente | La sintaxis específica de Actions depende de la primera validación remota | Windows bloqueó el proceso descargado antes de iniciarlo | Observar y corregir la primera ejecución de GitHub Actions |

## No comprobado y riesgo residual

- Ruleset o protección de rama, que GitHub permite completar después de crear la rama y sus checks.
- Enlaces externos vivos y revisión pedagógica especializada.

## Veredicto

- Portal y datos locales: evidencia local suficiente para continuar hacia la publicación.
- Publicación remota: el repositorio es público y el commit de corrección tiene Calidad, Seguridad y Pages comprobados.
- Global: **auditoría publicada y verde**; cualquier commit posterior debe correlacionarse de nuevo con sus ejecuciones antes de declararlo verde.
