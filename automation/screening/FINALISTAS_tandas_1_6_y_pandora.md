# Segunda vuelta del universo · finalistas propuestos (criterio mecánico)

- Rama de registro: `origin/automatizacion/claude-api-piloto-registro` en `6fee3d2ed8ca58f472b4dd35e07ccb94872119c2`.
- Ejecuciones del cribado leídas: 44406828081, 44413758195, 44502520327, 44505954250, 44509331308, 44512238939, 44515220408. Son las seis tandas completas (con el informe de tanda publicado) y Pandora (tanda 0); la tanda 4 tiene 19 empresas porque Pandora ya estaba cribada.
- Empresas leídas: 111; con resultado utilizable: 111.
- Resultados de los filtros tal como los devolvió el modelo en el cribado: **sin revisar ni aceptar**.
- Generado por `automation/screening/finalistas.py` (sin API, sin red). No es una recomendación de compra ni una prioridad: decide la persona responsable.

## Criterio

1. Solo cuentan los informes en AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION (respuesta con formato válido).
2. Nivel 1: calidad, caja y balance = pasa, y precio = pasa o dudoso.
3. Nivel 2: ninguno de calidad, caja y balance es no_pasa ni no_aplica; al menos dos de los tres son pasa; precio = pasa o dudoso.
4. Encaje no cuenta (nunca elimina). El veredicto del cribado se muestra y no entra en el criterio.
5. Finalistas propuestos = nivel 1 + nivel 2. Es una propuesta mecánica, no una recomendación.

## Finalistas propuestos

| Nivel | Empresa | Calidad | Caja | Balance | Precio | Veredicto del cribado (informativo) | Ejecución |
|---|---|---|---|---|---|---|---|
| 1 | FW_Thorpe | pasa | pasa | pasa | dudoso | estudiar_a_fondo | 44502520327 |
| 2 | Azkoyen | dudoso | pasa | pasa | dudoso | estudiar_a_fondo | 44413758195 |
| 2 | Betsson | dudoso | pasa | pasa | dudoso | estudiar_a_fondo | 44413758195 |
| 2 | CocaCola | pasa | dudoso | pasa | dudoso | estudiar_a_fondo | 44502520327 |
| 2 | Moury | dudoso | pasa | pasa | dudoso | estudiar_a_fondo | 44509331308 |
| 2 | Spie | dudoso | pasa | pasa | dudoso | estudiar_a_fondo | 44512238939 |
| 2 | Strabag | dudoso | pasa | pasa | dudoso | estudiar_a_fondo | 44512238939 |
| 2 | Tupras | dudoso | pasa | pasa | dudoso | faltan_datos | 44515220408 |

## Todas las empresas leídas

| Empresa | Estado | Calidad | Caja | Balance | Precio | Encaje | Veredicto del cribado | Nivel |
|---|---|---|---|---|---|---|---|---|
| AAK | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | dudoso | pasa | no_pasa | no_aplica | vigilar | — |
| Aarsleff | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | dudoso | pasa | no_pasa | no_aplica | vigilar | — |
| ABB | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | pasa | pasa | pasa | no_pasa | no_aplica | vigilar | — |
| Acomo | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | dudoso | no_pasa | dudoso | no_aplica | descartar | — |
| Airbus | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | pasa | dudoso | pasa | no_pasa | no_aplica | vigilar | — |
| AirtelAfrica | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | pasa | dudoso | pasa | no_pasa | no_aplica | vigilar | — |
| Andina | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | pasa | pasa | pasa | no_pasa | no_aplica | vigilar | — |
| Antofagasta | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | dudoso | pasa | dudoso | no_aplica | vigilar | — |
| Arcadis | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | pasa | pasa | no_pasa | no_aplica | vigilar | — |
| ASML | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | pasa | pasa | pasa | no_pasa | no_aplica | vigilar | — |
| Azkoyen | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | pasa | pasa | dudoso | no_aplica | estudiar_a_fondo | 2 |
| BC_Speakers | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | dudoso | pasa | no_pasa | no_aplica | vigilar | — |
| Berkosan | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | no_pasa | pasa | dudoso | no_aplica | descartar | — |
| BESI | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | pasa | pasa | no_pasa | no_aplica | vigilar | — |
| Betsson | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | pasa | pasa | dudoso | no_aplica | estudiar_a_fondo | 2 |
| Bioventix | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | pasa | pasa | pasa | no_pasa | no_aplica | vigilar | — |
| Borgestad | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | no_pasa | dudoso | dudoso | dudoso | no_aplica | descartar | — |
| Bossa | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | no_pasa | dudoso | dudoso | dudoso | no_aplica | descartar | — |
| Campine | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | dudoso | pasa | dudoso | no_aplica | vigilar | — |
| Carriage | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | pasa | no_pasa | no_pasa | no_aplica | descartar | — |
| Chewy | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | pasa | pasa | no_pasa | no_aplica | vigilar | — |
| CocaCola | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | pasa | dudoso | pasa | dudoso | no_aplica | estudiar_a_fondo | 2 |
| Ege_Gubre | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | dudoso | pasa | no_pasa | no_aplica | vigilar | — |
| Ege_Profil | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | dudoso | pasa | dudoso | no_aplica | estudiar_a_fondo | — |
| Elia | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | no_pasa | dudoso | dudoso | no_aplica | descartar | — |
| Excellence | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | no_pasa | dudoso | pasa | no_pasa | no_aplica | descartar | — |
| Ferrari | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | pasa | pasa | pasa | no_pasa | no_aplica | vigilar | — |
| Ferrovial | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | dudoso | pasa | dudoso | no_aplica | faltan_datos | — |
| Frontera | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | dudoso | dudoso | dudoso | no_aplica | faltan_datos | — |
| FW_Thorpe | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | pasa | pasa | pasa | dudoso | no_aplica | estudiar_a_fondo | 1 |
| Golar | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | no_pasa | no_pasa | no_aplica | no_aplica | descartar | — |
| Grupa | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | no_pasa | no_pasa | dudoso | no_pasa | no_aplica | descartar | — |
| Gubre_Fabrikalari | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | dudoso | pasa | dudoso | no_aplica | demasiado_dificil | — |
| Hal | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | dudoso | pasa | dudoso | no_aplica | vigilar | — |
| Heidelberg | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | pasa | pasa | no_pasa | no_aplica | vigilar | — |
| Heijmans | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | dudoso | pasa | no_pasa | no_aplica | vigilar | — |
| HelloFresh | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | no_pasa | no_pasa | pasa | no_aplica | no_aplica | descartar | — |
| Hermes | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | pasa | pasa | pasa | no_pasa | no_aplica | vigilar | — |
| Hitachi | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | pasa | pasa | no_pasa | no_aplica | vigilar | — |
| Hubbell | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | pasa | pasa | dudoso | no_pasa | no_aplica | vigilar | — |
| Indeks_Indes | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | no_pasa | dudoso | pasa | dudoso | no_aplica | descartar | — |
| Inditex | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | pasa | pasa | pasa | no_pasa | no_aplica | vigilar | — |
| Indra | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | dudoso | pasa | no_pasa | no_aplica | vigilar | — |
| Intuitive | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | pasa | pasa | pasa | no_pasa | no_aplica | vigilar | — |
| Italian_Wines | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | dudoso | pasa | pasa | no_aplica | estudiar_a_fondo | — |
| JetBlue | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | no_pasa | no_pasa | no_pasa | no_aplica | no_aplica | descartar | — |
| Kongsberg | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | pasa | dudoso | pasa | no_pasa | no_aplica | vigilar | — |
| Kopparbergs | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | pasa | pasa | no_pasa | no_aplica | vigilar | — |
| Leonardo | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | pasa | pasa | no_pasa | no_aplica | vigilar | — |
| Lifco | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | pasa | pasa | pasa | no_pasa | no_aplica | vigilar | — |
| Lifeservicesgroup | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | no_pasa | no_pasa | no_pasa | no_aplica | no_aplica | descartar | — |
| Limes | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | dudoso | pasa | no_pasa | no_aplica | vigilar | — |
| London_Security | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | pasa | pasa | pasa | no_pasa | no_aplica | vigilar | — |
| LOreal | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | pasa | pasa | pasa | no_pasa | no_aplica | vigilar | — |
| LVMH | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | pasa | pasa | pasa | no_pasa | no_aplica | vigilar | — |
| Mavi | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | dudoso | pasa | no_pasa | no_aplica | vigilar | — |
| MercadoLibre | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | dudoso | dudoso | dudoso | no_aplica | demasiado_dificil | — |
| Methanex | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | no_pasa | dudoso | dudoso | dudoso | no_aplica | descartar | — |
| MLP_Saglik | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | dudoso | pasa | dudoso | no_aplica | faltan_datos | — |
| Mo-BRUK | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | dudoso | pasa | no_pasa | no_aplica | vigilar | — |
| Moncler | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | pasa | pasa | pasa | no_pasa | no_aplica | vigilar | — |
| Moury | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | pasa | pasa | dudoso | no_aplica | estudiar_a_fondo | 2 |
| Naturelgaz | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | pasa | pasa | no_pasa | no_aplica | vigilar | — |
| Neochim | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | no_pasa | no_pasa | pasa | dudoso | no_aplica | descartar | — |
| Nike | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | dudoso | pasa | no_pasa | no_aplica | vigilar | — |
| NKT | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | dudoso | pasa | dudoso | no_aplica | vigilar | — |
| nVent | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | pasa | pasa | no_pasa | no_aplica | vigilar | — |
| Oil-Dri | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | dudoso | pasa | no_pasa | no_aplica | vigilar | — |
| Omer | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | dudoso | pasa | dudoso | no_aplica | estudiar_a_fondo | — |
| Oyak | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | dudoso | pasa | dudoso | no_aplica | vigilar | — |
| Pandora | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | pasa | pasa | no_pasa | no_aplica | vigilar | — |
| Parex | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | no_pasa | dudoso | dudoso | dudoso | no_aplica | descartar | — |
| Petrobras | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | no_pasa | dudoso | pasa | dudoso | no_aplica | descartar | — |
| Petsathome | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | dudoso | pasa | no_pasa | no_aplica | vigilar | — |
| Prysmian | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | pasa | dudoso | no_pasa | no_aplica | vigilar | — |
| Puigbrands | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | pasa | pasa | pasa | no_pasa | no_aplica | vigilar | — |
| Quanta | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | pasa | pasa | no_pasa | no_aplica | vigilar | — |
| Rational | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | pasa | pasa | pasa | no_pasa | no_aplica | vigilar | — |
| Rentokil | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | pasa | pasa | no_pasa | no_aplica | vigilar | — |
| Rheinmetall | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | dudoso | pasa | no_pasa | no_aplica | vigilar | — |
| Roche | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | pasa | pasa | pasa | no_pasa | no_aplica | vigilar | — |
| Rovi | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | pasa | pasa | no_pasa | no_aplica | vigilar | — |
| Royal_BAM | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | no_pasa | dudoso | pasa | dudoso | no_aplica | descartar | — |
| RStahl | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | no_pasa | no_pasa | no_pasa | dudoso | no_aplica | descartar | — |
| Salzgitter | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | no_pasa | no_pasa | dudoso | no_aplica | no_aplica | descartar | — |
| Sarantis | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | pasa | pasa | no_pasa | no_aplica | vigilar | — |
| Schneider | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | pasa | pasa | dudoso | no_pasa | no_aplica | vigilar | — |
| Seche | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | no_pasa | dudoso | dudoso | no_pasa | no_aplica | descartar | — |
| Siemens | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | no_pasa | pasa | no_pasa | no_aplica | descartar | — |
| Sika | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | pasa | dudoso | no_pasa | no_aplica | vigilar | — |
| Sony | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | dudoso | pasa | no_pasa | no_aplica | vigilar | — |
| Spectra | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | pasa | pasa | no_pasa | no_aplica | vigilar | — |
| Spie | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | pasa | pasa | dudoso | no_aplica | estudiar_a_fondo | 2 |
| SQM | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | dudoso | pasa | dudoso | no_aplica | faltan_datos | — |
| Strabag | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | pasa | pasa | dudoso | no_aplica | estudiar_a_fondo | 2 |
| Sulzer | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | pasa | dudoso | pasa | no_pasa | no_aplica | vigilar | — |
| Sweco | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | pasa | pasa | pasa | no_pasa | no_aplica | vigilar | — |
| TE_Connectivity | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | pasa | pasa | pasa | no_pasa | no_aplica | vigilar | — |
| Technogym | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | pasa | pasa | pasa | no_pasa | no_aplica | vigilar | — |
| Tessenderlo | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | no_pasa | dudoso | dudoso | dudoso | no_aplica | descartar | — |
| Thales | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | pasa | pasa | pasa | no_pasa | no_aplica | vigilar | — |
| Tupras | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | pasa | pasa | dudoso | no_aplica | faltan_datos | 2 |
| Upsales | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | pasa | pasa | no_pasa | no_aplica | vigilar | — |
| Valeura | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | no_pasa | dudoso | pasa | dudoso | no_aplica | descartar | — |
| Veolia | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | dudoso | dudoso | dudoso | no_aplica | faltan_datos | — |
| Vidrala | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | pasa | pasa | pasa | no_pasa | no_aplica | vigilar | — |
| Viscofan | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | pasa | dudoso | pasa | no_pasa | no_aplica | vigilar | — |
| Vitec | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | pasa | pasa | no_pasa | no_aplica | vigilar | — |
| Volution | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | pasa | pasa | pasa | no_pasa | no_aplica | vigilar | — |
| Vossloh | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | no_pasa | dudoso | dudoso | no_pasa | no_aplica | descartar | — |
| WEG | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | pasa | pasa | pasa | no_pasa | no_aplica | vigilar | — |
