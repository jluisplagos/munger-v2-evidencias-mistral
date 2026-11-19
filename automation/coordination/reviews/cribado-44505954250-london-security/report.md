# Cribado · London_Security

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-31 |
| Tarea | cribado-44505954250-london-security |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 939aa4407c07f2c5047bcb6bd2460e9593e57eb823d115f297c01f39cfcc8267 |
| Huella del envío (bundle_sha256) | f950ab74ef974913dbf841fbbb1b8ccab62c4dad68a2a75051f2245bf55e7db7 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | b081358beff6785735ea28c1efb61e13f13ff64a1b2d7a3da1573431102273ae |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 130080 tokens |
| Reserva estimada antes de llamar | USD 1.17568 |
| Uso de tokens | entrada 58528, salida 3403 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.302172; cota 0.302172 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/London_Security/London_Security_respuesta.md | 819e4dfc65ea8983f63914ec08c4d486ce9d974fd0ddc0561ab77a82f97b9bb6 | 31867 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/London_Security/London_Security_evaluada.xlsx#Análisis | 1a3b603aca9014b3684c8f509f665e87dcf59cd11c01239c627a3ae6c257f891 | 23596 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/London_Security/London_Security_evaluada.xlsx#Control maestro | c30c2537f73b749cfc7aae368a675cac4f1dd128e3b30242b3ef45c95609722d | 53667 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `vigilar` · DCF de la plantilla aplica: `si`

| Filtro | Resultado |
|---|---|
| calidad | pasa |
| caja | pasa |
| balance | pasa |
| precio | no_pasa |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51 = 7.513 (mm £ a 30-jun-2026; está incluido en Análisis!C54 = 7.821)


### Tipo de negocio y motor

    Servicios recurrentes y venta de equipos de protección contra incendios (revisión, venta, instalación y alquiler) en ocho países europeos; negocio estable de cumplimiento normativo, con caja neta y un accionista de control.
    El DCF de caja libre de la plantilla, porque es un negocio estable de servicios recurrentes, con poca inversión y caja neta, sumando aparte el exceso de caja no operativa.

### calidad

    El negocio se entiende, con demanda de cumplimiento normativo y un ROCE antes de impuestos de 0,183 (estable en 0,18-0,20 durante diez años), pero el margen operativo ha caído del 18,2 % al 13,4 % (Análisis!C27 «Comprimiendo») y el 98,85 % está en manos del controlador; el «DESCARTAR · demasiado difícil» de Análisis!A6 viene de C13 (precio), no de que el negocio no se entienda.
    Dato clave: Análisis!C24 = 0.183

### caja

    La caja libre base (media de 3 años, ya neta del principal de arrendamientos de 2,74) es de 18,26 mm £ y la caja operativa equivale a 1,327 veces el beneficio, aunque crece despacio (≈3,3 % anual) y el LTM de 23,94 está inflado por circulante.
    Dato clave: Análisis!C52 = 18.26

### balance

    Sin arrendamientos, la deuda son solo 0,308 mm £ de préstamos frente a 54,823 mm £ de caja, con una deuda neta/EBITDA ≈ −1,27x (EBITDA pre-NIIF 16 aproximado de 42,86 en Control maestro!N36); la cifra de Análisis!C33 = −1,01 incluye arrendamientos y no sirve tal cual, pero ambas indican caja neta amplia en un negocio estable.
    Dato clave: Análisis!C54 = 7.821 menos arrendamientos Control maestro!M51 = 7.513 → préstamos 0.308; Análisis!C53 = 54.823

### precio

    La cotización de 36,5 £ está muy por encima del precio de Sí (escenario malo, 19,54 £) y del valor ponderado (27,77 £, margen −31 %), y exige un crecimiento de la caja libre del 8,19 %, superior al del escenario bueno; incluso a r = 7 % el ponderado (38,65 £) apenas supera el precio y el precio de Sí (≈25 £) sigue lejos.
    Dato clave: Análisis!B78 = 19.5420750821087

### encaje

    El paquete no trae la cartera; solo consta como dato una capitalización de 447,45 mm £ con un free float ≈1,15 %, que condiciona la ejecución pero no elimina en el cribado.
    Dato clave: Análisis!C41 = 447.45

### Qué lo cambiaría

    - Un precio ejecutable de ≈19,5 £ o menos (Análisis!B78), o cercano al valor ponderado de 27,8 £: pasaría a estudiar a fondo.
    - Un margen operativo por debajo del 12 % dos años seguidos, o un ROCE bruto por debajo del 15 %: llevaría a descartar.
    - Una compra grande y cara pagada con la caja, o una oferta de exclusión de minoritarios a precio bajo por parte del controlador.

### Qué falta

    - Crecimiento orgánico y retención de clientes: la empresa no los publica, y son la prueba del foso y del escenario normal.
    - Precio ejecutable: 36,5 £ es un precio medio sin operaciones (Control maestro!J38), con un free float ≈1,15 %; falta una cotización en firme.
    - El EBITDA sin NIIF 16 (≈42,86) es aproximado, con D&A LTM estimadas; además, la decisión del periodo del FCF base figura fechada el 09-nov-2026, después de la fecha de la hoja (31-oct-2026).

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

