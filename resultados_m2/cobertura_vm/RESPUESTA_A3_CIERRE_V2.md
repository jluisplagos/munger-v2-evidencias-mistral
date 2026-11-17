# Respuesta A3 · frente A (M2, cobertura VM) · sobre `8b88fab` (respuesta A2 v4.0)

- **De:** relevo de Mistral A en sesión Vibe Code de Mistral AI, modelo `mistral-large-4-0` (único expuesto; consumo no visible). Rama `mistral/m2-cobertura-vm`, carpeta exclusiva `resultados_m2/cobertura_vm/`.
- **Encargo:** `coordinacion/cierre_v2/revisiones_coordinador/A2_8b88fab/CORRECCION_A3.md` y `REVISION_A2_8b88fab.md` leídos íntegramente con `git show origin/coordinacion/cierre-v2:…` (control vigente `57b34a60`; sin cambios posteriores sobre `coordinacion/cierre_v2`). Un commit por punto (R1…R8); G-DOCS atendido antes en bloque separado (rama `mistral/g-manual-traspaso`, commit `a0524d9`).
- **Entorno real:** Python 3.12.15, openpyxl 3.1.5, pypdf 7.1.0 (en `.trabajo/pylibs`); ZIP base-4.14 descargado vía `gh api` (1.130.912.246 bytes, sha256 `bb51942c…b7b93e`) y `preparar_insumos.py --zip` → 251/251 insumos conformes en `.trabajo/insumos_m2`. Sin LibreOffice, sin pipeline del producto, sin red salvo GitHub (lectura/escritura del auxiliar). pypdf 6.17.0 instalado aparte (`/tmp/pylibs6`) solo para reproducir el defecto de `asociacion_pdf.py`.
- **Reproducción base (antes de tocar nada):** pipeline completo → 59/62 byte a byte vs `8b88fab` (las 3 diferencias son la marca de tiempo de 2 docs generados y la ruta absoluta de `inventario.json`, ya documentadas por el revisor); CSV 169/209/133/60/106; control PASS exit 0; sondas del informe s02/s03/s07 con los mismos defectos que el revisor (1d, 3e–3g; R1a–R1e, R2a–R2e, R3a/b, R4a/c).

## Resultado por punto (comando ejecutado, exit, sondas, cambios de estado)

| Punto | Commit | Arreglo | Sonda(s) | Cambios de estado (CSV) |
|---|---|---|---|---|
| A3-R1 signos | `93a02e0` | `signed_num`: la comparación posicional compara con signo (paréntesis, U+2212, `-`) y magnitud en espacio de dígitos | informe s02/s07 (R1a/R1b → OK) + propia `s11_R1` (R1f CONFLICTO signo real, R1g, R1h OK) | 104 filas: 70 CONFLICTO→REVISADO, 34 CONFLICTO→PENDIENTE (`cambios_estado_a3_R1.json`) |
| A3-R2 cabeceras/columnas | `d11ee44` | `es_linea_columnas` excluye frases narrativas (palabras alfa > años fuera de paréntesis); empate a la cabecera más próxima a la fila; fusión de cabecera partida en la zona de la fila | informe (R1c→CONFLICTO, R1d→NO_DECIDIBLE, 2a–2g ok) + propia `s11_R2` (R2g–R2i ok) | 4 filas REVISADO→PENDIENTE (p. ej. `Viscofan Configuración V6.4!B150`) |
| A3-R3 importe con forma de año | `74d94f8` | los valores 20xx sin puntuar ocupan su posición (antes se descartaban y desplazaban); el año en prosa `2024,` no es importe ni año de columna, pero sí cuenta en el bloque | informe (R1e→NO_DECIDIBLE, R4c ok) + propia `s11_R3` (R3g–R3j ok) | 29 filas (20 PENDIENTE→REVISADO, 4 PENDIENTE→CONFLICTO, 3 CONFLICTO→PENDIENTE, 2 REVISADO→PENDIENTE) |
| A3-R4 reexpresión | `c472595` | quitado el atajo «no reexpresado + valor suelto»; fila del original solo por rótulo completo; escala y perímetro comparados (original vs comparativo); negación por polaridad | informe s02/s07 criterios 2 y 3 sin defectos (3e/3f/3g, R2a–R2f pasan) + propia `s11_R4` (R4g–R4j ok) | 70 filas (39 REVISADO→PENDIENTE incl. las 2 promociones 28/35, 5 →CONFLICTO, etc.) |
| A3-R5 versión | `2e4eb15` | `check_version` con límites de palabra (12025 / 2025,4 ya no acreditan); año con coma en título/prosa sí cuenta | informe (1d, R4a → CONFLICTO) + propia `s11_R5` (R5a–R5d ok) | 0 filas (0 casos reales, como decía el informe; 3 CONFLICTO de «2020,» ya reparados en R3) |
| A3-R6 escala | `447a977` | `MILLONES_RE` ampliada: `EUR million(s)`, `€ million`, `million(s) EUR`, `Millones de €`/`Millones €` | informe (R3a/R3b → CONFLICTO) + propia `s11_R6` (R6a–R6e ok) | 0 filas (sin impacto real) |
| A3-R7 derivados como operandos | `4f50e6a` | `estado_operando` lee el estado de un operando derivado de su nodo (transitivo) en `derivaciones.py` y `control_cobertura.py`; control negativo nuevo §10 en `control_negativo.py` | propia `s11_R7` (R7a–R7d ok) + control_negativo registra la sonda A3-R7 detectada | 0 filas hoy (los 5 operandos derivados son del piloto); el control negativo synthetic D=f(E), F pendiente → D PENDIENTE (antes REVISADO con PASS) |
| A3-R8 textos y huellas | (este bloque) | huellas/recuentos de `ENTREGA.json` regenerados desde salidas (`generar_entrega_json.py`); textos desfasados corregidos desde salidas (`actualizar_textos_resumen.py`); `cola_pendientes.py`/`resolver_bloque2.py` funcionan con `-I`; `asociacion_pdf.py` falla con mensaje claro con pypdf 6.x (probado con 6.17.0: exit 1 + mensaje; con 7.1.0 exit 0); sondas del informe publicadas en `sondas_a3/sondas_informe/` | verificación: `python3 -I -B … cola_pendientes.py` rc=0; pypdf 6.17.0 rc=1 con mensaje; pypdf 7.1.0 rc=0 (21/21 ASOCIACION_VERIFICADA) | sin cambio de estados |

## Estado final (generado, `resultados/RECUENTOS_VIGENTES.md`)

- CSV 677: **209 REVISADO / 283 PENDIENTE / 19 CONFLICTO / 60 REUTILIZADO_M1 / 106 NO_APLICA** (en `8b88fab`: 169/209/133/60/106). Los 133 CONFLICTO no eran 133 errores económicos: 104 dependían solo del artefacto de signo (A3-R1) y el resto se reparte en reexpresión no acreditada, cabeceras narrativas/partidas y años con coma.
- `control_cobertura.py` **PASS exit 0** (0 violaciones); `control_negativo.py` 219 mutaciones (140 ctx / 40 mec), bilaterales 15/15 ok, sondas d375d80 5/5 CONFLICTO, sonda A3-R7 ok.
- Diff de estados vs `8b88fab` (base revisada): 142 fuentes / 184 filas CSV en `resultados/cambios_estado_a3.json`; por punto en `cambios_estado_a3_R1…R7.json`.
- Nada sustituye cifras ni fuentes: los cambios son de estado contextual únicamente. Las entradas que pierden acreditación quedan PENDIENTE (o CONFLICTO si hay contradicción documentada).

## Conservado (conforme) de A2

Reproducción 59/62 byte a byte (3 diferencias explicadas), control PASS, negativos, bilaterales 15/15, sondas d375d80 5/5 CONFLICTO, propagación a 101 nodos, sondas 2a–2e, 4a–4c, 1b, 1c, 3a–3d, 3h–3j, 3i (siguen pasando tras A3), caso real C37.

## Límite

Revisión y correcciones del verificador propio del frente A (autocomprobación + sondas), no auditoría independiente: queda pendiente la revisión del coordinador sobre solo lo afectado. No acredita aptitud económica; no integra nada en el producto.
