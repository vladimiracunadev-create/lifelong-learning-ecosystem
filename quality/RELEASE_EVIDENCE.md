# Auditoría de evidencia de publicación · 2026-10-05

## Identidad

- Repositorio público: `vladimiracunadev-create/lifelong-learning-ecosystem`.
- Rama objetivo: `main`.
- Producto: superrepositorio federado y portal autocontenido, versión 0.1.0.
- Entorno local fresco: Windows, Python 3.12.9 y Node 24.11.1.

El primer commit publicado fue `dea81af5b0ec4740afb9ed787e73676f3cdefd79`. Su ejecución de Calidad detectó una huella del portal dependiente de CRLF/LF en Windows; la corrección normaliza las fuentes y añade una prueba de regresión. La evidencia verde corresponde únicamente a la ejecución final de la corrección.

## Matriz de afirmaciones

| Plataforma/artefacto | Afirmación | Fuente canónica | Nivel de evidencia | Resultado | Referencia |
| --- | --- | --- | --- | --- | --- |
| Datos | Los registros y referencias son coherentes | JSON y `scripts/validate.py` | Ejecución local fresca | Correcto | `quality/validation.json` |
| Python | La suite protege contrato, rutas, privacidad, exportación y huellas entre plataformas | `tests/` | Ejecución local fresca | 40/40 correctas | `python -m unittest discover -s tests -v` |
| Portal | El derivado coincide con sus fuentes | `portal/template.html`, datos y docs | Ejecución local fresca | Vigente | `python scripts/build_portal.py --check` |
| Portal | Secciones, detalles, filtros y escape funcionan en DOM controlado | `tests/check_portal_dom.cjs` | Ejecución local fresca | Correcto | 7 secciones, 68 detalles |
| GitHub Actions | Los workflows tienen sintaxis y referencias válidas | `.github/workflows/` | Resultado remoto comprobado | GitHub aceptó y ejecutó los tres workflows | Enlaces de ejecución en la sección remota |
| Portal público | Pages sirve el commit final | Workflow `Portal público` | No comprobada | Pendiente de primera ejecución | URL prevista en `docs/AUTOMATION.md` |

## Gates ejecutados

| Comando | Entorno | Resultado | Duración | Evidencia |
| --- | --- | --- | --- | --- |
| `python scripts/validate.py --json` | Windows · Python 3.12.9 | Correcto | < 10 s | 6 JSON, 14 programas, 36 competencias, 5 mallas |
| `python -m unittest discover -s tests -v` | Windows · Python 3.12.9 | Correcto | < 10 s | 40 pruebas |
| `python scripts/build_portal.py --check` | Windows · Python 3.12.9 | Correcto | < 10 s | 85 documentos embebidos; 680.288 bytes |
| `node tests/check_portal_dom.cjs` | Windows · Node 24.11.1 | Correcto | < 10 s | 7 secciones, 68 detalles y 85 documentos |

## Artefactos inspeccionados

| Artefacto | Procedencia/commit | Versión | Propiedades verificadas | Resultado |
| --- | --- | --- | --- | --- |
| `index.html` | Árbol local previo al commit público | 0.1.0 | Autocontenido, determinístico y sin fetch de datos | Correcto; 680.288 bytes |
| ZIP local preliminar | Árbol local previo al commit público | 0.1.0 | Manifiesto SHA-256 e integridad de copia extraída | Correcto; el artefacto del commit final lo construirá CI |

## Resultados remotos

- [Calidad del primer commit](https://github.com/vladimiracunadev-create/lifelong-learning-ecosystem/actions/runs/37403748247): fallo en Windows por huella de saltos de línea; evidencia negativa utilizada para la corrección.
- [Seguridad del primer commit](https://github.com/vladimiracunadev-create/lifelong-learning-ecosystem/actions/runs/37403748254): ejecución iniciada para Python y JavaScript.
- [Pages posterior al primer gate](https://github.com/vladimiracunadev-create/lifelong-learning-ecosystem/actions/runs/37403793396): omitido correctamente porque Calidad no terminó verde.

## Incidencias

| Severidad | Hallazgo | Impacto | Evidencia | Acción siguiente |
| --- | --- | --- | --- | --- |
| Alta | La primera ejecución detectó una huella distinta en Windows | El portal válido en Linux se consideraba desactualizado en Windows | La huella usaba bytes CRLF/LF sin normalizar | Normalizar fuentes de texto y cubrir ambos finales de línea con una prueba |
| Media | La revisión visual en navegador real no está disponible en este entorno | La apariencia no tiene evidencia visual fresca | El navegador automatizable no admite archivos locales | Revisar el portal público después de Pages |
| Media | `actionlint` no pudo ejecutarse localmente | La sintaxis específica de Actions depende de la primera validación remota | Windows bloqueó el proceso descargado antes de iniciarlo | Observar y corregir la primera ejecución de GitHub Actions |

## No comprobado y riesgo residual

- Estado final de CI, CodeQL y Pages para el commit con la corrección multiplataforma.
- Ruleset o protección de rama, que GitHub permite completar después de crear la rama y sus checks.
- Enlaces externos vivos y revisión pedagógica especializada.

## Veredicto

- Portal y datos locales: evidencia local suficiente para continuar hacia la publicación.
- Publicación remota: el repositorio es público; no declarar `main` verde hasta correlacionar la corrección, sus ejecuciones y la URL de Pages.
- Global: **no preparar una afirmación de `main` verde todavía**; falta evidencia remota del commit final.
