# Auditoría de evidencia de publicación · 2026-10-05

## Identidad

- Repositorio previsto: `vladimiracunadev-create/lifelong-learning-ecosystem`.
- Rama objetivo: `main`.
- Producto: superrepositorio federado y portal autocontenido, versión 0.1.0.
- Entorno local fresco: Windows, Python 3.12.9 y Node 24.11.1.

El commit y los enlaces de ejecución remota se completan después de la primera publicación. Un workflow configurado aún no constituye evidencia remota verde.

## Matriz de afirmaciones

| Plataforma/artefacto | Afirmación | Fuente canónica | Nivel de evidencia | Resultado | Referencia |
| --- | --- | --- | --- | --- | --- |
| Datos | Los registros y referencias son coherentes | JSON y `scripts/validate.py` | Ejecución local fresca | Correcto | `quality/validation.json` |
| Python | La suite protege contrato, rutas, privacidad y exportación | `tests/` | Ejecución local fresca | 39/39 correctas | `python -m unittest discover -s tests -v` |
| Portal | El derivado coincide con sus fuentes | `portal/template.html`, datos y docs | Ejecución local fresca | Vigente | `python scripts/build_portal.py --check` |
| Portal | Secciones, detalles, filtros y escape funcionan en DOM controlado | `tests/check_portal_dom.cjs` | Ejecución local fresca | Correcto | 7 secciones, 68 detalles |
| GitHub Actions | Los workflows tienen sintaxis y referencias válidas | `.github/workflows/` | Inspección estática; comprobación remota pendiente | No comprobado todavía | `actionlint` local fue bloqueado antes de ejecutarse |
| Portal público | Pages sirve el commit final | Workflow `Portal público` | No comprobada | Pendiente de primera ejecución | URL prevista en `docs/AUTOMATION.md` |

## Gates ejecutados

| Comando | Entorno | Resultado | Duración | Evidencia |
| --- | --- | --- | --- | --- |
| `python scripts/validate.py --json` | Windows · Python 3.12.9 | Correcto | < 10 s | 6 JSON, 14 programas, 36 competencias, 5 mallas |
| `python -m unittest discover -s tests -v` | Windows · Python 3.12.9 | Correcto | 3.36 s | 39 pruebas |
| `python scripts/build_portal.py --check` | Windows · Python 3.12.9 | Correcto | < 10 s | 85 documentos embebidos; 680.288 bytes |
| `node tests/check_portal_dom.cjs` | Windows · Node 24.11.1 | Correcto | < 10 s | 7 secciones, 68 detalles y 85 documentos |

## Artefactos inspeccionados

| Artefacto | Procedencia/commit | Versión | Propiedades verificadas | Resultado |
| --- | --- | --- | --- | --- |
| `index.html` | Árbol local previo al commit público | 0.1.0 | Autocontenido, determinístico y sin fetch de datos | Correcto; 680.288 bytes |
| ZIP local preliminar | Árbol local previo al commit público | 0.1.0 | Manifiesto SHA-256 e integridad de copia extraída | Correcto; el artefacto del commit final lo construirá CI |

## Resultados remotos

Pendientes. La carpeta recibida no tenía metadatos Git ni repositorio remoto configurado, y la sesión local de GitHub CLI no estaba autenticada.

## Incidencias

| Severidad | Hallazgo | Impacto | Evidencia | Acción siguiente |
| --- | --- | --- | --- | --- |
| Alta | No existe aún ejecución remota ligada al commit final | `main` todavía no puede declararse verde | Ausencia de `.git` y sesión CLI no autenticada al iniciar | Inicializar, publicar y esperar resultados finales |
| Media | La revisión visual en navegador real no está disponible en este entorno | La apariencia no tiene evidencia visual fresca | El navegador automatizable no admite archivos locales | Revisar el portal público después de Pages |
| Media | `actionlint` no pudo ejecutarse localmente | La sintaxis específica de Actions depende de la primera validación remota | Windows bloqueó el proceso descargado antes de iniciarlo | Observar y corregir la primera ejecución de GitHub Actions |

## No comprobado y riesgo residual

- Estado final de CI, CodeQL y Pages para el commit publicado.
- Ruleset o protección de rama, que GitHub permite completar después de crear la rama y sus checks.
- Enlaces externos vivos y revisión pedagógica especializada.

## Veredicto

- Portal y datos locales: evidencia local suficiente para continuar hacia la publicación.
- Publicación remota: no declarar completada hasta correlacionar commit, ejecuciones y URL pública.
- Global: **no preparar una afirmación de `main` verde todavía**; falta evidencia remota del commit final.
