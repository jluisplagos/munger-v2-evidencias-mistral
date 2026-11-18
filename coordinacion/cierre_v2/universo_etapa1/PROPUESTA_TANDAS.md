# Propuesta de tandas del cribado (dry-run, sin API)

- Código: `5e8d4b9e1be84e1dc24a1eb4e1169c1da0c704b9` (rama `automatizacion/cribado-tandas`).
- Release: `universo-etapa1-20261118/universo_etapa1.zip.zip`, SHA-256 `4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9` (comprobada; las 117 huellas de libro coinciden con INDICE.tsv).
- Modelo claude-opus-5-5, esfuerzo high, tarifas 4 / 20 USD por millón (2026-11-17).
- Preparadas 111 de 117; total de cotas USD 135.588848; orientativo USD 50.7365.
- Entradas propuestas para cada tanda: `coste_maximo_por_empresa_usd` = 1.6 (la mayor reserva es 1,52), `coste_maximo_tanda_usd` = 30, `gramatica` según el resultado de la tanda 0. Escribir 1.6 con punto.
- El orden es alfabético: no es una recomendación ni una prioridad de análisis.
- Excluidas hasta después del 23-nov (C-EX, lista cerrada en el código): Ahold, Jumbo, Zoetis, Elis, Vinci, WasteManagement.
- Lanzar las tandas de una en una (comparten grupo de concurrencia: una segunda en cola cancela a la que espera).

## Tanda 0 · prueba técnica de una empresa (lanzar primero)

Entradas: `empresas` = `Pandora`, `modelo` = claude-opus-5-5, `esfuerzo` = high, `coste_maximo_por_empresa_usd` = 1.6, `coste_maximo_tanda_usd` = 2, `gramatica` = si. Preparada sin API en `tanda0_pandora_preparacion/` (reserva 1,183 USD con la gramática; hoja del 2026-10-25). Comprobar: estado, model_returned, facturación, tokens reales frente a la cota y al orientativo, duración y publicación del informe de la empresa y del de la tanda. Si da 400: reconciliar la reserva en Console y repetir con `gramatica` = no. Su veredicto no cuenta para A6 si después cambia el encargo. Alternativa: Inditex (cota 1,19).

## Tandas de 20

| Tanda | Empresas | Suma de cotas USD | Mayor cota USD | Orientativo USD |
|---|---|---|---|---|
| 1 | 20 | 24.410716 | 1.335816 | 9.1360 |
| 2 | 20 | 24.369272 | 1.509996 | 9.1243 |
| 3 | 20 | 23.896912 | 1.272568 | 8.9894 |
| 4 | 20 | 24.386440 | 1.520204 | 9.1289 |
| 5 | 20 | 24.877052 | 1.362968 | 9.2696 |
| 6 | 11 | 13.648456 | 1.415376 | 5.0883 |

## Tanda 1

Entrada `empresas`, lista para pegar:

```
AAK, Aarsleff, ABB, Acomo, Airbus, AirtelAfrica, Andina, Antofagasta, Arcadis, ASML, Azkoyen, BC_Speakers, Berkosan, BESI, Betsson, Bioventix, Borgestad, Bossa, Campine, Carriage
```

## Tanda 2

Entrada `empresas`, lista para pegar:

```
Chewy, CocaCola, Ege_Gubre, Ege_Profil, Elia, Excellence, Ferrari, Ferrovial, Frontera, FW_Thorpe, Golar, Grupa, Gubre_Fabrikalari, Hal, Heidelberg, Heijmans, HelloFresh, Hermes, Hitachi, Hubbell
```

## Tanda 3

Entrada `empresas`, lista para pegar:

```
Indeks_Indes, Inditex, Indra, Intuitive, Italian_Wines, JetBlue, Kongsberg, Kopparbergs, Leonardo, Lifco, Lifeservicesgroup, Limes, London_Security, LOreal, LVMH, Mavi, MercadoLibre, Methanex, MLP_Saglik, Mo-BRUK
```

## Tanda 4

Entrada `empresas`, lista para pegar:

```
Moncler, Moury, Naturelgaz, Neochim, Nike, NKT, nVent, Oil-Dri, Omer, Oyak, Pandora, Parex, Petrobras, Petsathome, Prysmian, Puigbrands, Quanta, Rational, Rentokil, Rheinmetall
```

## Tanda 5

Entrada `empresas`, lista para pegar:

```
Roche, Rovi, Royal_BAM, RStahl, Salzgitter, Sarantis, Schneider, Seche, Siemens, Sika, Sony, Spectra, Spie, SQM, Strabag, Sulzer, Sweco, TE_Connectivity, Technogym, Tessenderlo
```

## Tanda 6

Entrada `empresas`, lista para pegar:

```
Thales, Tupras, Upsales, Valeura, Veolia, Vidrala, Viscofan, Vitec, Volution, Vossloh, WEG
```

Excepciones de ceguera aplicadas (pendientes de revisión): Andina (CONTENIDO_PROHIBIDO_EN_EL_PAQUETE:hoja_control_maestro:rubrica), Petsathome (CONTENIDO_PROHIBIDO_EN_EL_PAQUETE:hoja_control_maestro:rubrica)

