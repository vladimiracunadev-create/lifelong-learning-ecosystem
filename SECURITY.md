# Política de seguridad

## Alcance

Este repositorio distribuye datos curriculares públicos, documentación y un lector HTML autocontenido. No opera cuentas, no recibe evidencias personales y no necesita secretos para funcionar. Los programas enlazados conservan sus propias políticas y ciclos de mantenimiento.

La rama `main` se comprueba con validación de datos, pruebas, reconstrucción determinística del portal y análisis CodeQL para Python y JavaScript. Las acciones externas de los workflows están fijadas a commits completos.

## Informar una vulnerabilidad

No publiques credenciales, datos personales ni una demostración explotable en una incidencia pública. Utiliza la opción **Report a vulnerability** de la pestaña Security del repositorio para describir:

- componente y versión o commit afectados;
- impacto observado y condiciones necesarias;
- pasos mínimos para reproducirlo;
- mitigación conocida, si existe.

Si el problema pertenece a uno de los programas federados, repórtalo en el repositorio de origen. Una referencia desde este catálogo no traslada la responsabilidad operativa al superrepositorio.

## Versiones atendidas

| Versión | Estado |
| --- | --- |
| Rama `main` | Atendida |
| Entregas anteriores | Mejor esfuerzo |

Las correcciones se documentan en `CHANGELOG.md`. Ningún archivo del repositorio debe contener historiales de aprendizaje reales, tokens, claves, perfiles privados o exportaciones personales.
