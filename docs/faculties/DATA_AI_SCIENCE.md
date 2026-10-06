# 🧠 Datos, inteligencia artificial y ciencia

[← Volver al campus](../CAMPUS.md) · [Ver todos los flujos nativos](../NATIVE_LEARNING_FLOWS.md)

Esta área reúne cinco repositorios con flujos diferentes: matemática secuencial, ciencia de datos aplicada, historia y técnicas de IA, entrenamiento experimental de redes y un laboratorio científico modular.

## 🧭 Mapa de elección

| Propósito | Repositorio | Flujo existente |
| --- | --- | --- |
| construir base matemática y reproducir resultados | [`computational-mathematics-program`](https://github.com/vladimiracunadev-create/computational-mathematics-program) | 360 clases, 18 partes y 5 etapas |
| programar, analizar, modelar y operar datos | [`python-data-science-program`](https://github.com/vladimiracunadev-create/python-data-science-program) | 232 clases, 9 partes, notebooks y apps |
| comprender la evolución completa de la IA | [`artificial-intelligence-evolution-program`](https://github.com/vladimiracunadev-create/artificial-intelligence-evolution-program) | 184 clases, 15 partes, papers y laboratorios |
| entrenar y evaluar redes neuronales | [`neural-network-training-labs`](https://github.com/vladimiracunadev-create/neural-network-training-labs) | 31 clases, 7 módulos y 93 notebooks |
| aplicar software a genómica reproducible | [`human-genome-labs`](https://github.com/vladimiracunadev-create/human-genome-labs) | módulos con madurez explícita, CLI, PWA y juego |

## 🧮 Matemática computacional

**Estado:** EXISTENTE. La fuente declara una progresión de cinco etapas: desde contar y representar hasta reproducir un paper.

- [Ruta de aprendizaje](https://github.com/vladimiracunadev-create/computational-mathematics-program/blob/main/docs/LEARNING_PATH.md)
- [Índice de 360 clases](https://github.com/vladimiracunadev-create/computational-mathematics-program/tree/main/classes)
- **Evidencia declarada:** demostraciones deterministas verificadas en CI y notebooks.
- **Límite:** no se ha comprobado cada notebook desde este maestro.

## 🐍 Python y ciencia de datos

**Estado:** EXISTENTE. El README completo declara 232 clases en nueve partes, laboratorio Python, notebooks y aplicaciones con las clases embebidas.

- [Índice de clases](https://github.com/vladimiracunadev-create/python-data-science-program/tree/main/classes)
- **Flujo:** Python y Polars → estadística y causalidad → ML/DL → MLOps, ética y capstones, según la estructura publicada.
- **Práctica:** notebooks y laboratorio local.
- **Límite:** el maestro no ejecutó los notebooks, instaladores ni apps.

## 🤖 Evolución de la inteligencia artificial

**Estado:** EXISTENTE. La fuente declara que las 15 partes siguen la evolución histórica y que lo enseñado en una etapa prepara la siguiente.

- [Ruta principal](https://github.com/vladimiracunadev-create/artificial-intelligence-evolution-program/blob/main/docs/LEARNING_PATH.md)
- [Portal de estudio](https://vladimiracunadev-create.github.io/artificial-intelligence-evolution-program/)
- **Flujos paralelos:** clases, ruta de papers, notebooks y motores didácticos.
- **Vínculos explícitos:** matemática, datos, redes neuronales, LangGraph, cloud, seguridad, sistemas, blockchain y genómica aparecen enlazados por su README.
- **Límite:** esos enlaces no son automáticamente prerrequisitos.

## 🧠 Entrenamiento de redes neuronales

**Estado:** EXISTENTE. La fuente permite dos usos: estudiar de la clase 01 a la 31 o abrir una clase aislada y atender sus prerrequisitos declarados.

- [Programa de clases](https://github.com/vladimiracunadev-create/neural-network-training-labs/blob/main/docs/learning-path.md)
- [Siete módulos](https://github.com/vladimiracunadev-create/neural-network-training-labs/tree/main/parts)
- **Práctica:** 93 notebooks con datos públicos reales declarados.
- **Vínculos explícitos:** evolución de IA, Python y datos, y LangGraph.

## 🧬 Human Genome Labs

**Estado:** EXISTENTE. La fuente presenta un núcleo científico TypeScript, formatos FASTA/GFF3/VCF, CLI, PWA y juego.

- [Sistema de módulos](https://github.com/vladimiracunadev-create/human-genome-labs/blob/main/docs/MODULE_SYSTEM.md)
- **Flujo correcto:** escoger un módulo según su madurez y evidencia publicada.
- **Límite:** no se infiere una carrera de genómica ni una secuencia educativa completa.

## 🔗 Relación con evidencia

El README de IA enlaza explícitamente matemática, datos y redes neuronales; el de redes neuronales enlaza IA y datos. Esa evidencia permite mostrar un **conjunto conectado**. Definir “matemática → datos → IA → redes” como una malla obligatoria todavía requeriría comparar unidades y niveles de entrada.
