# Preparación F-B3 / F-C1 · Cola 2 · rama mistral/f-alcance-real

Paquete de **preparación** (ensayo), no de ejecución: nada corrido con LibreOffice ni pipeline.

- `SELECCION.csv` — hasta 3 candidatas por recorrido (B y C) con elegibilidad documental/negocio/
  método, carencias, principal/reserva, exclusiones y motivos. Sin usar precios para seleccionar.
- `PROTOCOLO_CONGELADO.md` — criterios y protocolo fijados **antes de calcular**.
- `INVENTARIO_Y_HUECOS.csv` — recursos ya conservados (ZIP base-4.14, 6799 archivos, SHA-256
  `bb51942cefb848e409a4828e3faeb70f94aa4d29af39cda6d90cd0a97cb7b93e`; 6 empresas en
  `empresas_v2`; todos los ensayos de `empresas_v2_correcciones/` incluido `elis_decisiones` y
  `…/2026-11_Vidrala_ensayo/fuentes/`; `contrastes/`; y una fila por `.bat` con su SHA-256) y
  huecos. El alcance negativo se declara en la fila del ZIP (de 6799 archivos, 6476 entran y 323
  quedan fuera: `v6/` 91, `personaje_v2/` fuera de `empresas_v2*` 152, `documentacion_reparacion/` 45,
  `kit_pipeline_munger/` 26, 8 sueltos en la raíz y 1 suelto en `empresas_v2_correcciones/`;
  ningún PDF queda fuera). Lo regenera byte a byte
  `scripts/inventario_desde_zip.py <ruta_zip> <salida.csv> <salida_huellas.csv>` (F2-D1/D2/D7).
- `MAPA_ENTRADAS.jsonl` — entradas mínimas por recorrido (B V6.4 / C motor C).
- `CONTRATO_C_PROPUESTA.md` — contrato económico específico propuesto para el primer caso C real
  (patrimonio y ROE), puentes contables, hipótesis y límites (E62: no valida solvencia ni capital
  regulatorio; la plantilla no acredita el negocio por sí sola).
- `fuentes/huellas_fuentes_conservadas.csv` — 29 PDF del dossier B @ daa7478 (ruta/bytes/SHA-256)
  + la release base-4.14 con SHA-256 completo.
- `fuentes/huellas_todas_las_fuentes.csv` — los **71 PDF del ZIP** con ruta/bytes/SHA-256 completo
  + la release con SHA-256 completo (antes 29/71 y SHA truncado; F2-D2).
- `scripts/inventario_desde_zip.py` — regenera byte a byte `INVENTARIO_Y_HUECOS.csv` y
  `fuentes/huellas_todas_las_fuentes.csv` desde el ZIP pasado por argumento (sin rutas fijas).
- `ENTREGA_B3_C1.json` — entrega según plantilla.

## Hallazgos

- **B (tercer caso fuera de muestra)**: no hay empresa fuera de muestra con insumos conservados.
  Ahold Delhaize (reserva nombrada en la matriz) carece de Excel de etapa 1; su `.bat` de descargas
  **sí está conservado** en el ZIP (`descargas_bat/descargar_fuentes_ahold.bat`, SHA-256
  `04feebd409754a91e509dfde1e8dd63a1e8534695d05cb75fffca6a97bd53d88`, fila propia en
  `INVENTARIO_Y_HUECOS.csv`) pero **no se ha ejecutado** → **bloqueada, no forzada**. Hermès/Aarsleff
  sirven solo como reserva técnica dentro de muestra. Elis excluida (no forzar motor B; la fase A
  eligió A y cerró «límite del modelo»).
- **C (primer caso real)**: ninguna empresa financiera conservada; solo 2 fixtures sintéticos.
  Principal propuesta = banco/aseguradora con fuente oficial pendiente; bloqueo documental concreto
  declarado (solo GitHub alcanzable en este entorno).
- Límites de la matriz vieja: I19/I20 no se restauran como vigentes; la frase de doble PPA más
  fuerte que F1 no se restaura (F1 es la vigente).

*Propuesta de preparación de Mistral; pendiente de revisión del coordinador. No APROBADO ni aptitud
financiera general.*
