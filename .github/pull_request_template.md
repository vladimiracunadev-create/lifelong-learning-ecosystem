## Propósito

Describe el problema observable y el resultado que cambia.

## Alcance y procedencia

- Datos canónicos o documentos afectados:
- Programas externos consultados (`owner/name`, fuente y versión):
- Estado de las correspondencias: candidata / verificada por unidad / no aplica.

## Verificación

- [ ] `python scripts/validate.py`
- [ ] `python -m unittest discover -s tests -v`
- [ ] `python scripts/build_portal.py --check`
- [ ] `node tests/check_portal_dom.cjs` si cambia el portal
- [ ] Navegación, enlaces y documentación afectados revisados
- [ ] `CHANGELOG.md`, `quality/STATUS.md` y `prompts/CONTINUITY.md` actualizados cuando corresponde

## Límites y continuidad

Indica qué no se comprobó, las brechas abiertas y la siguiente acción concreta.
