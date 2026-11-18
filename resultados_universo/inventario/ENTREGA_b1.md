# ENTREGA M5 · Inventario bloque 1 (39 empresas) · rama `mistral/m5-inventario-b1`

Entregables en `resultados_universo/inventario/`: `INVENTARIO_b1.tsv` (39 filas + cabecera) y este `ENTREGA_b1.md`. Commit y push cada 10 empresas (4 commits: 10, 20, 30, 39).

## Material y verificación
- Release `universo-etapa1-20261118`, asset `universo_etapa1.zip.zip`: SHA-256 comprobado = `4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9` (coincide con el encargo).
- Los 39 XLSX se leyeron solo en lectura con openpyxl (sin macros ni LibreOffice); los 39 SHA-256 coinciden con `INDICE.tsv`. Ningún archivo dio error de apertura.
- `fecha_etapa1` = celda D4 de «Análisis»; `precio_etapa1`/`moneda_precio` = fila «Precio actual» y «Control maestro» de cada hoja; `veredicto_etapa1` = literal de `<Empresa>_respuesta.md` (las 39 dicen «Cubo», con la etiqueta corta entre paréntesis).

## Qué no se encontró y por qué
- **ISIN no verificado en fuente oficial** (se deja «no encontrado en fuente oficial consultada», nunca de memoria): AAK, AirtelAfrica, Andina, Antofagasta, Azkoyen, BC_Speakers, Berkosan, Betsson, Bioventix, Borgestad, Bossa, Carriage, Chewy, CocaCola (CCI), Ege_Gubre, Ege_Profil, Frontera, FW_Thorpe, Golar, Grupa, Gubre_Fabrikalari, Hal, Heidelberg, HelloFresh. Se buscaron en webs IR, Euronext Live, LSE, SIX, NewConnect, KAP y CNMV; los valores vistos solo en agregadores (MarketScreener, Investing, etc.) no se anotan. **ISIN sí verificados en fuente oficial**: Aarsleff DK0060700516, ABB CH0012221716 (SIX), Acomo NL0000313286, Ahold NL0011794037, Airbus NL0000235190, Arcadis NL0006237562, ASML NL0010273215, BESI NL0012866412, Campine BE0003825420, Elia BE0003822393, Elis FR0012435121, Ferrovial NL0015001FS8, Heijmans NL0009269109 (todos Euronext Live), Excellence PLEXCLN00016 (NewConnect) y Ferrari NL0011585146 (ferrari.com, listing information).
- **Informe anual 2025 sin versión en inglés en la web oficial**: Berkosan, Bossa, Ege_Gubre, Ege_Profil, Gubre_Fabrikalari (informes 2025 solo en turco; TMS 29) y Excellence (informe 2025 solo en polaco). Se indica «no» con la URL oficial consultada.
- **Recuento de informes anuales en inglés 2016–2025 no verificado uno a uno** en la web oficial: Andina, Azkoyen, Bioventix, Carriage, CocaCola (CCI), Frontera (archivos existen en web IR propia, no contados). Donde el archivo oficial se contó: 10 para la mayoría; 9 Aarsleff (cierre 30-sep) y HelloFresh (IPO 2017); 7 AirtelAfrica (IPO 2019) y Chewy (IPO 2019); 3 Grupa Klepsydra (IPO 2023); 0 Excellence en inglés.
- **Norma contable no indicada en la web IR consultada**: Bioventix y FW_Thorpe (la página IR vista no lo especifica; la hoja indica IFRS en ambos casos salvo Bioventix, «Otra»).
- **Incidencias anotadas en filas**: Frontera (venta del upstream colombiano a Parex cerrada 1-jun-2026, devolución de capital C$8,34/acción, dividendo suspendido, perímetro cambiado); Azkoyen (JG aprobó la segregación de la actividad VPS); Hal (la hoja «Control maestro» dice IFRS mientras la fuente oficial indica US GAAP y USD de estados).
- No se usó SEC EDGAR: los 10-K/20-F de Carriage, Chewy, Ferrari, Golar y HAL se citan solo desde las webs IR propias de cada empresa.

## Modelo y herramientas usados de verdad
- Modelo: **mistral-large-4-0** (este agente). Herramientas: bash, `gh` CLI (clon, release, push), Python 3 + openpyxl 3.1.5 (lectura de XLSX), web_search (Brave) y web_fetch sobre webs IR/registros oficiales.
- Nada de PDF/XLSX/ZIP se ha subido a Git; todo el trabajo intermedio quedó en `.trabajo/` (gitignored). No se valora ni recomienda nada: es inventario puro.
