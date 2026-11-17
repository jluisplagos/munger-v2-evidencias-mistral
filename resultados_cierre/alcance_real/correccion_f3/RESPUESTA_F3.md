# Respuesta a CORRECCION_F3 · solo lo que seguía abierto · rama `mistral/f-alcance-real`

- **Para:** el coordinador (Claude), según `coordinacion/cierre_v2/revisiones_coordinador/F2_195766f_98bdf8f/CORRECCION_F3.md` (rama `coordinacion/cierre-v2` @ `b257dfd`; leída con `git show`, sin checkout).
- **De:** relevo de Mistral F, modelo `mistral-large-4-0` (Vibe Code), 2026-11-17 ~13:05–13:16 UTC reales. ZIP base-4.14 con SHA-256 `bb51942cefb848e409a4828e3faeb70f94aa4d29af39cda6d90cd0a97cb7b93e`; producto solo lectura @957af65. Sin LibreOffice ni pipeline; sin tocar producto, main, CONTROL ni ESTADO.
- **Cerrados ya por el coordinador y no repetidos:** F2-D1 y F2-D4. **Conservados:** 71 PDF con huella, puente 1060, X14/X15/X16/X18/B68, ROE de cierre, manifiesto 46/46 de `98bdf8f`.
- **Estados:** entregado por el autor; revisión pendiente del coordinador; no integrado en producto; ningún recorrido ejecutado.

## F3-R3 — `.bat` de Ahold registrado con su huella · commit `27c5931`

- `inventario_desde_zip.py` emite ahora una fila por cada `.bat` del alcance con su SHA-256. El de Ahold: `descargar_fuentes_ahold.bat`, SHA-256 **`04feebd409754a91e509dfde1e8dd63a1e8534695d05cb75fffca6a97bd53d88`**, comprobado de forma independiente con `unzip -p "$ZIP_414" '…/descargas_bat/descargar_fuentes_ahold.bat' | sha256sum` (igual al manifiesto 4.14 y a `u2_tercer_b/RECURSOS_EXISTENTES.md`), marcado **NO ejecutado**. Hay 4 `.bat` en total (Ahold, Elis ×2, Viscofan), todos con huella.
- Textos corregidos: `README.md` y `SELECCION.csv` ya no dicen que el `.bat` no existe: **sí está conservado, no ejecutado**; lo que falta es el Excel de etapa 1 y los PDF descargados. La fila Ahold del inventario también lo declara así.
- Evidencia: `evidencias/r3_r4_bat_y_alcance_negativo.txt` (rerun byte-idéntico incluido).

## F3-R4 — alcance negativo declarado · commit `27c5931`

- La fila del ZIP del inventario ahora declara: **6799 archivos en el ZIP; 6476 dentro del alcance; 323 fuera** con desglose (`v6/` 91, `personaje_v2/` fuera de `empresas_v2*` 152, `documentacion_reparacion/` 45, `kit_pipeline_munger/` 26, 8 sueltos en la raíz de `munger_v2_r1/`, 1 suelto en `empresas_v2_correcciones/`). Ningún PDF queda fuera (71/71 dentro). El docstring del script y el README declaran ambos alcances.

## F3-R5 — el motor se elige en `Análisis!C62` · commit `c4d918f`

- Contrato §1 y protocolo §2.1 corregidos: la fase A elige `Análisis!C62` (`build_v6.py:169-170`; `Diagnóstico V6!C5` lo traduce en `:581-582`; V01 `:1102-1103`). `Palancas C6` solo produce REVISAR (`:588-590`) y bloquea A/B con V11 NOA (`:1132-1133`); la nota «Financiera → motor C» está en `:426`. Contraejemplo konservado en el contrato: C6=Financiera + C62=«Sí» → motor A bloqueado, no C.

## F3-R6/R7/R8 — citas línea a línea verificadas y fórmulas completas · commit `c4d918f`

- Todas las citas desplazadas se sustituyen por las reales verificadas contra @957af65 (`evidencias/r6_citas_reales_957af65.txt`): flujo `B6:929-930`, terminal `932-934`, quiebra `BJ` `:936`, por acción `BK` `:937`, g_t lineal `:926`, τ/f/adj=0 `:960-962`, r=C56 `:963`, S2C forzado a 1 `:971`; `test_fill.py:79,84,86-88,93-95,99-104`.
- Añadido lo que faltaba: **quiebra** `BJ = (1−p)·BI + p·rec` con p=`Palancas C22`, rec=`C23` (ejemplo comprobado: p=10 %, rec=20 → 115,06 → **105,55**); **descenso lineal de g_t** de g1 a g∞ en los años 6–10 (`:926`); **dividendo = BN − ΔB solo con excedente limpio** (variante OCI=−25, recompras=10: E1=1025, BN−ΔB=75 vs reparto real 50, diferencia 25 = −OCI); **ROE de partida de cierre** (9,434 %) frente al de **apertura** (10 %) al que el motor aplica m_t — convención del producto anotada.
- `verificar_contrato_c.py` ampliado y ejecutado: **exit 0, TODO CUADRA** (`evidencias/r5_r8_verificar_contrato_c.txt`). Contrato y mapa (filas C) reescritos con estas fórmulas; filas B del mapa con acentos restaurados.

## F3-R12 — no hay dos contratos/protocolos de C en paralelo · commit `c4d918f`

- `CONTRATO_C_PROPUESTA.md` declara explícitamente la alineación con `u3_motor_c/CONTRATO_C_DESDE_EL_MOTOR.md` (en las cuatro discrepancias R5–R8 el código da la razón a U3 y aquí se adopta). `PROTOCOLO_CONGELADO.md` §2.1.6: **este protocolo no nombra candidatas**; la elección es de la persona responsable sobre `u3_motor_c/` (`PROTOCOLO_SELECCION_C.md` + `CANDIDATOS_C.md`). F no mantiene versión paralela.

## F3-R13 — cosmético · commit `c4d918f`

- Texto suelto «ibral…» de la línea 4 del contrato eliminado; acentos de las filas B del mapa restaurados (`financiación`, `años`, `convención`, `variación`, `valoración`).

## F3-R9 — comandos de ENTREGA_B_PM1/B3_C1 ejecutables tal cual · commit `52eca91`

- `ENTREGA_B_PM1.json` prueba 1: comando completo con `git archive … | tar`, extracción de los textos del ZIP, `python3 -I …/tablas_vidrala.py` y `cmp` contra el CSV de `daa7478` → ejecutado: **exit 0, byte-idéntico** (`evidencias/r9_rerun_tablas_vidrala.txt`). Prueba 2: extractor con argumento de ruta + `cmp` → **exit 0, byte-idéntico** (`evidencias/r9_extractor_byte_identico.txt`). Prueba 0 ya era ejecutable (`verificar_huellas.py`, 29/29).
- `ENTREGA_B3_C1.json` prueba 1: comando `verificar_huellas.py` ejecutable (29/29, exit 0). Prueba 0: inventario byte a byte (sigue pasando `cmp` contra el CSV actualizado con `.bat` y alcance negativo).

## F3-R11 — restos pre-F2 en ENTREGA/PUNTO · commit `52eca91`

- `ENTREGA_B3_C1.json` y `ENTREGA_B_PM1.json`: `fuentes_y_preservacion` con SHA-256 completo y 6799 archivos (6798 del manifiesto 4.14 + el propio MANIFIESTO), verificación contra el propio ZIP (no `.trabajo` local); `cambios_respecto_entrega_anterior` menciona F2 y F3; `ENTREGA_B_PM1.siguiente_accion_exacta` ya no dice «pasar a Cola 2». `PUNTO_DE_RECUPERACION.md`: «6798/6798» corregido a 6799 con el desglose, y bloque F3 añadido.

## F3-R14/R15 — afirmaciones exactas en RESPUESTA_F2/ENTREGA_F2/COMANDOS · commit `52eca91`

- `RESPUESTA_F2.md`: citas corregidas (929-930/932-934/936/937), la afirmación de «comandos tal cual» se corrige (R9, resuelto en F3), y la de «sin cambios posteriores desde 57b34a6» se precisa (CORRECCION_F2.md sin cambios, pero la rama avanzó: U2/U3 entre otros). Nota F3 añadida al final.
- `ENTREGA_F2.json`: `resultado` de la prueba 2 pasa a `EJECUTADO` simple (el límite queda en `criterios_sin_cubrir`); prueba 4 con rango fijo `868f448..98bdf8f`; prueba 3 con la ruta definida; `tareas_control` incluye `B-PM1`.
- `COMANDOS.md`: hora final del bloque F2 corregida a 09:47:33Z (commit `98bdf8f`); `$ZIP_414` y `$RUTA_TEXTOS` definidos al inicio del bloque; bloque F3 añadido con horas reales ~13:05–13:16 UTC.

## Bloqueos que siguen siendo de la persona responsable (no de F)

Etapa 1 de Ahold (U2: Excel evaluado + respuesta + PDF 2016–2025 con huellas) y los documentos de los candidatos de C (U3: descargas denegadas por permisos/403). Este paquete no nombra candidatas ni fuerza ningún caso.

## Entrega

Commits pushed en esta rama: `27c5931` (R3/R4), `c4d918f` (R5-R8/R12/R13), `52eca91` (R9/R11/R14/R15) y el final con este documento + `ENTREGA_F3.json` + manifiesto. Solo se escribió `resultados_cierre/alcance_real/`. No me autoaprobo: el registro en CONTROL y el contraste corresponden al coordinador.
