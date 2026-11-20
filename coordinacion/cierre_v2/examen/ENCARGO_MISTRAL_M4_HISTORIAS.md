# Encargo para Mistral · M4 · Historia de diez años, extracción independiente y contraste

**Para pegar en ventanas nuevas de Mistral, una por empresa** (cinco en total; pueden trabajar a la vez). Fecha: 18-nov-2026. Encarga: el coordinador Claude. Duración esperada: varias horas por ventana.

Lee antes `AGENTS.md` del repositorio auxiliar y cumple sus reglas: no escribir en `jluisplagos/munger-v2`, no subir PDF a Git, no aprobar tu propio trabajo, no hacer valoraciones ni recomendaciones.

## 1. Para qué sirve

El personaje Munger construye cada expediente con una **Historia de diez años** (ventas, EBIT, caja, deuda…) extraída por un agente Claude. Un error en una sola cifra puede cambiar la conclusión. Tú eres **otra familia de modelos**: haces la misma extracción **sin ver la de Claude**, y el coordinador comparará las dos cifra a cifra. Donde no coincidáis, alguien mira el PDF. Tu valor está en ser **independiente y literal**, no en coincidir.

## 2. Qué extraer (las 21 partidas)

Las definiciones exactas, que debes seguir al pie de la letra, son las del encargo de la fase 1 del producto (repositorio público `jluisplagos/munger-v2`, rama `examen/ahold-f1`, solo lectura):
`personaje_v2/empresas_v2_correcciones/2026-11_examen_universo/ahold/Ahold/prompts_generados/01_historia_2016.md` (tabla de partidas, componentes, «cero con evidencia» y EBIT derivado). Lee **solo ese archivo** de esa carpeta; es una plantilla genérica, y Ahold no es tu empresa (salvo en la ventana 5).

Partidas: `ventas`, `ebit` (impreso), `ebit_derivado` (BAI − resultado financiero, por componentes), `da`, `beneficio_neto`, `impuestos` y `resultado_antes_impuestos` (para el tipo impositivo), `cfo`, `capex`, `adquisiciones`, `circulante_lineas` (todas las líneas de variación del circulante), `intereses` (pagados), `intereses_financiacion`, `arrendamientos_principal`, `sbc`, `id` (I+D, si se publica), `acciones_diluidas`, `patrimonio`, `deuda`, `arrendamientos` (pasivo por arrendamiento), `caja`, `otros_activos_financieros`, `pensiones`, `minoritarios`.

Reglas que más se equivocan:
- **Cifra más reciente publicada.** Para el año N usa la columna comparativa del informe de N+1 si existe (recoge reexpresiones); si no, el informe de N. Anota cuál usas.
- **Tal como está impreso**: número, signo, separadores y **unidad** (millones, miles, unidades). No conviertas; declara la unidad.
- **Cero con evidencia**: si la partida no existe, cero con la página que lo demuestra. Si no la encuentras, `no_encontrado`; nunca un cero sin prueba.
- **Página = la del PDF** (la que muestra el visor), no la impresa en el pie, salvo que coincidan.
- Cita literal corta (la línea de la tabla con su rótulo).

## 3. Las cinco ventanas

| Ventana | Empresa | Años | Fuentes (Release del repositorio auxiliar) | Ojo |
|---|---|---|---|---|
| 1 | **Jumbo S.A.** | ejercicios 2016/17 … 2025 (diez) | `fuentes-examen-20261118`: `jumbo-annual-report-*.pdf`, y para 2022 y 2023 los XHTML `jumbo-annual-report-fy2022.xhtml` y `…fy2023.xhtml` (ábrelos en el navegador) | cambio de ejercicio: julio–junio hasta 2018/19, transición de **seis meses** jul–dic 2019, año natural desde 2020. Trata la transición como un periodo propio y dilo. En los XHTML no hay páginas: cita la sección y la tabla. |
| 2 | **Zoetis Inc.** | 2016 … 2025 | `zoetis-10k-fy2016.pdf` … `zoetis-10k-fy2025.pdf` | **Solo los 10-K.** No abras nada publicado después del 9-oct-2026 (comunicado, presentación ni 10-Q del T3). US GAAP: los arrendamientos operativos no tienen «principal» en financiación; dilo. |
| 3 | **VINCI SA** | 2016 … 2025 | `vinci-annual-report-2016…2019.pdf`, `vinci-urd-2020…2025.pdf` | documentos muy largos: usa las cuentas consolidadas. Concesiones: la deuda es grande; separa deuda financiera de arrendamientos. |
| 4 | **Waste Management, Inc.** | 2016 … 2025 | `wm-annual-report-2016…2025.pdf` (cada uno incluye el 10-K) | US GAAP, como Zoetis. |
| 5 | **Ahold Delhaize** (contraste, no a ciegas) | 2016 … 2025 | los textos ya extraídos del expediente: `jluisplagos/munger-v2`, rama `examen/ahold-f1`, carpeta `personaje_v2/empresas_v2_correcciones/2026-11_examen_universo/ahold_f1/Ahold/texto/` (marcas `[PDF PAGE n]`) | Aquí **sí** comparas con lo de Claude: el libro `Ahold_v63_datos.xlsx` no está en Git, así que usa `fase1_v63.json` de esa carpeta (`historia.partidas.<partida>.valores`). Para cada una de las 210 cifras: ¿la encuentras en la página citada con ese valor? |

Descarga los assets con `gh release download fuentes-examen-20261118 -R jluisplagos/munger-v2-evidencias-mistral -p '<patrón>'` y comprueba su SHA-256 contra `coordinacion/cierre_v2/examen/RELEASE_FUENTES_EXAMEN_SHA256SUMS` (rama `coordinacion/cierre-v2`). **En las ventanas 1 a 4 no abras las carpetas `jumbo/`, `zoetis_t1/` ni ninguna otra del expediente en `munger-v2`**: perderías la independencia.

## 4. Qué entregas

Rama nueva **`mistral/m4-historia-<empresa>`** (`jumbo`, `zoetis`, `vinci`, `wastemanagement`, `ahold`), carpeta `resultados_examen/historia_independiente/<empresa>/`:

1. `HISTORIA.csv` (ventanas 1–4), una fila por partida, año y componente: `partida, anio, periodo_exacto, valor_impreso, unidad, signo_en_el_documento, archivo, sha256_archivo, pagina_pdf, cita_literal, informe_usado (N o comparativo N+1), estado (encontrado | cero_con_evidencia | no_encontrado), nota`.
2. Ventana 5: `CONTRASTE_AHOLD.csv`: `partida, anio, valor_claude, valor_en_la_pagina, archivo, pagina, coincide (si/no/no_se_encuentra), cita_literal, nota`, y al final un recuento.
3. `ENTREGA.md` (máximo una página): qué hiciste, lo que no encontraste y por qué, dudas de definición, el modelo y las herramientas que usaste de verdad.

Commit y push al terminar cada bloque de años.

## 5. Cómo se acepta

El coordinador comparará tu `HISTORIA.csv` con la Historia de Claude. Cada discrepancia se resolverá mirando el PDF; si el error es tuyo se anota, si es de Claude se corrige en el expediente con su trazabilidad. Una cifra sin página o sin cita no cuenta. Prefiero un `no_encontrado` honesto a una cifra dudosa.

---

### Frase para pegar en cada ventana (cambia solo el número y el nombre)

> Lee `coordinacion/cierre_v2/examen/ENCARGO_MISTRAL_M4_HISTORIAS.md` en la rama `coordinacion/cierre-v2` del repositorio `jluisplagos/munger-v2-evidencias-mistral` y haz **la ventana N (EMPRESA)**. Solo esa ventana. Entrega en la rama `mistral/m4-historia-EMPRESA`.
