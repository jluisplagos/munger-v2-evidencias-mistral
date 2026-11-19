# Cribado · Hubbell

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-09 |
| Tarea | cribado-44502520327-hubbell |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 0aea1044e65815289f4aa74ba4b18d66baf6a251941bdaa30a403979ad7970dc |
| Huella del envío (bundle_sha256) | b10bb8bb8e20d6cc203b1fd41905c5d40b337b78c87951c0abd27c7832c43fef |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | dae489e762e5ddf18f8660dfaa48ee8f78b9a6c8ff1e808e675f1c03230a7f2f |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 129162 tokens |
| Reserva estimada antes de llamar | USD 1.172008 |
| Uso de tokens | entrada 58666, salida 3914 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.312944; cota 0.312944 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Hubbell/Hubbell_respuesta.md | 0c26e9f29cb7fc3ba53b0c8f7c3bea7efbf71f4473899d7eb55cfa5feed4f614 | 30250 |
| cambios_v2 | EMPRESAS_LOTES_COMPLETOS/Hubbell/Hubbell_cambios_v2.md | d3f04c18924f20236da7809548db07719c3046909a1398b7e33b73ea51d5daba | 2969 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Hubbell/Hubbell_evaluada.xlsx#Análisis | 2d52a42c6ddf2bed064ff08f232cd6b2df1aab19e1a3530396b864df72a86d99 | 23003 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Hubbell/Hubbell_evaluada.xlsx#Control maestro | 12dc3cdf3004b71b33c593d6f7ec136c9e5b2865b6c2e15cd4a5f1a379039d2c | 51905 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `vigilar` · DCF de la plantilla aplica: `si`

| Filtro | Resultado |
|---|---|
| calidad | pasa |
| caja | pasa |
| balance | dudoso |
| precio | no_pasa |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51 = 184.0 (arrendamientos operativos a 30-jun-2026, excluidos de la deuda; el alquiler ya va dentro del CFO y del EBITDA)


### Tipo de negocio y motor

    Industrial de componentes eléctricos y de red (Utility Solutions, 63 %, y Electrical Solutions), vendidos sobre todo a distribuidores y eléctricas de EE. UU.; un negocio bastante estable con algo de ciclo y crecimiento en parte comprado.
    El DCF de caja libre de la plantilla, recalculado con un año completo de NSI en el flujo y los intereses de su deuda para corregir la incoherencia de perímetro que señala C62, y contrastado con un margen de ciclo medio.

### calidad

    Es un negocio que se entiende, con ROIC del 17–19 % en FY22–FY25 y del 12,4 % pro forma con NSI (por encima del 9 %) y margen ajustado del 22,7 %, aunque ese margen solo lleva tres años, las compras son cada vez más caras y la hoja marca DESCARTAR · demasiado difícil, un veredicto de etapa 1 del que discrepo porque su C11 y su C12 dicen Sí.
    Dato clave: Análisis!C24 = 0.124

### caja

    Convierte el beneficio en caja de forma recurrente: CFO/beneficio neto de 1,22 en cinco años (C26), FCF de la empresa al alza de 423,5 (2021) a 901,4 LTM (C40) y una caja libre base tras SBC de 770,2, con capex de 167,1 y SBC de solo un 3,7 % del FCF.
    Dato clave: Análisis!C52 = 770.2

### balance

    Sin arrendamientos, la deuda de 5.372,6 deja una deuda neta de 4.977,9 sobre un EBITDA LTM de 1.493,2 que ya resta el alquiler: 3,33x (unas 6,5 veces la caja libre base de 770,2); es alta para un negocio con algo de ciclo, aunque la pro forma con NSI es de 2,97x, los vencimientos están repartidos (2027: 300; 2028: 1.050) y el revolver de 1.000 está sin disponer, de modo que queda dudoso hasta ver el desapalancamiento.
    Dato clave: Análisis!C54 = 5372.6

### precio

    La cotización de 475,4 está muy por encima del precio de Sí que da la hoja (203,6, frente al ≈205 que estimaba la respuesta; manda la hoja), del valor ponderado de 304,5 y hasta del escenario bueno, de 425,4; el precio exige un crecimiento del 12,2 % (C86), con r al 7 % el ponderado sigue en 451,2 y, aunque el FCF base omite NSI (run-rate de 946–971), la conclusión no cambia.
    Dato clave: Análisis!C78 = 203.6010833075

### encaje

    El paquete no trae la cartera y la hoja solo registra decisiones de cartera de etapa 1 (C103 = No), que aquí no se usan; este filtro no elimina.
    Dato clave: Análisis!C103 = No

### Qué lo cambiaría

    - Una cotización en torno al precio de Sí de la hoja (≈203,6 USD) o por debajo, con la tesis intacta.
    - Un margen operativo ajustado por debajo del 18 % sin una caída fuerte de volumen, que haría no pasar la calidad.
    - Una deuda neta/EBITDA sin arrendamientos por encima de 4x u otra compra grande antes de desapalancar, que haría no pasar el balance.

### Qué falta

    - FCF y EBITDA de un año completo con NSI y los intereses de su deuda (el FCF base de 770,2 y el EBITDA LTM solo recogen unos 22 días de NSI).
    - Qué vende NSI y qué retorno da sobre los aproximadamente 3.008 pagados.
    - Propiedad de dirección y consejo según el proxy 2026 (Análisis!C96 vacía).

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [
          "Filtro balance: motivo de más de 400 caracteres."
        ],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

