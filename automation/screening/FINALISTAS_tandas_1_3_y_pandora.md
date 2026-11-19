# Segunda vuelta del universo · finalistas propuestos (criterio mecánico)

- Rama de registro: `origin/automatizacion/claude-api-piloto-registro` en `9e1868d1a0dd9727ead212e1d3f28063146a44bb`.
- Ejecuciones del cribado leídas: 44406828081, 44413758195, 44502520327, 44505954250. La ejecución 44509331308 (tanda 4, 12 de 20 empresas publicadas al leer) no se lee: las tandas 4 a 6 se añadirán cuando terminen.
- Empresas leídas: 61; con resultado utilizable: 61.
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
| Pandora | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | dudoso | pasa | pasa | no_pasa | no_aplica | vigilar | — |
