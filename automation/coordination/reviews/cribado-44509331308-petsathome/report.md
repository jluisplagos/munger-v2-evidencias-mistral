# Cribado · Petsathome

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-26 |
| Tarea | cribado-44509331308-petsathome |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 342b625ea98827a1509349e855cf94a0fba11c90a5c9a1cca54532efa40a0215 |
| Huella del envío (bundle_sha256) | 022906c211b8809499b734ca1aa80fde4adb6baa3024db72df61f24576c05acb |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 1a7e4fd997d791c4793337e178c76c907ac2150105e122a4142e603c3832ec99 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 176357 tokens |
| Reserva estimada antes de llamar | USD 1.360788 |
| Uso de tokens | entrada 80776, salida 5125 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.425604; cota 0.425604 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Petsathome/Petsathome_respuesta.md | acf235ae035bae518cc34be6f6ecbb24108b0d28bda3a371eaa87656690b0bb9 | 32518 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Petsathome/Petsathome_evaluada.xlsx#Análisis | 5c94eb75e32b0a23445b5018eaca348d47866d10dab4398a2bade746798f1021 | 23609 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Petsathome/Petsathome_evaluada.xlsx#Control maestro | ad4b52551643877120668eda03b8638f31a99f99e6d26bf8d825feb065accb5d | 98220 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `vigilar` · DCF de la plantilla aplica: `si`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | dudoso |
| balance | pasa |
| precio | no_pasa |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M36 = 338.8 (76,1 corriente y 262,7 no corriente; 403,1 sin descontar, según Control maestro!N51)


### Tipo de negocio y motor

    Minorista británico especializado en productos para mascotas (88 % de los ingresos, margen en caída) más un negocio veterinario que cobra un fee sobre 407 clínicas en joint venture que no controla y que genera la mayor parte de la caja libre.
    DCF de caja libre al accionista de la plantilla (los arrendamientos ya van en el flujo), contrastado con una suma de partes Retail/Vet por la divergencia de márgenes entre segmentos y el riesgo regulatorio de la CMA sobre el fee veterinario.

### calidad

    El negocio se entiende y Vet muestra ventaja en las cifras (margen UPBT 47,4 %, ROIC 18,8 % sin el fondo de comercio del LBO), pero ese ROIC baja a c6 % con todo el capital, el margen bruto del grupo cae de 50,7 % a 45,7 % (siete caídas en ocho años), Retail está en plan de giro con dirección nueva y el fee de Vet queda bajo remedios de la CMA sin cuantificar; la etapa 1 marca el foso como bandera (C18 = No), y aquí queda en duda porque el foso de Vet sí se ve en las cifras.
    Dato clave: Análisis!C24 = 0.188

### caja

    La caja libre base es positiva (60,3 mm tras SBC) y lo ha sido en los cinco años, pero cae de 110,3 a 64,8 (CAGR -12,45 %), bajaría a c52 con el capex guiado de c50 y en FY26 los retornos al accionista se financiaron con 25,7 de deuda nueva; el 2,45x de Análisis!C26 que la hoja da como PASA está inflado (1,53x restando arrendamientos e intereses).
    Dato clave: Análisis!C52 = 60.3

### balance

    Sin arrendamientos, la deuda financiera bruta es 59,0 y la neta 19,4 frente a un EBITDA pre-NIIF 16 de 135,9 (0,14x) y a una caja libre base de 60,3 (c0,3x); el EBITDA pre-NIIF 16 ya resta el alquiler, quedan 260 de RCF sin disponer hasta 2028 y el ABL vence en 2030; el 1,69x de Análisis!C33 incluye arrendamientos y no se usa.
    Dato clave: Deuda financiera neta sin arrendamientos = 19.4 (Control maestro!N36: 19,4/135,9 = 0,14x); deuda bruta sin arrendamientos 59.0 = Análisis!C54 397.8 − arrendamientos 338.8

### precio

    A 2,394 £ cotiza a más del doble del precio de Sí (1,14 £; el mínimo entre el escenario malo y ¾ del ponderado de 2,19 £, que es 1,64 £) y por encima del valor ponderado (margen -9 %), y el DCF inverso exige un 4,3 % anual; con r al 7 % el ponderado (3,11 £) supera el precio, pero ni así el precio de Sí (≤ 2,33 £) lo alcanza.
    Dato clave: Análisis!C37 = 2.394 frente a precio de Sí Análisis!B78 = 1.14273275355557

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja no dice nada concreto sobre encaje, más allá de una capitalización de 1.043,8 mm como dato de contexto.
    Dato clave: Análisis!C41 = 1043.8

### Qué lo cambiaría

    - Que la cotización baje a la zona de 1,14–1,64 £ (precio de Sí y ¾ del ponderado de la hoja) sin deterioro del negocio: pasaría a estudiar_a_fondo.
    - Que los interinos H1 FY27 del 25/11/2026 muestren otra caída del margen bruto de Retail por debajo del 44,4 % o del grupo por debajo del 45 %: la calidad pasaría a no_pasa y el veredicto a descartar.
    - Que la deuda financiera neta sin arrendamientos siga creciendo por financiar retornos con deuda (desde 19,4) o que el FCF base caiga de forma sostenida por debajo de c52: la caja pasaría a no_pasa.

### Qué falta

    - Cuantificación del efecto del Order 2026 de la CMA sobre el take rate del fee de Vet y sobre la adhesión a Care Plans (la hoja dice que nadie lo ha medido).
    - Nivel y umbral de los covenants del RCF (Control maestro!N36: no publicados).
    - Duda de fuentes: la hoja registra «decisiones del inversor» fechadas el 01-nov-2026, posteriores a la fecha de análisis del 26/10/2026; además, la base de FCF usa el capex de FY26 (41,7) y no el guiado de c50.

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

