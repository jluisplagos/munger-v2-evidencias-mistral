# Mapa de repositorios y ramas · 17-nov-2026

Para qué sirve cada rama tras la reorientación (`REORIENTACION_UNIVERSO.md`).

**Estados:**
- **EN USO:** se trabaja con ella.
- **CONSERVAR:** referencia que no se toca.
- **APARCADO:** se conserva sin trabajar en ella.
- **CERRADO:** trabajo terminado.
- **BORRABLE:** su contenido ya está en otra rama o en una etiqueta. Solo se borra con confirmación de la persona responsable y tras crear la etiqueta `archivo/<rama>`.

## `jluisplagos/munger-v2` (el producto: el personaje)

| Rama | Cabeza | Estado | Nota |
|---|---|---|---|
| `main` | d69d483 | CONSERVAR | Base histórica 4.14 |
| `integracion/candidata-cierre-v2` | b129b36 | **EN USO** | **El personaje actual:** 4.15 hito 2 con G-DOCS y G-RAIZ. Es la base de todo el trabajo |
| `auditoria/economica-f1-frente-e` | 9cad78d | **EN USO** | F1 (Elis): CSV verificado, decisiones, propuestas y scripts. Base de F1-IMPL |
| `claude/hopeful-bardeen-qap6y0` | 957af65 | BORRABLE | Hito 2; contenida en la candidata |
| `revision/4.15-hito1` | 059f4f6 | BORRABLE | Contenida en la candidata |
| `integracion/docs-operativos-957af65` | c0542b8 | BORRABLE con etiqueta | G-DOCS, ya integrado (por archivo) |
| `integracion/hechos-raiz-957af65` | e813fe6 | BORRABLE con etiqueta | G-RAIZ, ya integrado (por archivo) |
| `auditoria/economica-f1` | b91c68a | CERRADO | Primera rama de F1 |
| `auditoria/economica-f1-frente-e-revision` | 8fcc7fd | CERRADO | Revisiones independientes de F1 |
| `auditoria/revision-propuesta-f1` | 1a07188 | CERRADO | Revisión externa de la propuesta F1 |
| `preparacion/mistral-fuentes-vm` | 2a6242c | CERRADO | Preparación antigua |

## `jluisplagos/munger-v2-evidencias-mistral` (auxiliar: control, revisiones y fuentes)

| Rama | Estado | Nota |
|---|---|---|
| `coordinacion/cierre-v2` | **EN USO** | Control (CONTROL.json, ESTADO.md), reorientación, este mapa, revisiones y `universo/` (informe y su lectura) |
| `mistral/m2-cobertura-vm` (59b7f6b) | **EN USO** | Mistral A: verificación de contexto de las entradas. Le quedan los puntos de A4 que falten. Útil para todas las empresas |
| `revision/mistral-contraste-coordinador` | **EN USO** | Mistral R: contraste externo de las revisiones del coordinador |
| `fuentes/ahold-etapa1-20261117` | **EN USO** | Originales de la etapa 1 de Ahold aportados por la persona responsable |
| `coordinacion/release-fuentes-elis` | CONSERVAR | Rama de la Release `fuentes-elis-e-20261117`, con los 11 PDF de Elis |
| `revision/qwen-q1-v2` (4745f38) | CONSERVAR | Banco de 36 casos; de ahí salen los ~16 útiles como control |
| `mistral/e-fuentes-elis` (ea641e7) | APARCADO | Fuentes de Elis. CORRECCION_E3 es menor; solo se atiende si hace falta para el examen |
| `mistral/d-qwen-aceptacion` (7349840) | APARCADO | Arnés de los 36 casos. D4 sin revisar |
| `mistral/f-alcance-real` (c504830) | APARCADO | Casos fuera de muestra y contrato C |
| `mistral/g-manual-traspaso` (e61d66d) | APARCADO | Revisiones del manual y de G-RAIZ |
| `automatizacion/*` (4 ramas; PR #1 y #2 en borrador) | APARCADO | Automatización por API. No se usa |
| `coordinacion/release-fuentes-fineco`, `coordinacion/release-fuentes-hannover` | CERRADO | Sus Releases existen (`fuentes-fineco-u3-20261117`, `fuentes-hannover-u3-20261117`) |
| `mistral/m2-fundamento-pm1`, `mistral/m2-matematica-b` | CERRADO | Trabajo antiguo terminado |
| `mistral/fuentes-vm-01`, `preparacion/programa-mistral-m2`, `revision/chatgpt-*` (5 ramas de 16-nov) | BORRABLE | Contenidas en `coordinacion/cierre-v2` |
| `revision/chatgpt-reanudacion-20261117`, `preparacion/qwen-q1-aceptacion` | CERRADO | Revisión y preparación antiguas |

## Releases (fuentes conservadas con huella)

- `fuentes-elis-e-20261117`: 11 PDF de Elis.
- `fuentes-fineco-u3-20261117`: Fineco, candidato C descartado.
- `fuentes-hannover-u3-20261117`: Hannover Rück, prueba negativa de motor C.
- `fuentes-mistral-m2-20261116`: Release anterior del frente M2.

## Dentro de `coordinacion/cierre_v2/`, lo que importa ahora

- `REORIENTACION_UNIVERSO.md`: objetivo, reglas, examen, recorte y la pregunta de fondo sobre las fases A, B y C.
- `PROMPT_CONTINUIDAD_20261117.md`: el arranque de una ventana nueva.
- `universo/`: el informe crítico (PDF) y su lectura minuciosa.
- `CONTROL.json` y `ESTADO.md`: el registro de todo lo hecho.
- `revisiones_coordinador/`: todas las revisiones, como historial. No hace falta leerlas para continuar.
