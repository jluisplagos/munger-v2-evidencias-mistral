# Punto de recuperación · Frente A M2 · rama `mistral/m2-cobertura-vm`

Propuesta de evidencia de Mistral; pendiente de revisión e incorporación por el integrador. No APROBADO ni aptitud financiera general.

## Estado actual

- Repositorio auxiliar: `jluisplagos/munger-v2-evidencias-mistral`, origin verificado (`https://github.com/jluisplagos/munger-v2-evidencias-mistral`). Rama `mistral/m2-cobertura-vm` traída de origin y publicada; **no** se trabaja sobre `main` ni sobre `jluisplagos/munger-v2`.
- Escritura exclusively en `resultados_m2/cobertura_vm/`. No se tocan frentes B/C, ni el producto, ni `resultados/` del piloto M1.
- Insumos: `python3 docs/programa_mistral_m2/herramientas/preparar_insumos.py --download` ejecutado; ZIP base-4.14 (1.130.912.246 bytes, sha256 `bb51942c…b7b93e` verificado por la herramienta) y **251 archivos conformes** con huella verificada en `.trabajo/insumos_m2/` (29 PDF candidatos). Selección parcial: `producto_completo_verificado: false`.
- Inventario generado (`scripts/inventario.py` → `INVENTARIO.md`, `resultados/inventario.json`): 677 entradas (Vidrala 347, Viscofan 330), 60 del piloto, 617 nuevas; clases 454 dato_publicado / 13 cero_comprobado / 101 derivado / 6 dato_ausente / 52 hipótesis / 35 convención / 16 no aplicable; concilia con `entrada/configuracion.json` y `entrada/catalogo_entradas.csv`. 21 fuentes referenciadas, todas CONFORME (huella sha256 verificada). Grafo de derivados: 101 nodos, **0 huecos, 0 ciclos**. 22 lotes definidos (L00 piloto de 60; L01–L21 de ≤30 entradas nuevas, agrupadas por documento/página).

## Hecho en este punto

- `scripts/`: `comun.py`, `inventario.py`, `verificar_fuentes.py`, `derivaciones.py`, `construir_cobertura.py`, `revisar_lote.py`, `control_cobertura.py`, `asociacion_pdf.py` (cálculos con `Decimal`, solo lectura sobre insumos).
- Verificación mecánica ejecutada (`verificar_fuentes.py`): 467 entradas con fuente → **467 COINCIDE_PROPUESTO** (archivo conforme + página `[PDF PAGE n]` localizada + cita localizada + valor localizado + transformación `valor_fuente × escala × signo = valor_modelo` + comparación con el libro XLSX en solo lectura / registro oficial para aux). 123 observaciones por página en `OBSERVACIONES.jsonl`.
- Derivados (`derivaciones.py` → `DERIVADOS.json`): 101 nodos (14 reutilizados del piloto, 87 nuevos), recalculados con `Decimal` → **101 COINCIDE_PROPUESTO** (71 exactos, 30 dentro del redondeo a 3 decimales del libro).
- `COBERTURA_677.csv`: 677 filas; estados: 568 COINCIDE_PROPUESTO, 52 HIPOTESIS, 35 CONVENCION, 16 NO_APLICABLE, 6 DATO_AUSENTE; 60 filas con `origen_revision=M1_REUTILIZADA`.
- Control (`control_cobertura.py` → `resultados/control_cobertura.json`): **PASS, 0 violaciones** (sin filas duplicadas/faltantes, sin fuentes inexistentes presentadas como examinadas, sin operandos incoherentes, sin reutilización tras cambio sin recalcular; recuentos conciliados con 677/60/617/101/14/87).

## Lotes publicados

- `L00`: 60 entradas (PILOTO_M1_REUTILIZADA); estados COINCIDE_PROPUESTO=57, DATO_AUSENTE=1, HIPOTESIS=2; archivo `resultados/lotes/lote_L00.json`
- `L01`: 30 entradas (NUEVO); estados COINCIDE_PROPUESTO=6, CONVENCION=12, HIPOTESIS=9, NO_APLICABLE=3; archivo `resultados/lotes/lote_L01.json`
- `L02`: 30 entradas (NUEVO); estados COINCIDE_PROPUESTO=27, CONVENCION=1, NO_APLICABLE=2; archivo `resultados/lotes/lote_L02.json`
- `L03`: 30 entradas (NUEVO); estados COINCIDE_PROPUESTO=17, CONVENCION=4, HIPOTESIS=9; archivo `resultados/lotes/lote_L03.json`
- `L04`: 30 entradas (NUEVO); estados COINCIDE_PROPUESTO=23, HIPOTESIS=7; archivo `resultados/lotes/lote_L04.json`
- `L05`: 30 entradas (NUEVO); estados COINCIDE_PROPUESTO=30; archivo `resultados/lotes/lote_L05.json`
- `L06`: 30 entradas (NUEVO); estados COINCIDE_PROPUESTO=30; archivo `resultados/lotes/lote_L06.json`
- `L07`: 30 entradas (NUEVO); estados COINCIDE_PROPUESTO=30; archivo `resultados/lotes/lote_L07.json`
- `L08`: 30 entradas (NUEVO); estados COINCIDE_PROPUESTO=30; archivo `resultados/lotes/lote_L08.json`
- `L09`: 30 entradas (NUEVO); estados COINCIDE_PROPUESTO=30; archivo `resultados/lotes/lote_L09.json`
- `L10`: 30 entradas (NUEVO); estados COINCIDE_PROPUESTO=29, DATO_AUSENTE=1; archivo `resultados/lotes/lote_L10.json`
- `L11`: 30 entradas (NUEVO); estados COINCIDE_PROPUESTO=20, CONVENCION=5, DATO_AUSENTE=2, HIPOTESIS=3; archivo `resultados/lotes/lote_L11.json`
- `L12`: 30 entradas (NUEVO); estados COINCIDE_PROPUESTO=4, CONVENCION=11, HIPOTESIS=5, NO_APLICABLE=10; archivo `resultados/lotes/lote_L12.json`
- `L13`: 30 entradas (NUEVO); estados COINCIDE_PROPUESTO=27, DATO_AUSENTE=2, NO_APLICABLE=1; archivo `resultados/lotes/lote_L13.json`
- `L14`: 30 entradas (NUEVO); estados COINCIDE_PROPUESTO=11, CONVENCION=2, HIPOTESIS=17; archivo `resultados/lotes/lote_L14.json`
- `L15`: 30 entradas (NUEVO); estados COINCIDE_PROPUESTO=30; archivo `resultados/lotes/lote_L15.json`
- `L16`: 30 entradas (NUEVO); estados COINCIDE_PROPUESTO=30; archivo `resultados/lotes/lote_L16.json`
- `L17`: 30 entradas (NUEVO); estados COINCIDE_PROPUESTO=30; archivo `resultados/lotes/lote_L17.json`
- `L18`: 30 entradas (NUEVO); estados COINCIDE_PROPUESTO=30; archivo `resultados/lotes/lote_L18.json`
- `L19`: 30 entradas (NUEVO); estados COINCIDE_PROPUESTO=30; archivo `resultados/lotes/lote_L19.json`
- `L20`: 30 entradas (NUEVO); estados COINCIDE_PROPUESTO=30; archivo `resultados/lotes/lote_L20.json`
- `L21`: 17 entradas (NUEVO); estados COINCIDE_PROPUESTO=17; archivo `resultados/lotes/lote_L21.json`

## Lotes publicados (revision externa A / correccion de contexto)

- `L00` (revision A): 60 entradas; mecanico [COINCIDE_PROPUESTO=57, DATO_AUSENTE=1, HIPOTESIS=2]; contextual [REUTILIZADO_M1=60]; `resultados/lotes/lote_L00.json`
- `L01` (revision A): 30 entradas; mecanico [COINCIDE_PROPUESTO=6, CONVENCION=12, HIPOTESIS=9, NO_APLICABLE=3]; contextual [NO_APLICA=24, REVISADO_CONTEXTUAL=6]; `resultados/lotes/lote_L01.json`
- `L02` (revision A): 30 entradas; mecanico [COINCIDE_PROPUESTO=27, CONVENCION=1, NO_APLICABLE=2]; contextual [NO_APLICA=3, PENDIENTE_CONTEXTUAL=1, REVISADO_CONTEXTUAL=26]; `resultados/lotes/lote_L02.json`
- `L03` (revision A): 30 entradas; mecanico [COINCIDE_PROPUESTO=17, CONVENCION=4, HIPOTESIS=9]; contextual [NO_APLICA=13, REVISADO_CONTEXTUAL=17]; `resultados/lotes/lote_L03.json`
- `L04` (revision A): 30 entradas; mecanico [COINCIDE_PROPUESTO=23, HIPOTESIS=7]; contextual [NO_APLICA=7, REVISADO_CONTEXTUAL=23]; `resultados/lotes/lote_L04.json`
- `L05` (revision A): 30 entradas; mecanico [COINCIDE_PROPUESTO=30]; contextual [REVISADO_CONTEXTUAL=30]; `resultados/lotes/lote_L05.json`
- `L06` (revision A): 30 entradas; mecanico [COINCIDE_PROPUESTO=30]; contextual [PENDIENTE_CONTEXTUAL=1, REVISADO_CONTEXTUAL=29]; `resultados/lotes/lote_L06.json`
- `L07` (revision A): 30 entradas; mecanico [COINCIDE_PROPUESTO=30]; contextual [REVISADO_CONTEXTUAL=30]; `resultados/lotes/lote_L07.json`
- `L08` (revision A): 30 entradas; mecanico [COINCIDE_PROPUESTO=30]; contextual [REVISADO_CONTEXTUAL=30]; `resultados/lotes/lote_L08.json`
- `L09` (revision A): 30 entradas; mecanico [COINCIDE_PROPUESTO=30]; contextual [REVISADO_CONTEXTUAL=30]; `resultados/lotes/lote_L09.json`
- `L10` (revision A): 30 entradas; mecanico [COINCIDE_PROPUESTO=29, DATO_AUSENTE=1]; contextual [NO_APLICA=1, REVISADO_CONTEXTUAL=29]; `resultados/lotes/lote_L10.json`
- `L11` (revision A): 30 entradas; mecanico [COINCIDE_PROPUESTO=20, CONVENCION=5, DATO_AUSENTE=2, HIPOTESIS=3]; contextual [NO_APLICA=10, REVISADO_CONTEXTUAL=20]; `resultados/lotes/lote_L11.json`
- `L12` (revision A): 30 entradas; mecanico [COINCIDE_PROPUESTO=4, CONVENCION=11, HIPOTESIS=5, NO_APLICABLE=10]; contextual [NO_APLICA=26, REVISADO_CONTEXTUAL=4]; `resultados/lotes/lote_L12.json`
- `L13` (revision A): 30 entradas; mecanico [COINCIDE_PROPUESTO=27, DATO_AUSENTE=2, NO_APLICABLE=1]; contextual [NO_APLICA=3, REVISADO_CONTEXTUAL=27]; `resultados/lotes/lote_L13.json`
- `L14` (revision A): 30 entradas; mecanico [COINCIDE_PROPUESTO=11, CONVENCION=2, HIPOTESIS=17]; contextual [NO_APLICA=19, REVISADO_CONTEXTUAL=11]; `resultados/lotes/lote_L14.json`
- `L15` (revision A): 30 entradas; mecanico [COINCIDE_PROPUESTO=30]; contextual [REVISADO_CONTEXTUAL=30]; `resultados/lotes/lote_L15.json`
- `L16` (revision A): 30 entradas; mecanico [COINCIDE_PROPUESTO=30]; contextual [REVISADO_CONTEXTUAL=30]; `resultados/lotes/lote_L16.json`
- `L17` (revision A): 30 entradas; mecanico [COINCIDE_PROPUESTO=30]; contextual [REVISADO_CONTEXTUAL=30]; `resultados/lotes/lote_L17.json`
- `L18` (revision A): 30 entradas; mecanico [COINCIDE_PROPUESTO=30]; contextual [REVISADO_CONTEXTUAL=30]; `resultados/lotes/lote_L18.json`
- `L19` (revision A): 30 entradas; mecanico [COINCIDE_PROPUESTO=30]; contextual [REVISADO_CONTEXTUAL=30]; `resultados/lotes/lote_L19.json`

## Entrega final (universo completo)

- Lotes L00–L21 publicados con commit+push tras cada lote (ver sección anterior); asociación texto↔PDF ejecutada (`resultados/asociacion_pdf_texto.json`: 21 textos, 426 valores en muestra, 100% en página alineada, offset 0).
- Entregables completos en esta carpeta: `COBERTURA_677.csv` (677 filas), `OBSERVACIONES.jsonl` (123), `DERIVADOS.json` (101 nodos: 14 piloto / 87 nuevos), `scripts/` (8 scripts), `resultados/` (inventario, verificación, lotes, asociación, recuentos, control), `INVENTARIO.md`, `HALLAZGOS.md`, `MAPA_REGENERACION.md`, `RESUMEN_PARA_CLAUDE.md`, `MANIFIESTO_SHA256.txt` (45 archivos con huella), este archivo.
- Control final: `python3 resultados_m2/cobertura_vm/scripts/control_cobertura.py` → **PASS, 0 violaciones** (`resultados/control_cobertura.json`); recuentos: 677 = 568 COINCIDE_PROPUESTO + 52 HIPOTESIS + 35 CONVENCION + 16 NO_APLICABLE + 6 DATO_AUSENTE; 60 M1_REUTILIZADA / 617 M2_NUEVA; derivados 101 = 14 + 87.

## Pendiente / siguiente acción exacta

1. **Revisión por otro contexto** sobre el commit congelado de esta rama (citados, estados, dependencias y compatibilidad antes de incorporar nada).
2. Nada más en este frente: no ampliar alcance, no PR, no fusión, no tocar el producto, los frentes B/C ni los resultados M1 ya revisados. Hallazgos materiales pendientes: los 6 DATO_AUSENTE y las 52 HIPOTESIS quedan como tales (ver `HALLAZGOS.md`).

## Modelo, herramientas y consumo

- Sesión Vibe Code de Mistral AI, modelo **`mistral-large-4-0`** (único modelo expuesto por la interfaz; no hay selector de esfuerzo). Herramientas: Python 3.12 (stdlib) + openpyxl 3.1.5 + pypdf 7.1.0 instalados en `.trabajo/pylibs` (pip del sandbox), git/gh, sha256. Sin LibreOffice ni pipeline (prohibidos y no ejecutados). XLSX solo lectura.
- Consumo/facturación: **no visible desde la sesión**; no se afirma ningún límite ni tope. No se compraron créditos ni recargas.
- Red: usada solo para GitHub (clon del auxiliar y descarga verificada de la release base-4.14 con la herramienta preparada).
