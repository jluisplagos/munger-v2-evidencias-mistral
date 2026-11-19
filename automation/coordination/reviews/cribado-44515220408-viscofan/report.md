# Cribado · Viscofan

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-07 |
| Tarea | cribado-44515220408-viscofan |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | cd4af95c854eafa7f835cf4ceb178079ea1814eb88776bf097617253183b8710 |
| Huella del envío (bundle_sha256) | 83241a7f2040fb45b3041481250d1c24b0763f59381b13cd4ef72f367e64fa01 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 9ed7015786fb5a8702cf4f3a702e3b840b219f88645afbe9b5e29e640cfe0e10 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 129772 tokens |
| Reserva estimada antes de llamar | USD 1.174448 |
| Uso de tokens | entrada 59138, salida 4835 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.333252; cota 0.333252 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Viscofan/Viscofan_respuesta.md | 3c522e08f471975e4e6032de09505e05879f2e963369f3cd5b4ed9b82344c27e | 32518 |
| cambios_v2 | EMPRESAS_LOTES_COMPLETOS/Viscofan/Viscofan_cambios_v2.md | 5cc68c2bfa0a9e045f6a960a1d999bfcaffb5a285ea26a0d823bae38f95a9156 | 2074 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Viscofan/Viscofan_evaluada.xlsx#Análisis | 471f1aef6f151d501bc711b834ffa94a3149017864579df33484e94882062e5e | 23550 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Viscofan/Viscofan_evaluada.xlsx#Control maestro | 4ffb9e8b0158e6765c98ea5e7bf6916d270c2ecc0d115aefc78c3a0b7f49c89d | 50669 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `vigilar` · DCF de la plantilla aplica: `si`

| Filtro | Resultado |
|---|---|
| calidad | pasa |
| caja | dudoso |
| balance | pasa |
| precio | no_pasa |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51 = 11.87 (incluido en la deuda bruta de Análisis!C54 = 375.75; excluido del cociente de deuda)


### Tipo de negocio y motor

    Fabricante industrial líder de envolturas para embutidos (celulósica, colágeno, fibrosa y plástica): demanda estable de la industria cárnica, con costes de materias primas, energía y divisa cíclicos.
    DCF de caja libre de la plantilla para un negocio estable con costes cíclicos, usando una caja libre normalizada de ciclo medio que incluya años como 2022.

### calidad

    Es un líder de nicho que se entiende (C11 y C12 = Sí): ROIC del 12,6 %, por encima del 9 %, margen EBITDA del 22-26 % en 2019-2025, cuota estimada al alza (30 % → 41 %) y ningún cliente por encima del 10 %, con costes de pieles, gas y divisa como riesgo; discrepo del «DESCARTAR · demasiado difícil» de A6, que nace de C13 (precio) y no del negocio.
    Dato clave: Análisis!C24 = 0.126

### caja

    Convierte bien en caja operativa (CFO/beneficio 1,26 en C26) y la caja libre base es positiva (97,29 M€), pero la caja libre tras intereses no crece (108,7 M€ en 2019 frente a 100,5 M€ en 2025), fue de −1,7 M€ en 2022 y C25 = No, así que la recurrencia y la conversión del EBITDA en caja quedan en duda.
    Dato clave: Análisis!C52 = 97.29

### balance

    Sin arrendamientos, la deuda neta es de unos 305,1 M€ (363,88 − 57,73 de caja − 1,06 de otros activos), frente a un EBITDA LTM de 279,32 M€: ≈1,1x, o 1,04–1,12x según Control maestro con el EBITDA aproximado sin NIIF 16 (no publicado); es holgado para un negocio estable, aunque la caja solo cubre 0,20x la deuda a corto plazo (pólizas de renovación anual, 155,3 M€ no dispuestos a dic-25) y el 1,13x de Análisis!C33 incluye arrendamientos, por lo que no sirve tal cual.
    Dato clave: Control maestro!N51 = 363.88 (deuda bruta sin arrendamientos; deuda neta sin arrendamientos ≈ 363,88 − 57,73 − 1,06 = 305,1 M€)

### precio

    La cotización (53,6 €) dobla el precio de Sí (25,1 €, B78) y supera el ponderado (38,52 €, C83) e incluso el escenario bueno (50,97 €, D78); el DCF inverso exige un crecimiento del 9,3 % (C86), por encima del 8 % del escenario bueno, y aunque con r del 7 % el ponderado llega a 54,99 € (C90), el precio de Sí seguiría muy por debajo.
    Dato clave: Análisis!C37 = 53.6 frente a Análisis!B78 = 25.0705110462092

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja no dice nada concreto sobre encaje, más allá de una capitalización de 2.444,4 M€.
    Dato clave: Análisis!C41 = 2444.4

### Qué lo cambiaría

    - Una cotización cercana o inferior al precio de Sí de 25,1 € (o claramente por debajo del ponderado de 38,5 €) con el negocio intacto pasaría a estudiar_a_fondo.
    - Una caja libre tras intereses sostenida por encima de 140 M€ en 2026-2027, con el capex de 100 M€ ya hecho, despejaría la duda de caja y subiría los valores de la hoja.
    - Una deuda neta sin arrendamientos por encima de 2x EBITDA, o un margen bruto por debajo del 65 % dos años seguidos, llevaría a descartar.

### Qué falta

    - EBITDA LTM después de alquileres (sin NIIF 16), no publicado: el cociente deuda/EBITDA sin arrendamientos es aproximado (≈1,04–1,12x).
    - Umbrales de covenants y calendario de renovación de las pólizas a corto plazo (líneas no dispuestas a jun-26 no encontradas).
    - Puente entre EBITDA y caja libre 2019-2025 (capex de mantenimiento frente a capacidad, circulante e impuestos), y beneficio neto LTM para medir la conversión caja libre/beneficio.

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

