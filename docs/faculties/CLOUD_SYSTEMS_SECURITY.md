# ☁️ Cloud, sistemas y seguridad

[← Volver al campus](../CAMPUS.md) · [Ver todos los flujos nativos](../NATIVE_LEARNING_FLOWS.md)

Esta área mezcla programas extensos y laboratorios acotados. La infraestructura disponible cambia lo que se puede ejecutar; por eso cada ficha distingue contenido, entorno y evidencia.

## 🧭 Mapa de elección

| Propósito | Repositorio | Flujo existente |
| --- | --- | --- |
| formarse en ingeniería multicloud | [`multi-cloud-engineering-program`](https://github.com/vladimiracunadev-create/multi-cloud-engineering-program) | 288 clases, 24 partes, 288 labs y rutas profesionales |
| recorrer ciberseguridad paso a paso | [`modern-cybersecurity-program`](https://github.com/vladimiracunadev-create/modern-cybersecurity-program) | 360 clases, 20 partes, rutas y laboratorios |
| dominar virtualización Linux | [`qemu-kvm-labs`](https://github.com/vladimiracunadev-create/qemu-kvm-labs) | 12 labs progresivos y proyecto final |
| practicar contenedores por stack | [`docker-labs`](https://github.com/vladimiracunadev-create/docker-labs) | colección de laboratorios Docker/Compose |
| aprender AWS por proyectos | [`proyectos-aws`](https://github.com/vladimiracunadev-create/proyectos-aws) | casos en evolución |
| experimentar con aislamiento | [`sandbox-labs`](https://github.com/vladimiracunadev-create/sandbox-labs) | 36 casos experimentales |
| comprender flujos de pagos | [`universal-payments-engineering-lab`](https://github.com/vladimiracunadev-create/universal-payments-engineering-lab) | empieza aquí, ruta y demo local |

## 🌩️ Ingeniería multicloud

**Estado:** EXISTENTE. La fuente declara 288 clases, 24 partes, 1.288 horas, 288 laboratorios, capstones y rutas profesionales.

- [Índice de clases](https://github.com/vladimiracunadev-create/multi-cloud-engineering-program/tree/main/classes)
- [Rutas profesionales](https://github.com/vladimiracunadev-create/multi-cloud-engineering-program/tree/main/learning-paths)
- [Laboratorios](https://github.com/vladimiracunadev-create/multi-cloud-engineering-program/tree/main/labs)
- **Vínculos explícitos del README:** ciberseguridad, IA, datos, blockchain y programación políglota.

## 🛡️ Ciberseguridad moderna

**Estado:** EXISTENTE. Programa modular y secuencial de 360 clases en 20 partes.

- [Índice de clases](https://github.com/vladimiracunadev-create/modern-cybersecurity-program/tree/main/classes)
- [Rutas por rol](https://github.com/vladimiracunadev-create/modern-cybersecurity-program/tree/main/rutas)
- [Plataformas de práctica](https://github.com/vladimiracunadev-create/modern-cybersecurity-program/blob/main/docs/PLATAFORMAS-DE-PRACTICA.md)
- **Condición:** los laboratorios ofensivos requieren sistemas propios, CTF o autorización explícita, según la fuente.

## 🧰 Virtualización con QEMU/KVM

**Estado:** EXISTENTE. Doce laboratorios progresivos culminan en `vm-manager`.

- [Ruta de aprendizaje](https://github.com/vladimiracunadev-create/qemu-kvm-labs#ruta-de-aprendizaje)
- [Guía de laboratorios](https://github.com/vladimiracunadev-create/qemu-kvm-labs/blob/main/docs/LAB_GUIDE.md)
- **Prerrequisitos de entorno:** Python 3.11+, Linux y, para la ruta completa, virtualización, `/dev/kvm`, QEMU, libvirt y herramientas relacionadas.
- **Degradación:** la fuente ofrece una ruta según las capacidades del host y registra los límites.

## 🐳 Docker y proyectos AWS

[`docker-labs`](https://github.com/vladimiracunadev-create/docker-labs) está **EXISTENTE** como colección de laboratorios personales en varios stacks. [`proyectos-aws`](https://github.com/vladimiracunadev-create/proyectos-aws) está **EN DESARROLLO** y organiza aprendizaje caso a caso. La revisión no encontró una secuencia completa común; se navegan por laboratorio o proyecto.

## 🧪 Aislamiento experimental

[`sandbox-labs`](https://github.com/vladimiracunadev-create/sandbox-labs) se declara **EXPERIMENTAL** y educativo. Sus 36 casos se dividen entre sandboxes técnicos y mercado de capitales con dinero simulado. No se presenta como producto de seguridad.

## 💳 Ingeniería de pagos

**Estado:** EXISTENTE. La ruta hace visibles orden, estados, ledger, resultado desconocido, liquidación, fallos y conciliación sin credenciales ni dinero.

- [Empieza aquí](https://github.com/vladimiracunadev-create/universal-payments-engineering-lab/blob/main/docs/START_HERE.md)
- [Ruta de aprendizaje](https://github.com/vladimiracunadev-create/universal-payments-engineering-lab/blob/main/docs/LEARNING_PATH.md)
- **Práctica:** demo local y preguntas con criterios verificables.

## 🔗 Conexiones pendientes

Cloud, ciberseguridad, contenedores y virtualización se enlazan temáticamente y algunos README los conectan explícitamente. Aun así, una malla federada debe declarar el entorno mínimo y verificar qué laboratorio prepara realmente al siguiente.
