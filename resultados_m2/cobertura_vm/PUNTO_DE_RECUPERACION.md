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

## Pendiente / siguiente acción exacta

1. `python3 resultados_m2/cobertura_vm/scripts/asociacion_pdf.py` (asociación texto↔PDF por tokens numéricos en páginas citadas, con pypdf).
2. Revisar y publicar lote por lote: `python3 resultados_m2/cobertura_vm/scripts/revisar_lote.py L00` … `L21`, commit+push tras cada lote completo con este archivo actualizado.
3. Entrega final: `HALLAZGOS.md`, `MAPA_REGENERACION.md`, `RESUMEN_PARA_CLAUDE.md`, `MANIFIESTO_SHA256.txt`, recuentos finales y control PASS.

## Modelo, herramientas y consumo

- Sesión Vibe Code de Mistral AI, modelo **`mistral-large-4-0`** (único modelo expuesto por la interfaz; no hay selector de esfuerzo). Herramientas: Python 3.12 (stdlib) + openpyxl 3.1.5 + pypdf 7.1.0 instalados en `.trabajo/pylibs` (pip del sandbox), git/gh, sha256. Sin LibreOffice ni pipeline (prohibidos y no ejecutados). XLSX solo lectura.
- Consumo/facturación: **no visible desde la sesión**; no se afirma ningún límite ni tope. No se compraron créditos ni recargas.
- Red: usada solo para GitHub (clon del auxiliar y descarga verificada de la release base-4.14 con la herramienta preparada).
