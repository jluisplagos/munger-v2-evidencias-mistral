# Encargo para Mistral · M5 · Inventario del universo (117 empresas)

**Para pegar en tres ventanas nuevas de Mistral, una por bloque.** Fecha: 18-nov-2026. Encarga: el coordinador Claude. Lee antes `AGENTS.md` del repositorio auxiliar y cumple sus reglas (no escribir en `jluisplagos/munger-v2`, no subir PDF/XLSX/ZIP a Git, no aprobar tu propio trabajo, **no valorar ni recomendar**: es un inventario, no un juicio).

## Para qué
La persona responsable tiene 117 empresas analizadas en «etapa 1» (una hoja Excel y una respuesta en texto por empresa). Antes de cribarlas con la API de Claude, necesitamos una tabla fiable de **qué es cada empresa y qué fuentes oficiales tiene**.

## Material
- Release `universo-etapa1-20261118` del repositorio auxiliar, asset `universo_etapa1.zip.zip` (SHA-256 `4d30f735…58b0a9`; compruébalo). Dentro: `EMPRESAS_LOTES_COMPLETOS/<Empresa>/<Empresa>_evaluada.xlsx` y `<Empresa>_respuesta.md`. Índice y lista en `coordinacion/cierre_v2/universo_etapa1/INDICE.tsv` (rama `coordinacion/cierre-v2`).
- La web de inversores de cada empresa y su registro oficial (sin SEC EDGAR: no tienes datos de contacto autorizados).

## Qué hacer, para cada empresa de tu bloque
Una fila de `INVENTARIO.tsv` con: `empresa` (nombre de la carpeta), `razon_social`, `pais_sede`, `bolsa_principal`, `ticker`, `isin` (si lo encuentras en fuente oficial), `moneda_estados`, `norma_contable` (IFRS / US GAAP / otra), `cierre_fiscal`, `sector_breve` (una línea: qué vende), `tipo_especial` (banco, aseguradora, holding, concesiones, materias primas, regulada, ninguno), `informe_anual_ingles_2025` (sí/no + URL oficial), `informes_anuales_ingles_10_anios` (cuántos de 2016–2025 hay en inglés en la web oficial), `fecha_etapa1` (la de la hoja, celda D4 de «Análisis» si existe), `precio_etapa1` y `moneda_precio` (de la hoja), `veredicto_etapa1` (lo que dice la respuesta: cubo/acción, literal y corto), `incidencias` (archivos que no abren, datos contradictorios, empresa deslistada, fusión…).
- Lee el Excel **solo en lectura** (por ejemplo con `openpyxl`), sin macros ni LibreOffice.
- Cada dato de la web con su URL oficial en una columna `fuentes`. Si no lo encuentras, «no encontrado», nunca de memoria.

## Bloques (uno por ventana)
- **Bloque 1 (39):** AAK, Aarsleff, ABB, Acomo, Ahold, Airbus, AirtelAfrica, Andina, Antofagasta, Arcadis, ASML, Azkoyen, BC_Speakers, Berkosan, BESI, Betsson, Bioventix, Borgestad, Bossa, Campine, Carriage, Chewy, CocaCola, Ege_Gubre, Ege_Profil, Elia, Elis, Excellence, Ferrari, Ferrovial, Frontera, FW_Thorpe, Golar, Grupa, Gubre_Fabrikalari, Hal, Heidelberg, Heijmans, HelloFresh
- **Bloque 2 (39):** Hermes, Hitachi, Hubbell, Indeks_Indes, Inditex, Indra, Intuitive, Italian_Wines, JetBlue, Jumbo, Kongsberg, Kopparbergs, Leonardo, Lifco, Lifeservicesgroup, Limes, London_Security, LOreal, LVMH, Mavi, MercadoLibre, Methanex, MLP_Saglik, Mo-BRUK, Moncler, Moury, Naturelgaz, Neochim, Nike, NKT, nVent, Oil-Dri, Omer, Oyak, Pandora, Parex, Petrobras, Petsathome, Prysmian
- **Bloque 3 (39):** Puigbrands, Quanta, Rational, Rentokil, Rheinmetall, Roche, Rovi, Royal_BAM, RStahl, Salzgitter, Sarantis, Schneider, Seche, Siemens, Sika, Sony, Spectra, Spie, SQM, Strabag, Sulzer, Sweco, TE_Connectivity, Technogym, Tessenderlo, Thales, Tupras, Upsales, Valeura, Veolia, Vidrala, Vinci, Viscofan, Vitec, Volution, Vossloh, WasteManagement, WEG, Zoetis

## Qué entregas
Rama nueva **`mistral/m5-inventario-bN`** (N = 1, 2 o 3), carpeta `resultados_universo/inventario/`: `INVENTARIO_bN.tsv` y `ENTREGA_bN.md` (máximo una página: qué no encontraste y por qué, modelo y herramientas usados de verdad). Commit y push cada 10 empresas.

---

### Frases para pegar (una por ventana)
> Lee `coordinacion/cierre_v2/universo_etapa1/ENCARGO_MISTRAL_M5_INVENTARIO.md` en la rama `coordinacion/cierre-v2` del repositorio `jluisplagos/munger-v2-evidencias-mistral` y haz el **bloque 1**. Solo ese bloque. Entrega en la rama `mistral/m5-inventario-b1`.

(Para las otras dos ventanas, cambia «bloque 1» y «b1» por «bloque 2»/«b2» y «bloque 3»/«b3».)
