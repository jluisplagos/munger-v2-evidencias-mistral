# Punto de recuperación · Frente C (M2) · rama mistral/m2-matematica-b

Evidencia propuesta por Mistral; pendiente de revisión e incorporación por el integrador.

## Estado actual

- Repositorio auxiliar: `jluisplagos/munger-v2-evidencias-mistral` (origin verificado). Rama `mistral/m2-matematica-b` **publicada** en origin @ `f5b65f717f97f777471bc5343c6541805edcd7b4`.
- Insumos: Release `base-4.14` de `jluisplagos/munger-v2` descargada (sha256 `bb51942c…b7b93e` verificado) y `preparar_insumos.py --zip` ejecutado: 251 archivos conformes en `.trabajo/insumos_m2/` (selección parcial). Producto de referencia: commit `059f4f68dca7acf465b5f5b21de2dede84c885ff`.
- Bloque B1 terminado: definiciones fijadas (dominio, G/L/F, P*, precio de Sí, zona), demostraciones T1–T12 con bibliografía primaria (Newey–Powell 1987, Koenker–Bassett 1978, Rockafellar–Uryasev 2000), 56 casos fijados con provenance y sha256 (`casos_fijados.json`), plan finito y sensibilidad finita preanunciada (`INVENTARIO_Y_PLAN.md`).
- Oráculo propio `codigo/oraculo_precio_si.py`: selftest PASA (5 casos Anexo C como entradas + propiedades: residuo exacto 0, bisección, permutación, traslación, escala, monotonía en k, k=1 ⇒ ponderado, masa cero, rechazo de dominio inválido).

## Pendiente / siguiente acción exacta

1. Bloque B2: `codigo/ejecutar_casos.py` (propiedades ejecutables sobre los 56 casos) y `codigo/comparar_producto.py` → `COMPARACION_IMPLEMENTACION.csv` (esperado = oráculo propio; columna aparte = producto leído de `.trabajo`, con sha256 del archivo y commit). Commit y push.
2. Bloque B3: `EFECTOS_PROBABILIDADES.csv` (descomposición 4.12→4.13→4.14 de Viscofan, efecto puro de p separado del total) y `SENSIBILIDAD_FINITA.csv` (rejilla ya anunciada en `INVENTARIO_Y_PLAN.md` §4). Commit y push.
3. Bloque B4: `PROTOCOLOS_COBERTURA.md` + ejemplos sintéticos del contrato de `objetivo_v64.py`. Commit y push.
4. Bloque B5: `DOSSIER_D1_D7_D11.md`, `HALLAZGOS.md`, `RESUMEN_PARA_CLAUDE.md`, `MANIFIESTO_SHA256.txt`. Commit y push final. Sin PR ni fusión.

## Modelo y limitaciones

- Sesión: Vibe Code de Mistral AI, modelo `mistral-large-4-0` (único modelo expuesto; sin selector de esfuerzo). Herramientas: Python 3.12.15 stdlib; red solo para GitHub (descarga de release vía `gh`); sin LibreOffice ni pipeline; no se abrieron XLSX.
- Consumo/facturación: no visible desde la sesión; no se afirma ningún límite configurado. No se compraron créditos ni se usaron servicios de pago.
- No se ha modificado el producto ni `main`; no hay PR ni fusión; no se han tocado los frentes A/B ni F1/Elis ni los resultados M1 revisados.
