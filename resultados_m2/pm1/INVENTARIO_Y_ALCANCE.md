# Frente B (P-M1) · inventario, alcance y plan finito · 2026-11-16

Propuesta de evidencia o especificación de Mistral; pendiente de revisión e incorporación por el integrador. No APROBADO; no acredita aptitud financiera general.

## 1. Entorno verificado

- Repositorio auxiliar: `jluisplagos/munger-v2-evidencias-mistral`; origin verificado (`https://github.com/jluisplagos/munger-v2-evidencias-mistral.git`). No se trabaja en `main` ni en `jluisplagos/munger-v2`.
- Rama: `mistral/m2-fundamento-pm1` @ `f5b65f717f97f777471bc5343c6541805edcd7b4`, traída de origin y coincidente con `git ls-remote` (publicada).
- Base de referencia económica: Release `base-4.14` de `jluisplagos/munger-v2` (commit de referencia `059f4f68dca7acf465b5f5b21de2dede84c885ff`). ZIP descargado con `docs/programa_mistral_m2/herramientas/preparar_insumos.py --download`: 1.130.912.246 bytes, SHA-256 `bb51942cefb848e409a4828e3faeb70f94aa4d29af39cda6d90cd0a97cb7b93e` **verificado**; 251 insumos conformes en `.trabajo/insumos_m2/` (selección parcial; `producto_completo_verificado: false`), 29 PDF candidatos. Todo en `.trabajo/` (excluido de Git).
- Escritura exclusiva en `resultados_m2/pm1/`. No se ejecuta LibreOffice, el pipeline ni macros; XLSX solo en lectura; no se modifica código del producto. No se suben PDF/XLSX/ZIP/credenciales a Git.

## 2. Fuentes conservadas (bytes + SHA-256 en la selección de la base 4.14)

### Viscofan (ruta base `personaje_v2/empresas_v2_correcciones/`)

| Documento | PDF (…`2026-11_Vidrala_ensayo_4_12/viscofan/fuentes/pdf/`) | Texto (…`2026-11_Vidrala_ensayo_4_14/viscofan_decisiones/Viscofan/texto/`) |
|---|---|---|
| IA 2016 (informe anual) | `IA_2016_es.pdf` sha256 `77a4f18b…` 9.950.374 B | no seleccionado |
| AR 2017 | `AR_2017.pdf` sha256 `1e8ad90c…` 13.102.812 B | `AR_2017.txt` sha256 `844f9221…` 622.806 B |
| IA 2018 | `IA_2018_es.pdf` sha256 `a05779dd…` 4.481.979 B | `IA_2018_es.txt` sha256 `267ebb36…` 1.313.989 B |
| AR 2019 | `AR_2019.pdf` sha256 `683e8223…` 5.755.496 B | `AR_2019.txt` sha256 `7f5917e8…` 996.736 B |
| AR 2020 | `AR_2020.pdf` sha256 `499161dd…` 7.162.796 B | `AR_2020.txt` sha256 `2ac223dc…` 1.042.073 B |
| CF 2021 (cuentas) | `CF_2021.pdf` sha256 `bed55817…` 750.777 B | `CF_2021.txt` sha256 `40bf9969…` 301.410 B |
| CF 2022 (compilación) | `CF_2022_compilacion.pdf` sha256 `02fa612d…` 87.018.413 B | `CF_2022_compilacion.txt` sha256 `c154770c…` 707.000 B |
| IA 2021 | `IA_2021_es.pdf` sha256 `b7e6bc45…` 6.263.660 B | no seleccionado |
| CA 2023 / IA 2023 | `CA_2023_es.pdf` sha256 `b0bc2818…` 3.399.913 B · `IA_2023_es.pdf` sha256 `5fddc963…` 41.472.559 B | `CA_2023_es.txt` sha256 `15260cfc…` 673.249 B |
| CF 2024 (cuentas) | `CF_2024.pdf` sha256 `14b61868…` 1.599.962 B | `CF_2024.txt` sha256 `01ab4128…` 349.933 B |
| AR 2025 | `AR_2025.pdf` sha256 `e997bc7d…` 12.452.242 B | `AR_2025.txt` sha256 `0c58cd37…` 2.357.261 B |
| Boletín BME 2026-11-03 §16 | `…_4_14/viscofan*/Viscofan/fuentes_mercado/BMadrid_boletin_20261103_seccion_16.pdf` sha256 `23335f63…` 707.036 B | `.txt` sha256 `a1b9ca79…` 45.398 B |

Huellas completas: `docs/programa_mistral_m2/entrada/indice_fuentes.json` (251 entradas verificadas por `preparar_insumos.py`). Los textos llevan marcas `[PDF PAGE n]`; para IA_2016/IA_2021/IA_2023 se extraerá texto de los PDF conservados con PyMuPDF en `.trabajo/` y se citará página PDF.

### Vidrala

- Textos (…`2026-11_Vidrala_ensayo_4_14/vidrala_decisiones/Vidrala/texto/`): `CF_2017.txt` … `CF_2025.txt` (sha256 `60c948af…` … `ebfe0f35…`), `ES_2024_informacion_financiera_consolidada.txt` (`1eb5ac62…`), `ES_2025_informacion_financiera_consolidada.txt` (`a9f12f93…`).
- PDF (…`2026-11_Vidrala_ensayo/fuentes/`): cuentas consolidadas 2016–2022 en inglés (`1279_en-2016…` … `1668_en-2022…`), piloto 2025 EN/ES (`2355_en-2025…`, `2308_es-…`), arrendamientos 2023/2024 EN/ES (`1831_en-2023…`, `2145_en-2024…`, `2118_es-…`), BORME-C-2026-5696, CNMV OIR Vidrala 2026, dividendo 2275 OIR.

## 3. Fuentes oficiales declaradas como faltantes (estado de acceso medido el 2026-11-16)

| Fuente | Estado |
|---|---|
| Viscofan, informe anual / informe de gestión 2024 completo (el desglose por tipo de 2024) | AUSENTE en la base; `CF_2024.pdf` son solo cuentas y no se convierte por su nombre en informe anual. Acceso: `informeanual2024.viscofan.com` **OK con TLS verificado**; `www.viscofan.com` y `public.viscofan.com` **fallan verificación TLS del proxy del sandbox** (no se usarán bytes de ahí sin documentar el límite). CNMV OK. |
| Viscofan, presentación del plan estratégico «Beat'30» 2026–2030 (CNMV, «Otra información relevante», feb-2026) | AUSENTE en la base; no obtenida por el frente B de la 4.14. Acceso: CNMV OK con TLS verificado. |
| Viscofan, AR 2016, 2018, 2021, 2022, 2023, 2024 e IA 2019/2020/2022/2024/2025, notas de resultados trimestrales | AUSENTES (no en la selección). Algunas cubiertas por CF/IA conservados; el resto queda pendiente. |
| Vidrala, informes anuales en español 2016–2022 | AUSENTES (solo inglés 2016–2022 en la selección). |
| Series primarias INE/Eurostat de índices de precios de bienes de equipo | No descargadas aún; `ec.europa.eu` (API Eurostat) e `ine.es` responden OK con TLS verificado. |

Regla: una lectura web sin bytes conservados no se presenta como documento conservado; si no se pueden preservar bytes con TLS verificado, se declara cobertura provisional con URL, fecha, nombre, SHA-256 y tamaño si se obtuvieron, y queda pendiente su revisión.

## 4. Alcance finito del frente B

1. **B2 · Viscofan, inversión por tipo 2016–2025**: extraer de los textos/PDF conservados el desglose publicado (capacidad, proceso, EHS/sostenibilidad, ordinaria) y el total de cada año, con cita literal, línea y página PDF; años sin desglose declarados como tales. Salida: `INVERSION_VISCOFAN_2016_2025.csv` generado por script.
2. **B3 · Conciliación capex/D&A/ROU**: pagos de caja frente a adiciones; bruto frente a neto; ROU y adquisiciones; unidades y comparativos; recomprobar el puente 2022 (inversión publicada 125,6 M€ frente a capex de caja 115,566 M€) y el perímetro 2025 con ROU en la taxonomía. Salida: `PUENTE_CAPEX_DA_ROU.csv`.
3. **B4 · Fuentes oficiales nuevas**: informe de gestión/anual 2024 y presentación Beat'30 si son accesibles con bytes; conservar en la Release auxiliar `fuentes-mistral-m2-20261116` con índice SHA-256; si no, declarar cobertura provisional. Salidas: `FUENTES_NUEVAS.csv`, `FUENTES_CONSERVADAS.csv`.
4. **B5 · Vidrala, reposición y capacidad**: reconstrucciones de hornos, vida útil, capacidad, modernización, inversiones; altas ROU activo/pasivo con sus diferencias. Salida: `VIDRALA_REPOSICION_CAPACIDAD.csv`.
5. **B6 · Límites de θ/λ**: recalcular con script (`Decimal`) las tablas de θ sobre el desglose por tipo (definiciones estrecha/media/amplia, acotación, sensibilidad) y rangos de λ condicionados a supuestos explícitos (p. ej. vida útil 8–16 años como pista a contrastar, no como distribución adoptada); si se usan series INE/Eurostat, datos primarios con metadatos. El script citado `agentes/B/scripts/theta_desglose_viscofan.py` **no está en la base** y no se invoca. Salida: `CALCULOS_PM1.json` + scripts en `scripts/`.
6. **B7 · Entregas**: `DOSSIER_D2.md`, `HALLAZGOS.md`, `RESUMEN_PARA_CLAUDE.md`, `PUNTO_DE_RECUPERACION.md`, `MANIFIESTO_SHA256.txt`.

## 5. Plan y recuperación

Commit y push tras el inventario (este) y tras cada bloque (B2, B3, B4, B5, B6, B7), con `PUNTO_DE_RECUPERACION.md` actualizado (hecho, evidencia, pendiente, siguiente comando/acción, límites). No se abre PR ni se fusiona.

## 6. Límites declarados

- Los informes antiguos de la base (`documentacion_cierre_4_14/`, `configuracion_economica.py`, fases) se usan como **índices de búsqueda**, no como evidencia nueva; cada cifra citada se recomprueba en el texto/PDF conservado.
- No se convierte ninguna categoría contable de inversión en mantenimiento económico ni en crecimiento automáticamente. Una θ negativa se conserva como diagnóstico de definición/identificación; truncarla a cero no valida θ = 0.
- No se adopta θ, λ, k, probabilidades ni política alguna; no se elige estructura de P-M1; no hay recomendaciones de inversión ni autoaprobación.
- Si la evidencia no identifica un parámetro, se demuestra el límite y se deja pendiente (D2 queda para la persona responsable).

## 7. Modelo y herramientas registradas

- Sesión: Vibe Code de Mistral AI, modelo `mistral-large-4-0` (único modelo expuesto; la interfaz no ofrece selector de esfuerzo). Consumo/facturación no visible desde la sesión; no se afirma límite ni gasto.
- Herramientas: Python 3.12.15 (stdlib) + `pypdf` 7.1.0 + `openpyxl` 3.1.5 + `PyMuPDF` 2.1 (instalados con pip en el sandbox) para huellas, extracción de texto de PDF, lectura de XLSX (solo lectura) y aritmética. Red: GitHub, CNMV, BOE, Eurostat, INE e `informeanual*.viscofan.com` responden con TLS verificado; `www.viscofan.com`/`public.viscofan.com` no verifican en el proxy del sandbox; `curl` está bloqueado por el sandbox (se usa urllib). Sin LibreOffice ni pipeline (prohibidos).
