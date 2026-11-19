# Cribado · Omer

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-11-01 |
| Tarea | cribado-44509331308-omer |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | d21b7414abb26bdf95f5748e41ed943da9b5ca331889c9cbf9c740873974ccda |
| Huella del envío (bundle_sha256) | 9d7d141c33ee208c8caa48591d68279ba99888d8e95e445652e919d8ef372e6d |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 998db7f275de2bcfa6a4988dab5993138d3012562d819113ec9be537777c6d1b |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 128668 tokens |
| Reserva estimada antes de llamar | USD 1.170032 |
| Uso de tokens | entrada 58454, salida 4279 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.319396; cota 0.319396 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Omer/Omer_respuesta.md | c4aa4e804549308f44226b4d5461c23c1192cbf0675573e88cadf47ff7c832ae | 30976 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Omer/Omer_evaluada.xlsx#Análisis | 842ea31b1ad9d3a02ce2059595811190d3b6b214b434802a9dac7e92309be8f5 | 23655 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Omer/Omer_evaluada.xlsx#Control maestro | 657c55f755310fa21b0063e94cc92cf6f22b97006db0dd786e10fa6165304558 | 53273 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `estudiar_a_fondo` · DCF de la plantilla aplica: `dudoso`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | dudoso |
| balance | pasa |
| precio | dudoso |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51: leasing financiero OIC 17 = 0,576 mm (incluido en la deuda bruta Análisis!C54 = 3.964 y excluido en el cociente). Los alquileres operativos de naves a sociedades vinculadas (~1,65 mm al año, Control maestro!M47) no tienen pasivo en balance.


### Tipo de negocio y motor

    Proveedor industrial por proyectos (interiores, cabinas de aseo y puertas de aluminio para fabricantes de trenes), cíclico y con circulante intensivo.
    Caja libre de ciclo medio (FCF normalizado a lo largo de un ciclo de pedidos, que incluya un año como 2016–2018), con la caja neta sumada aparte.

### calidad

    El ROIC sin caja es del 28,8 % y el margen EBITDA antes de provisiones se mantiene estable en torno al 22–23 % desde 2022, pero el ROIC incremental FY21→FY25 es solo del 1,7 %, no constan clientes ni competidores y el EBITDA ya cayó un 72 % en 2016–2018; el negocio se entiende, pero la ventaja no está demostrada (la etapa 1 lo lleva a «demasiado difícil», y aquí queda como duda que el estudio puede resolver).
    Dato clave: Análisis!C24 = 0.288

### caja

    La conversión es sana (CFO/beneficio 0,99 en FY21–FY25, Análisis!C26) y el FCF base es positivo (7,44 mm), pero el FCF reportado es 13,8 / −9,8 / 11,6 / 2,3 / 8,4 mm porque el circulante absorbió 19,1 mm en cinco años; con un ratio de 0,80 en FY22–25, la recurrencia está por demostrar.
    Dato clave: Análisis!C52 = 7.44

### balance

    Sin arrendamientos, la deuda es de 3,388 mm frente a 32,075 mm de caja (Análisis!C53), es decir, caja neta de unos 28,7 mm (−1,48x el EBITDA LTM de 19,32 mm, que ya resta los alquileres operativos según OIC), sin covenants encontrados; queda pendiente el factoring pro soluto de Hitachi, que la hoja estima en el peor caso en −0,4x.
    Dato clave: Control maestro!N51 = 3.388 (deuda financiera bruta sin leasing, mm; texto «Sin leasing 3,388»)

### precio

    La hoja no fija precio de Sí. La cotización de 3,46 € está un 15 % por encima del escenario malo (3,00 €, que coincide con el ≈3,0 € de la respuesta), pero por debajo del valor ponderado de 5,16 € y del valor con r+2 pts (4,02 €). Como el DCF depende de un FCF base volátil por el circulante (7,44 frente a 10,8 mm normalizado), hace falta un motor de caja de ciclo medio para concluir.
    Dato clave: Análisis!B78 = 2.99718142362823

### encaje

    El paquete no trae la cartera; solo consta que es un valor pequeño (99,08 mm de capitalización) y poco líquido (unas 15.000 acciones al día, Control maestro!N38), lo que no elimina en el cribado.
    Dato clave: Análisis!C41 = 99.08

### Qué lo cambiaría

    - Un desglose de ventas que muestre que un solo constructor concentra la mayoría de las ventas, o competidores con cuota que presionen el margen (pasaría a descartar).
    - Un margen EBITDA antes de provisiones por debajo del 20 % dos semestres seguidos con el backlog por debajo de 130 mm (descartar).
    - Un saldo de factoring o partidas asimilables a deuda que eliminen la caja neta de ~28 mm, o una cotización por debajo de 3,00 € (Análisis!B78), que movería el filtro de precio.

### Qué falta

    - Ventas por cliente, concentración y competidores con cuota: el paquete no los trae y son materiales para la calidad.
    - Saldo cedido en factoring pro soluto de Hitachi Rail, no publicado desde FY24: puede reducir la caja neta efectiva.
    - Precio de Sí explícito en la hoja (no consta) y resultados 9M-2026 con backlog, que se publican el 16/11/2026, después de la fecha de corte.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [
          "Filtro calidad: motivo de más de 400 caracteres."
        ],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

