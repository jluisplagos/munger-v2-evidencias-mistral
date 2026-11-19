# Cribado · Vitec

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-11-07 |
| Tarea | cribado-44515220408-vitec |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 372787233073fe147d75b9ba3f9a7196798bae0ca546907b1d82be42346a84a7 |
| Huella del envío (bundle_sha256) | e6e9e17c177b2102dc1f35304d7df0b5b18c4922e4b1dcf426ec0c277aaae3f6 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 090377c66c989ea2d2b71da597c2ddf0d2c06115731ab8f1372687c6c35a181d |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 136187 tokens |
| Reserva estimada antes de llamar | USD 1.200108 |
| Uso de tokens | entrada 60889, salida 4307 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.329696; cota 0.329696 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Vitec/Vitec_respuesta.md | 19e2ba6a4c76a774537576291d809144a3fad14b23aa639c3d439b7a1b48c11d | 33977 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Vitec/Vitec_evaluada.xlsx#Análisis | d009640ecd79cb9df7eff619fe7ca8a337b0a61a556570e40399b6cc4a0ac490 | 24450 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Vitec/Vitec_evaluada.xlsx#Control maestro | d04ac9e783f79f57412bf7ed9a1c0a532d145c9b3f125a62f36bcc323b964b53 | 56998 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `vigilar` · DCF de la plantilla aplica: `si`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | pasa |
| balance | pasa |
| precio | no_pasa |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51: arrendamientos 181,6 MSEK a 30-sep-2026, incluidos en la deuda total Análisis!C54 = 3736.7; se excluyen del cociente de deuda.


### Tipo de negocio y motor

    Consolidador de software vertical para nichos (49 unidades), con ingresos recurrentes por suscripción y crecimiento basado en adquisiciones
    El DCF de caja libre de la plantilla sobre la caja normalizada del accionista, con crecimiento solo autofinanciado, porque el flujo es recurrente; las adquisiciones habría que valorarlas aparte por su retorno sobre el capital invertido.

### calidad

    Es software vertical recurrente (88 % de las ventas, margen EBITA del 29,0 % R12), pero el ROCE bajó del 14 % al 10 % y el ROIC después de impuestos (7,7 %) iguala el coste de capital de la propia empresa, con un crecimiento orgánico del -0,1 % en 2025 y márgenes comprimiéndose: hay calidad en las unidades, pero no se ve en el retorno del grupo.
    Dato clave: Análisis!C24 = 0.1

### caja

    Convierte bien el beneficio en caja (caja operativa/beneficio neto de 2,34 en Análisis!C26) y la caja libre del accionista, después de arrendamientos, pasó de 65,6 en 2016 a 576,8 en 2025 y a 610,5 R12, con una base normalizada de 422,8, aunque las compras consumieron unas 3,4 veces la caja libre acumulada de 2021-2025.
    Dato clave: Análisis!C52 = 422.8

### balance

    La 2,63x de la hoja (Análisis!C33) incluye 181,6 de arrendamientos y 643,8 de aplazados; sin arrendamientos, la deuda neta de 3.005,7 frente a un EBITDA R12 de 1.457,8 menos 82,1 de principal de arrendamientos (≈1.376) da ≈2,2x, o ≈2,65x con aplazados, lo que es aceptable para un negocio con un 88 % de ingresos recurrentes, aunque la deuda neta equivale a ≈4,9 veces la caja libre R12 y vence un bloque de ≈2.773 en febrero de 2029.
    Dato clave: Control maestro!N36 = 3005.7 (deuda neta reportada, sin arrendamientos ni pagos aplazados)

### precio

    La cotización de 299,8 SEK supera el valor ponderado de 188,5 (margen del -59 %), el precio de Sí de unos 108 e incluso el escenario bueno de 295,6; con r del 7 % el ponderado solo llega a 269,1 y el precio exige un crecimiento del 10,8 % anual (Análisis!C86).
    Dato clave: Análisis!C43 = 188.472080318341 frente a Análisis!C37 = 299.8

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja solo da un plan de etapa 1 (C104), así que este filtro no se evalúa ni elimina.
    Dato clave: Análisis!C104 = 0% · Watchlist (dato de la etapa 1, no heredado)

### Qué lo cambiaría

    - Una cotización por debajo del valor ponderado de 188,5 SEK (Análisis!C83), y más aún cerca del escenario malo de 108,4 SEK, pasaría el filtro de precio y llevaría a estudiar a fondo.
    - Un ROCE R12 por encima del 12 % con crecimiento orgánico positivo en 2026 aclararía la calidad a favor.
    - Nuevas ampliaciones de capital por debajo de 300 SEK, deterioros de fondo de comercio no ligados a earn-outs o una deuda neta con aplazados por encima de 3,5x EBITDA llevarían a descartar.

### Qué falta

    - EBITDA exacto después de alquileres: no consta el interés de arrendamientos y el EBITDA R12 de 1.457,8 es derivado, con una diferencia de unos 60 sin conciliar frente al implícito de la empresa (Control maestro!N36).
    - Margen y retorno por unidad de negocio, retención de la base recurrente y covenants del crédito renovable y del programa MTN: no constan en el paquete.
    - Pequeñas discrepancias en las fuentes: la respuesta fecha el análisis el 15-nov-2026 frente a la hoja (2026-11-07), da unos 26.500 clientes frente a los ~28.000 de Control maestro!M19, y no se sabe si la SBC de 18,3 se resta dos veces del FCF base.

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

