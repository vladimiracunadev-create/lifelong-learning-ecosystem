# Automatización y publicación

La automatización protege tres propiedades distintas: coherencia del contenido, seguridad estática y disponibilidad del portal. Ningún workflow se presenta como evidencia de eficacia pedagógica.

## Workflows

| Workflow | Disparadores | Gates principales | Resultado |
| --- | --- | --- | --- |
| `Calidad` | cambios en `main`, pull requests y ejecución manual | Python 3.11 y 3.14 en Linux, Python 3.12 en Windows, 41 pruebas, validador, portal vigente, DOM controlado con Node 24 | Gate requerido para integrar y paquete ZIP temporal |
| `Seguridad` | cambios en `main`, pull requests, semanal y manual | CodeQL para Python y JavaScript | Alertas de análisis estático en GitHub Security |
| `Portal público` | final exitoso de `Calidad` en `main` y ejecución manual | revalida datos y vigencia antes de desplegar | `index.html` publicado mediante GitHub Pages |

Los workflows usan `permissions` mínimos, `timeout-minutes`, concurrencia controlada y acciones fijadas a SHAs completos. Dependabot revisa semanalmente las versiones de GitHub Actions; cada actualización debe conservar el pin por commit y su comentario de versión.

## Gate recomendado para `main`

Configura una regla de rama o ruleset con estas condiciones:

1. exigir pull request y al menos una revisión para cambios futuros;
2. exigir que pasen todos los jobs de `Calidad` y `Seguridad`;
3. exigir que la rama esté actualizada antes de integrar;
4. bloquear force-push y eliminación de `main`;
5. permitir administración excepcional solo con registro de la razón.

La primera publicación puede necesitar crear `main` antes de que GitHub permita seleccionar checks requeridos. Aplica el ruleset después de la primera ejecución verde.

## Publicación de Pages

El workflow despliega exclusivamente el `index.html` generado y un marcador `.nojekyll`. Los JSON, scripts, historiales locales y carpetas privadas no forman parte del sitio publicado. El lector sigue siendo autocontenido y no realiza peticiones de red en segundo plano.

La URL esperada es:

`https://vladimiracunadev-create.github.io/lifelong-learning-ecosystem/`

## Evidencia y límites

Una ejecución verde demuestra coherencia estructural, pruebas automatizadas, vigencia del derivado y ausencia de alertas CodeQL detectadas para ese commit. La revisión visual en navegadores, los enlaces externos vivos, la calidad especializada y la eficacia educativa requieren comprobaciones separadas.
