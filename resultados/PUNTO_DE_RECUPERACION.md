# Punto de recuperación · frente M · rama mistral/fuentes-vm-01

Evidencia propuesta por Mistral; pendiente de revisión e incorporación por el integrador.

## Estado actual

- Repositorio auxiliar: `jluisplagos/munger-v2-evidencias-mistral` (origin verificado: `https://github.com/jluisplagos/munger-v2-evidencias-mistral.git`). Rama local: `mistral/fuentes-vm-01`. Base: `main` @ `e137b854dc592bcad9ed3e51275f7b80d35d210e`.
- Insumos: `preparar_insumos.py --download` ejecutado; ZIP base-4.14 (1.130.912.246 bytes, sha256 `bb51942c…b7b93e` verificado) y 15 insumos en `.trabajo/insumos/` con sha256 conformes. Selección parcial (`producto_completo_verificado: false`).
- Asociaciones texto↔PDF verificadas (pypdf, 100% tokens numéricos por página) y verificación visual con PyMuPDF en EN2025 p.52 y ES2025 p.14.

## Terminado

- Bloque 1 (10 objetivos iniciales + 6 dependencias): primera lectura en `resultados/lectura_fuentes.jsonl` antes del contraste; hash `5571ee7f9a5b021da59f99d6ac61f9feb3a4723af92a240556f3e1ef20c90f51`. Commit local `5641bec`.
- Bloque 2 (44 observaciones restantes; total 60 = 26 objetivos + 34 dependencias): hash bloque 2 `8a7a518f7734a015ddc255fccfd0522a5ec33ddcc828640c3a44ddc561429c2c`; hash fichero completo `5905e415e71422fc4d5cf04e32a0b0fc4136210df7d0bfac9b52220547f3d8dc`. Commit local `b278727`.
- XLSX de ambos expedientes leídos en solo lectura (openpyxl; huellas `82ff7fb8…` Vidrala, `95a78291…` Viscofan): celdas objetivo hardcodeadas; Vidrala C48 vacío (None).
- Contraste: `resultados/contraste_objetivos.csv` con 26 filas — 23 `COINCIDE_EN_REVISION_MISTRAL`, 3 `HIPOTESIS_O_AUSENCIA` (Vidrala C48/C49/C50), 0 DIFERENCIA, 0 NO_ACREDITADO. Derivados recalculados desde fuentes verificadas (detalle en HALLAZGOS.md punto 9).
- Entregables completos: `lectura_fuentes.jsonl`, `contraste_objetivos.csv`, `HALLAZGOS.md`, `RESUMEN_PARA_CLAUDE.md`, este archivo, `MANIFIESTO_SHA256.txt`. `comprobar_entrega.py` ejecutado (resultado abajo).

## Pendiente / siguiente acción exacta

1. **Bloqueo de push remoto**: `git push origin mistral/fuentes-vm-01` → `403 Permission to jluisplagos/munger-v2-evidencias-mistral.git denied to jluisplagos` (también 403 vía `github_app_create_branch` «Resource not accessible by integration»; las mutaciones `gh` API y `github_app_push_files` están bloqueadas por el sandbox). Acción requerida de la persona responsable: autorizar la GitHub App (mistralai) con **Contents: write** sobre `jluisplagos/munger-v2-evidencias-mistral` (https://github.com/apps/mistralai/installations/new) y reintentar el push de la rama local (commits `5641bec`, `b278727` y el de entrega).
2. Tras el push: verificar el commit remoto y entregar el enlace al commit final.
3. Revisión externa (integrador/Claude) de citas, datos, derivaciones y compatibilidad antes de incorporar cualquier parte.

## Modelo y limitaciones

- Sesión: Vibe Code de Mistral AI, modelo `mistral-large-4-0` (único modelo expuesto; sin nivel de esfuerzo porque la interfaz no lo ofrece). Herramientas deterministas: Python stdlib + pypdf 7.1.0 + openpyxl 3.1.5 + PyMuPDF (pip en el sandbox) para huellas, extracción, verificación visual y aritmética.
- Consumo/facturación: no visible desde la sesión; se declara que no se está limitando. El presupuesto recomendado (25 EUR) está configurado externamente.
- Red: disponible para GitHub (descarga de release verificada con urllib; `curl` bloqueado por el sandbox). Sin LibreOffice ni pipeline (prohibidos). PDF/XLSX/ZIP fuera de Git (`.trabajo/` en `.git/info/exclude`).
- No se abrió PR, no hay fusión, no se modificó `munger-v2` ni ramas/PR/issues del original.
