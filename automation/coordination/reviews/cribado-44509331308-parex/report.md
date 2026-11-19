# Cribado · Parex

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 27/10/2026 |
| Tarea | cribado-44509331308-parex |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 86212859579a59f4a333c2b3f6b243b77f40f491f1cf459a9f43ac90b105e8a9 |
| Huella del envío (bundle_sha256) | 82584cbcafd0c5d1aa52ae8d2346570b235244fa29680b038bc452eae3f18de4 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 1f0768ff1d9d1cd15e27515021ea6c1c77871ff9187ef9a57f50ecd2f9306e85 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 218329 tokens |
| Reserva estimada antes de llamar | USD 1.528676 |
| Uso de tokens | entrada 98991, salida 4081 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.477584; cota 0.477584 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Parex/Parex_respuesta.md | 3d96bbf5af549a2ff0743249eb18b0d287e3c26edb75d8a4c5471661f24cd4dd | 36203 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Parex/Parex_evaluada.xlsx#Análisis | 04ad1909b77e85830b0addd951dd15c81dcb2b1d73d0b0a4bd777cf13f23e066 | 23240 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Parex/Parex_evaluada.xlsx#Control maestro | b99517b9880b0b12fc8261f60c2efbc491c9c47a15b055a941c97b9822ab7cd9 | 136677 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `descartar` · DCF de la plantilla aplica: `no`

| Filtro | Resultado |
|---|---|
| calidad | no_pasa |
| caja | dudoso |
| balance | dudoso |
| precio | dudoso |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!N46 = 22.916 k$ (22,9 mm a 30/06/2026; corriente 5,188 + no corriente 17,728), fuera del cociente de deuda


### Tipo de negocio y motor

    Productor independiente de crudo (E&P, upstream) con todos sus activos en Colombia: cíclico, tomador de precio y con reservas finitas; ha duplicado su tamaño con la compra de los activos de Frontera financiada con deuda.
    Valor de las reservas probadas y probables (NAV de 1P/2P a precios de ciclo medio) neto de deuda y de desmantelamiento, contrastado con la caja de ciclo medio del grupo combinado, no un DCF con perpetuidad.

### calidad

    El negocio se entiende, pero no es de calidad: es tomador de precio y sin foso, con un ROCE del 12,4 % antes de impuestos y un ROIC del 8,1 % después de impuestos, por debajo del WACC de comparables del 14 %; el margen de netback se comprimió del 69,8 % al 52,7 % y 1.931 M$ de capex no sostuvieron la producción. Discrepo del ✓ de C11 solo en que entender no equivale a calidad, y no del «demasiado difícil» de la etapa 1, que confunde ciclo con no entender.
    Dato clave: Análisis!C24 = 0.124

### caja

    La conversión del beneficio es alta (CFO/beneficio de 1,71x en C26), pero la caja libre es inestable y decreciente: el free funds flow cae un 17 % anual entre 2021 y 2025, el FCF fue negativo en 2023 y en el T2 2026 (−1,6 M$), y la base de 64,4 mm no cubre los 66,9 M$ de cupones nuevos; el perímetro combinado aún no tiene un año completo.
    Dato clave: Análisis!C52 = 64.4

### balance

    Sin arrendamientos, la deuda neta es de 629,0 mm (792,3 de deuda menos 163,3 de caja), unas 1,1x el EBITDA de doce meses (1,10x en la versión pre-NIIF 16 aproximada de la hoja) y sin vencimientos antes de 2028, lo que es holgado para un negocio cíclico; pero equivale a unas 9,8x la caja libre base de 64,4 mm, la deuda se multiplicó por 24 en seis meses y los cupones de 66,9 M$ al año consumen esa caja, así que queda en duda.
    Dato clave: Análisis!C54 = 792.3

### precio

    La cotización de 21,03 $ está por encima incluso del escenario bueno de la hoja (19,68 $; ponderado 10,59 $, y 8,29–14,52 $ con r ±2 puntos), pero ese DCF de perpetuidad no aplica a reservas finitas y la hoja es anterior al T3 2026; con el FCF combinado de la etapa 1 el normal saldría por encima del precio, así que haría falta un valor de reservas (NAV 1P/2P) neto de deuda y desmantelamiento.
    Dato clave: Análisis!C37 = 21.03

### encaje

    El paquete no trae la cartera; solo consta una capitalización de 2.022,4 mm como dato de tamaño, sin nada concreto sobre encaje.
    Dato clave: Análisis!C41 = 2022.4

### Qué lo cambiaría

    - Reposición de reservas 2P ≥ 100 % con coste de hallazgo y desarrollo < 20 $/boe durante dos años seguidos (hoy 34,84 $/boe trienal frente a un netback de 35,52 $/boe).
    - ROIC después de impuestos sostenido por encima del 14 % de WACC de comparables en el perímetro combinado (hoy 8,1 %).
    - Prórroga del contrato de Quifa anunciada antes del 01/06/2027, junto con una producción y un FFO por acción del grupo que se mantengan o crezcan sin nuevas compras.

### Qué falta

    - El AIF de 2026 con el informe de reservas NI 51-101: 1P/2P por bloque, reposición y coste de hallazgo y desarrollo de fuente primaria (el trienal de 34,84 $/boe es de fuente secundaria), además del estado de la prórroga de Quifa.
    - Un ejercicio completo, o al menos el T3 2026 (06/11/2026), del grupo combinado tras Frontera, con su caja libre después de los cupones de 66,9 M$ al año.
    - Duda sobre las fuentes: la hoja fechada el 27/10/2026 recoge decisiones del «1-nov-2026» en C46, C47 y C50 y una producción del T3 2026 de 83.259 boe/d (fuente secundaria), ambas posteriores a la fecha de corte.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [
          "Filtro calidad: motivo de más de 400 caracteres.",
          "Filtro balance: motivo de más de 400 caracteres."
        ],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

