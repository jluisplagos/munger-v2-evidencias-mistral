# Cribado · Inditex

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-09 |
| Tarea | cribado-44505954250-inditex |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | a8d146d376f5bebac40e7456739d9e3901b510c2c337a6e022e18e1c28f1d009 |
| Huella del envío (bundle_sha256) | aa5a99472012c8e8da069e8ae08e717a51b34b18e8912cb325a8634320591775 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | ff21065b3783970c6d0f496e65f30cdd150ae9164f5a2ee2194ba9fd106eba80 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 135746 tokens |
| Reserva estimada antes de llamar | USD 1.198344 |
| Uso de tokens | entrada 62371, salida 3402 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.317524; cota 0.317524 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Inditex/Inditex_respuesta.md | 77afb99b2d1a148c72290183e5203d7857a4a4fe2c190915638476089c41829b | 32195 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Inditex/Inditex_evaluada.xlsx#Análisis | fe8d85882ac119152d2836ccae901edee2935b3c17e2fea31df182fc68d55920 | 22574 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Inditex/Inditex_evaluada.xlsx#Control maestro | 18d2708761a50fb1cb7526bd4a0465b3b092e415d5e3e0403b278f579b3b96f1 | 59983 |

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

    Control maestro!M51 = 6197 (pasivo por arrendamientos a 31-jul-2026: no corriente 4.549 + corriente 1.648; 5.933 a 31-ene-2026); fuera del cociente de deuda.


### Tipo de negocio y motor

    Distribución minorista de moda verticalmente integrada (diseño, aprovisionamiento, logística, tiendas y online), negocio estable de consumo discrecional con caja neta.
    El DCF de caja libre de la plantilla es adecuado para este negocio estable, autofinanciado y con caja neta, con FCF ya neto de arrendamientos y SBC.

### calidad

    Minorista de moda integrado y comprensible con un ROCE del 40 % (28-40 % en nueve de diez años), margen bruto estable o al alza del 55,8 % al 58,3 % y sin dependencia de pocos clientes; discrepo del «DESCARTAR · demasiado difícil» de Análisis!A6, que nace de C13 = No (valor claro sin modelo) y C20, ambos ligados al precio y no a la calidad del negocio.
    Dato clave: Análisis!C24 = 0.4

### caja

    El FCF base, ya neto de arrendamientos (C49 = 1.790) y SBC, es de 4.761 mm, el FCF publicado fue positivo en 2021-2025 (3.638-5.062 mm) y la conversión CFO/beneficio de 1,63x baja a 1,28x al restar los alquileres, aún sana; el LTM de C40 = 5.819 es más alto por un circulante casi neutro (−20) y no lo uso como base.
    Dato clave: Análisis!C52 = 4761

### balance

    La deuda/EBITDA de la hoja (Análisis!C33 = −0,36x) y la deuda de Análisis!C54 = 6.198 incluyen arrendamientos y no sirven tal cual; recalculada sin ellos, la deuda financiera es 1 mm frente a 10.399 mm de caja e IFC, una caja neta de 10.398 mm (≈−1,1x sobre un EBITDA LTM tras alquiler de ≈9.796 = 11.666 − 1.870, cálculo propio), que pasa incluso descontando el dividendo pendiente de ≈2.724 mm; la respuesta usa cifras a 31-ene-2026 (caja 5.276, deuda 2) y manda la hoja a 31-jul-2026.
    Dato clave: Control maestro!M51 = deuda financiera 1 mm (sin arrendamientos, 31-jul-2026); caja 4.361 + IFC 6.038 → caja neta 10.398 (Control maestro!M82)

### precio

    La cotización de 52,84 € (Análisis!C37) es unas 2,5 veces el precio de Sí de ≈21,4 € (mín. del malo 21,44 y ¾ del ponderado 30,70 = 23,02), supera incluso el escenario bueno (44,80 €) y el ponderado con r al 7 % (45,37 €, Análisis!C91), y el precio exige un crecimiento del FCF del 12,9 % anual (Análisis!C86), por encima del bueno del 10 %.
    Dato clave: Análisis!B78 = 21.4427736055568

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja solo aporta datos generales como una capitalización de 164.669 mm, así que este filtro no aplica ni elimina.
    Dato clave: Análisis!C41 = 164669

### Qué lo cambiaría

    - Una cotización por debajo de ≈23 € (zona del precio de Sí de 21,4 € y ¾ del ponderado de 23,02 €) con el negocio intacto pasaría a estudiar a fondo.
    - Un margen bruto por debajo del 55 % dos años seguidos sin causa externa, o un ROCE que caiga por debajo del 30 %, rebajaría la calidad y llevaría a descartar.
    - Un FCF de 2026-2027 sin capex extraordinario por encima de 5.500-6.000 mm elevaría el valor de los escenarios y acercaría el precio de Sí.

### Qué falta

    - Datos de cuota de mercado, crecimiento del mercado de moda por zona y competidores concretos: el paquete no los trae.
    - Financiación a proveedores a 31-jul-2026 no publicada en el 1S (1.335 mm a ene-2026), relevante para la caja neta realmente libre.
    - El EBITDA tras alquiler no figura en la hoja: la deuda neta/EBITDA sin arrendamientos (≈−1,1x) es un cálculo propio con EBITDA LTM 11.666 menos cuota de arrendamientos LTM 1.870.

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

